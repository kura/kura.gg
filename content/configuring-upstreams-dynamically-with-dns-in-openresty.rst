Configuring upstreams dynamically with DNS in OpenResty
#######################################################
:date: 2020-08-30 17:30
:author: kura
:category: misc
:tags: nginx, openresty, lua
:slug: configuring-upstreams-dynamically-with-dns-in-openresty
:series: OpenResty upstreams

.. contents::
    :backlinks: none

This article is a continuation of `retrying dynamically configured
upstreams <{filename}/retrying-dynamically-configured-upstreams-with-openresty.rst>`_
that gives an example of how you can configure OpenResty to update your
upstream backend servers dynamically with DNS.

Breaking down `init_worker_by_lua_block`
========================================

`init_worker_by_lua_block` can be used to make an nginx worker do some fun
stuff. In this instance we're going to use it in conjunction with
`ngx.timer.every` and the `resty.dns.resolver`.

Here is the full example of my `init_worker_by_lua_block`.

.. code:: lua

    init_worker_by_lua_block {
        _backend_servers = {}

        local function update_dns()
            -- Set up the resolver
            local resolver = require "resty.dns.resolver"
            local r, err = resolver:new{
                nameservers = {"1.1.1.1", {"1.0.0.1", 53} },  -- Cloudflare
                retrans = 5,  -- 5 retransmissions on receive timeout
                timeout = 1000,  -- 1 sec
            }
            if not r then
                ngx.log(ngx.ERR, "failed to instantiate resolver: ", err)
                return
            end

            -- Pull DNS records
            -- Use a hardcoded domain to make this example easier
            local answers, err, tries = r:query("kura.gg", nil, {})
            if not answers then
                ngx.log(ngx.ERR, "failed to query resolved: ", err)
                return
            end
            if answers.errcode then
                ngx.log(ngx.ERR, "server returned error code: ", answers.errcode,
                        ": ", answers.errstr)
                -- Have a return here so that the old servers remain even if
                -- this lookup fails.
                return
            end

            -- Dump records in a global variable
            -- Note I am only pulling out addresses not CNAMEs
            _new_backend_servers = {}
            for i, ans in ipairs(answers) do
                table.insert(_new_backend_servers, ans.address)
            end
            _backend_servers = _new_backend_servers
        end

        -- Run an at timer to force update_dns to trigger on worker init
        ngx.timer.at(0, update_dns)
        -- Set a timer to run every 10 seconds
        ngx.timer.every(10, update_dns)
    }

Configuring the DNS resolver
----------------------------

Let's break this block down in to easier to understand blocks.

.. code:: lua

    _backend_servers = {}

Here we define an empty backend servers table that'll be modified by modified
by DNS resolver and is used by the balancer module for direction clients.

.. code:: lua

    local function update_dns()
        -- Set up the resolver
        local resolver = require "resty.dns.resolver"
        local r, err = resolver:new{
            nameservers = {"1.1.1.1", {"1.0.0.1", 53} },  -- Cloudflare
            retrans = 5,  -- 5 retransmissions on receive timeout
            timeout = 1000,  -- 1 sec
        }

Here we're defining the `update_dns` function and within that setting up a
DNS resolver using the `resty.dns.resolver` module.
I'm using Cloudflare's DNS servers in this example with 5 retransmissions and
a timeout of 1 second.

.. code:: lua

    if not r then
        ngx.log(ngx.ERR, "failed to instantiate resolver: ", err)
        return
    end

If instantiating the resolver fails, the function will return, leaving the
backend server table unmodified. If this happens randomly during operation then
the old server table will remain in use. If it fails during start up, the
backend server table will be empty and cause `HTTP 500` errors to be thrown
(this is set up later.)

Querying the DNS resolver
-------------------------

.. code:: lua

    -- Pull DNS records
    -- Use a hardcoded domain to make this example easier
    local answers, err, tries = r:query("kura.gg", nil, {})
    if not answers then
        ngx.log(ngx.ERR, "failed to query resolved: ", err)
        return
    end

Here we query the DNS server for records, I'm using my own domain `kura.gg` in
this example. 

.. code:: lua

    if answers.errcode then
        ngx.log(ngx.ERR, "server returned error code: ", answers.errcode,
                ": ", answers.errstr)
        -- Have a return here so that the old servers remain even if
        -- this lookup fails.
        return
    end

If querying the records fails or if no records are found the
function will return and leave the backend server table unmodified, allowing
clients to attempt to use the old servers if they're still alive.

Using the returned DNS records to configure the backend
-------------------------------------------------------

