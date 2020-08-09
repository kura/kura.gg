Retrying dynamically configured upstreams with OpenResty
########################################################
:date: 2020-08-09 17:00
:author: kura
:category: misc
:tags: nginx, openresty, lua
:slug: retrying-dynamically-configured-upstreams-with-openresty

Preamble
========

OpenResty is a modified version of nginx with LuaJIT compiled in and many
nginx options that can be controlled or modified via Lua. It is very commonly
used in content delivery networks for it's configurability.

As such, we use OpenResty and one of the features we use is the ability to
dynamically modify upstream backends. To achieve this we use some logic within
OpenResty to update upstreams based on DNS records. This means we can pull
upstreams in and out of service via DNS records and have OpenResty
update it's upstream proxy passing configuration without needing to push
configs out to hundreds of servers and reload daemons.

The logic behind how we update the upstream backends is beyond the scope of
this post, so let's just say we have a table of upstream servers.

.. code:: lua

    upstream_servers = {
        port=80,
        ips={"10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"}
    }

Introduction to `balancer_by_lua`
=================================

In nginx you'd normally specify multiple backends in an upstream block.

.. code:: nginx

    upstream backend {
        server 10.0.0.1:80 max_fails=3 fail_timeout=3;
        server 10.0.0.2:80 max_fails=3 fail_timeout=3;
        server 10.0.0.3:80 max_fails=3 fail_timeout=3;
        server 10.0.0.4:80 max_fails=3 fail_timeout=3;
    }

Doing this in OpenResty with a dynamic set of backends is slightly different
and requires using `balancer_by_lua_block` or `balancer_by_lua_file`.

.. code:: lua

    upstream backend {
        server 127.0.0.1:9999 max_fails=3 fail_timeout=3;
        balancer_by_lua_block {
            local balancer = require("ngx.balancer")
            -- ...
        }
    }

Using this as a base we can get `balancer_by_lua` to pick a backend from our
table.

.. code:: lua

    init_by_lua_block {
        local upstream_servers = {
            port=80,
            ips={"10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"}
        }
    }

    upstream backend {
        server 127.0.0.1:9999 max_fails=3 fail_timeout=3;
        balancer_by_lua_block {
            local balancer = require("ngx.balancer")
            local port = upstream_servers["port"]
            local ips = upstream_servers["ips"]
            -- Pick a random backend
            local ip = ips[math.random(#ips)]
            ok, err = balancer.set_current_peer(ip, port)
            if not ok then
                ngx.log(ngx.ERR, "set_current_peer failed: ", err)
                return ngx.exit(500)
            end
        }
    }

With this block each request will pick a random server from the table and use
it for reverse proxying.

This approach is great for multiple reasons; you can dynamically update the
server of backends available, you can add logic to how a backend is chosen,
and more.

The downside to this approach is in using it you are disabling nginx's builtin
retry logic.

Fixing retries
==============

The `ngx.balancer` module of OpenResty has a method for setting up retries and
it's called `set_more_tries`. So let's implement it.

.. code:: lua

    -- DO NOT COPY AND PASTE THIS WITHOUT READING FURTHER. IT HAS A DELIBERATE
    -- BUG TO SHOW HOW JUST USING set_more_tries WON'T WORK.

    init_by_lua_block {
        local upstream_servers = {
            port=80,
            ips={"10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"}
        }
    }

    upstream backend {
        server 127.0.0.1:9999 max_fails=3 fail_timeout=3;
        balancer_by_lua_block {
            local balancer = require("ngx.balancer")
            local port = upstream_servers["port"]
            local ips = upstream_servers["ips"]
            -- Pick a random backend
            local ip = ips[math.random(#ips)]
            
            -- set up more tries using the length of the server list minus 1.
            ok, err = balancer.set_more_tries(#ips - 1)
            if not ok then
                ngx.log(ngx.ERR, "set_more_tries failed: ", err)
            end
            
            ok, err = balancer.set_current_peer(ip, port)
            if not ok then
                ngx.log(ngx.ERR, "set_current_peer failed: ", err)
                return ngx.exit(500)
            end
        }
    }

This approach will allow retries to happen, but it also introduces a bug.
Each time `balancer_by_lua_block` is called it sets `set_more_tries`,
including for retries. Which means a client will retry endlessly.

We can fix that using the request context.

.. code:: lua

    init_by_lua_block {
        local upstream_servers = {
            port=80,
            ips={"10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"}
        }
    }

    upstream backend {
        server 127.0.0.1:9999 max_fails=3 fail_timeout=3;
        balancer_by_lua_block {
            local balancer = require("ngx.balancer")
            local port = upstream_servers["port"]
            local ips = upstream_servers["ips"]
            -- Pick a random backend
            local ip = ips[math.random(#ips)]
            
            -- This block will only trigger if ngx.ctx.retry is not true.
            -- We set this to true during the initial request so future
            -- requests within this context will not go down this path.
            if not ngx.ctx.retry then
                ngx.ctx.retry = true
                -- set up more tries using the length of the server list minus 1.
                ok, err = balancer.set_more_tries(#ips - 1)
                if not ok then
                    ngx.log(ngx.ERR, "set_more_tries failed: ", err)
                end
            end
            
            ok, err = balancer.set_current_peer(ip, port)
            if not ok then
                ngx.log(ngx.ERR, "set_current_peer failed: ", err)
                return ngx.exit(500)
            end
        }
    }

Obviously this approach isn't perfect. It picks a random backend server to use
for the initial request and for retries, which means a client could get
unlucky and hit the same bad backend multiple times. This is just an example
of what you can do with OpenResty and Lua.