.. code:: lua

        -- Dump records in a global variable
        -- Note I am only pulling out addresses not CNAMEs
        _new_backend_servers = {}
        for i, ans in ipairs(answers) do
            table.insert(_new_backend_servers, ans.address)
        end
        _backend_servers = _new_backend_servers
    end

Finally we reach this block if no errors have occured. This will create a new
table of backend servers from the DNS records queried and replace the old table
with the new one.

It's worth noting that this code will only store records that have an `A` or
`AAAA` record, not `CNAMES` etc. Although it's easy enough to modify it to
change this behaviour.

Set up a timer to update the backend servers periodically
---------------------------------------------------------

.. code:: lua

    -- Run an at timer to force update_dns to trigger on worker init
    ngx.timer.at(0, update_dns)
    -- Set a timer to run every 10 seconds
    ngx.timer.every(10, update_dns)
    
Here we're setting up 2 timers. The first is an `ngx.timer.at` timer that
tiggers when a worker is started to attempt to set up the backend server table
on worker init.

The second is an `ngx.timer.every` timer that runs in the worker every 10
seconds.

Each worker will do this and have it's own copy of the backend servers table.

Breaking down `balancer_by_lua_block`
=====================================

Just like in the  `retrying dynamically configured
upstreams <{filename}/retrying-dynamically-configured-upstreams-with-openresty.rst>`_
article we'll use OpenResty's `balancer_by_lua_block` to allow the balancer
to use these records.

.. code:: lua

    balancer_by_lua_block {
        local balancer = require("ngx.balancer")

        if #_backend_servers == 0 then
            ngx.log(ngx.ERR, "no backend servers available")
            return ngx.exit(500)

        -- This block will only trigger if ngx.ctx.retry is not true.
        -- We set this to true during the initial request so future
        -- requests within this context will not go down this path.
        if not ngx.ctx.retry then
            ngx.ctx.retry = true
            -- Pick a random backend to start with
            server = _backend_servers[math.random(#_backend_servers)]

            -- Kinda messy but, create a context table we dump tried
            -- backends to.
            ngx.ctx.tried = {}
            ngx.ctx.tried[server] = true

            -- set up more tries using the length of the server list minus 1.
            ok, err = balancer.set_more_tries(#_backend_servers - 1)
            if not ok then
                ngx.log(ngx.ERR, "set_more_tries failed: ", err)
            end

        else
            -- This block will trigger on a retry
            -- Here we'll run through the backends and pick one we haven't
            -- tried yet.
            for i, ip in ipairs(_backend_servers) do
                in_ctx = ngx.ctx.tried[ip] ~= nil
                if in_ctx == false then
                    ngx.ctx.tried[ip] = true
                    server = ip
                    break
                end
            end
        end

        -- Hardcoded port again to make example easier
        ok, err = balancer.set_current_peer(server, 443)
        if not ok then
            ngx.log(ngx.ERR, "set_current_peer failed: ", err)
            return ngx.exit(500)
        end
    }

As with the `init_worker_by_lua_block` I'll break the `balancer_by_lua_block`
block down in more manageable chunks.

Setting up balancer_by_lua
--------------------------

.. code:: lua

    local balancer = require("ngx.balancer")

    if #_backend_servers == 0 then
        ngx.log(ngx.ERR, "no backend servers available")
        return ngx.exit(500)
    end

First thing we do is include the `ngx.balancer` module, then we check to see
if the backend servers table has any records. If not all we can do is write
an error message to log and send the client an `HTTP 500` because we have no
backends available.

Handling an initial request
---------------------------

.. code:: lua

    -- This block will only trigger if ngx.ctx.retry is not true or is
    -- unset.
    -- We set this to true during the initial request so future
    -- requests within this context will not go down this path.
    if not ngx.ctx.retry then
        ngx.ctx.retry = true
        -- Pick a random backend to start with
        server = _backend_servers[math.random(#_backend_servers)]

        -- Kinda messy but, create a context table we dump tried
        -- backends to.
        ngx.ctx.tried = {}
        ngx.ctx.tried[server] = true

        -- set up more tries using the length of the server list minus 1.
        ok, err = balancer.set_more_tries(#_backend_servers - 1)
        if not ok then
            ngx.log(ngx.ERR, "set_more_tries failed: ", err)
        end

Here we set up what happens when `ngx.ctx.retry` is undefined or false, which
will happen on first request for a client.

Within this block we pick a random backend, set up a table of addresses already
tried so if a retry is necessary it won't use the same host.

Then we set the number of retries to attempt as the length of the server table
minus one.

Handling a retry request
------------------------

.. code:: lua

    else
        -- This block will trigger on a retry
        -- Here we'll run through the backends and pick one we haven't
        -- tried yet.
        for i, ip in ipairs(_backend_servers) do
            in_ctx = ngx.ctx.tried[ip] ~= nil
            if in_ctx == false then
                ngx.ctx.tried[ip] = true
                server = ip
                break
            end
        end
    end

This block is what will be called if the request is a retry. In it we simply
iterate through the backend server table looking for a backend we haven't tried
yet. Once we find one we add it to the list of servers tried and break the loop
to send the client to that server.

Passing the request back to nginx
---------------------------------

.. code:: lua

    -- Hardcoded port again to make example easier
    ok, err = balancer.set_current_peer(server, 443)
    if not ok then
        ngx.log(ngx.ERR, "set_current_peer failed: ", err)
        return ngx.exit(500)
    end

This final block is where nginx is told which backend to send the client to.

Putting it all together
=======================

Below is the full example written as a single `nginx.conf`. Sadly syntax
highlighters have issues with nginx and Lua in a single file.

.. code:: nginx

    # set 2 worker processes to show the timer spawning on each one
    worker_processes 2;

    events {
        worker_connections 1024;
    }

    http {

        # Do this for each worker so each worker has it's own copy of the DNS
        # records.
        init_worker_by_lua_block {
            _backend_servers = {}
        
            local function update_dns()
                -- Set up the resolver
                local resolver = require "resty.dns.resolver"
                local r, err = resolver:new{
                    nameservers = {"1.1.1.1", {"1.0.0.1", 53} },  -- Cloudflare
                    retrans = 5,  -- 5 retransmissions on receive timeout
                    timeout = 1000,  -- 1 sec
                }
                if not r then
                    ngx.log(ngx.ERR, "failed to instantiate resolver: ", err)
                    return
                end

                -- Pull DNS records
                -- Use a hardcoded domain to make this example easier
                local answers, err, tries = r:query("kura.gg", nil, {})
                if not answers then
                    ngx.log(ngx.ERR, "failed to query resolved: ", err)
                    return
                end
                if answers.errcode then
                    ngx.log(ngx.ERR, "server returned error code: ", answers.errcode,
                            ": ", answers.errstr)
                    -- Have a return here so that the old servers remain even if
                    -- this lookup fails.
                    return
                end

                -- Dump records in a global variable
                -- Note I am only pulling out addresses not CNAMEs
                _new_backend_servers = {}
                for i, ans in ipairs(answers) do
                    table.insert(_new_backend_servers, ans.address)
                end
                _backend_servers = _new_backend_servers
            end

            -- Run an at timer to force update_dns to trigger on worker init
            ngx.timer.at(0, update_dns)
            -- Set a timer to run every 10 seconds
            ngx.timer.every(10, update_dns)
        }

        upstream backend {
            server 127.0.0.1;

            balancer_by_lua_block {
                local balancer = require("ngx.balancer")

                if #_backend_servers == 0 then
                    ngx.log(ngx.ERR, "no backend servers available")
                    return ngx.exit(500)
                end

                -- This block will only trigger if ngx.ctx.retry is not true or is
                -- unset.
                -- We set this to true during the initial request so future
                -- requests within this context will not go down this path.
                if not ngx.ctx.retry then
                    ngx.ctx.retry = true
                    -- Pick a random backend to start with
                    server = _backend_servers[math.random(#_backend_servers)]

                    -- Kinda messy but, create a context table we dump tried
                    -- backends to.
                    ngx.ctx.tried = {}
                    ngx.ctx.tried[server] = true

                    -- set up more tries using the length of the server list minus 1.
                    ok, err = balancer.set_more_tries(#_backend_servers - 1)
                    if not ok then
                        ngx.log(ngx.ERR, "set_more_tries failed: ", err)
                    end

                else
                    -- This block will trigger on a retry
                    -- Here we'll run through the backends and pick one we haven't
                    -- tried yet.
                    for i, ip in ipairs(_backend_servers) do
                        in_ctx = ngx.ctx.tried[ip] ~= nil
                        if in_ctx == false then
                            ngx.ctx.tried[ip] = true
                            server = ip
                            break
                        end
                    end
                end

                -- Hardcoded port again to make example easier
                ok, err = balancer.set_current_peer(server, 443)
                if not ok then
                    ngx.log(ngx.ERR, "set_current_peer failed: ", err)
                    return ngx.exit(500)
                end
            }
        }

        server {
            listen 80;
            server_name localhost;

            location / {
                proxy_pass https://backend;
            }
        }

    }


Full example on GitHub
======================

The full example nginx config is `available on GitHub
<https://github.com/kura/openresty-upstream-dns-example/blob/master/nginx.conf>`__
so you can quickly spin it up yourself and try it out.