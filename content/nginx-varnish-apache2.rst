WordPress + nginx + Varnish + Apache 2
######################################
:date: 2010-09-26 19:41
:author: kura
:category: tutorials
:tags: apache, nginx, varnish, wordpress
:slug: nginx-varnish-apache2

.. contents::

Lately I've been doing a lot of work with Varnish, this includes testing
it within a load balanced environment, putting it behind nginx, putting
it in front of Solr, the list goes on.

This blog post will hopefully give you an insight in to a simple way of
combining nginx, Varnish and Apache to create a powerful Wordpress
environment that can really take a hammering.

I'm going to assume you already have Apache and nginx working together,
if not I suggest you read my other articles on these subjects to learn
how to combine them.

Installing Varnish
------------------

.. code:: bash

    sudo apt-get install varnish

Configuring Apache
------------------

I suggest binding Apache to port 81, this is easy to change, open the
following file in your favourite editor.

    /etc/apache2/ports.conf

Change the Listen and NameVirtualHost lines to:

.. code:: apache

    Listen 81
    NameVirtualHost *:81

This will mean you need to go and change all of your virtualhost
definitions to work on port 81.

Example below.

.. code:: apache

    <VirtualHost *:81>
        ServerAdmin webmaster@example.com
        ServerName example.com
        DocumentRoot /var/www/website

        CustomLog /var/log/apache2/access.example.com.log combined
        ErrorLog /var/log/apache2/error.example.com.log
    </VirtualHost>

Configuring Varnish
-------------------

Open the following file in your favourite editor

    /etc/varnish/default.vcl

First we define a backend

::

    backend default {
        .host = "localhost";
        .port = "81";
    }

This defines a host, this should be pretty straight forward, we set the
host and port number to use.

Next we define a list of allowed hosts, this is going to be used to
verify if the requester is allowed to use the PURGE request type, this
is used for purging pages on-the-fly and will be explained later.

::

    acl purge {
        "localhost";
    }

Next we set up our vcl_recv method, this is called when a request is
received.

::

    sub vcl_recv {
        set req.grace = 6h;

        if (req.request == "PURGE") {
            if(!client.ip ~ purge) {
                error 405 "Not allowed.";
            }

        purge("req.url ~ ^" req.url "$ && req.http.host == "req.http.host);

        }

        if (req.url ~ ".(jpg|png|gif|gz|tgz|bz2|lzma|tbz)(?.*|)$") {
            remove req.http.Accept-Encoding;
        } elsif (req.http.Accept-Encoding ~ "gzip") {
            set req.http.Accept-Encoding = "gzip";
        } elsif (req.http.Accept-Encoding ~ "deflate") {
            set req.http.Accept-Encoding = "deflate";
        } else {
            remove req.http.Accept-Encoding;
        }

        if (req.url ~ "wp-(login|admin)") {
            return (pass);
        }

        if (req.request != "GET" && req.request != "HEAD") {
            return (pass);
        }

        unset req.http.cookie;

        if (req.url ~ ".(jpeg|jpg|png|gif|ico|swf|js|css|txt|gz|zip|rar|bz2|tgz|tbz|html|htm|pdf|pls|torrent)(?.*|)$") {
            unset req.http.Authenticate;
            unset req.http.POSTDATA;
            set req.request = "GET";
            set req.url = regsub(req.url, "?.*$", "");
            return (lookup);
        }

    }

I should explain what the above method does.

-  We set req.grace to 6 hours, this means that if the cache expires and
   the backend is unreachable Varnish will continue using the cached
   copy for 6 hours. The first if statement checks to see if the request
   type is PURGE, if it is then it looks to see if the requester is in
   the access list, if they are then it purges the requested page. More
   on this later.
-  The next if/elseif/else statement is for handling encoding, it should
   be relatively straight forward.
-  Next we look to see if the url is either wp-login or wp-admin, if it
   is we tell Varnish to pass to the backend and exit the vcl_recv
   function.
-  We then check to see if the request type is neither GET nor HEAD, if
   not we pass to the backend and exit vcl_recv.
-  Next we unset all cookies, this is required since Varnish will not
   cache content when cookies are present.
-  The final if statement checks to see if the url has a static content
   extension, removes all HTTP Auth and POST data, sets the request type
   to GET and removes all QUERY_STRING content from the URL if it is
   static content.

Next is vcl_pipe and vcl_pass.

::

    sub vcl_pipe {
        set bereq.http.connection = "close";
        if (req.http.X-Forwarded-For) {
            set bereq.http.X-Forwarded-For = req.http.X-Forwarded-For;
        } else {
            set bereq.http.X-Forwarded-For = regsub(client.ip, ":.*", "");
        }
    }
    sub vcl_pass {
        set bereq.http.connection = "close";
        if (req.http.X-Forwarded-For) {
            set bereq.http.X-Forwarded-For = req.http.X-Forwarded-For;
        } else {
            set bereq.http.X-Forwarded-For = regsub(client.ip, ":.*", "");
        }
    }

These methods are identical and simply pass our X-Forwarded-For headers
around, this is used within nginx and Apache for logging correct IP
addresses in the access logs.

::

    sub vcl_fetch {
        set beresp.ttl = 1h;
        set req.grace = 6h;
        if (req.url ~ "wp-(login|admin)") {
            return (pass);
        }

        unset beresp.http.set-cookie;

        if (req.url ~ ".(jpeg|jpg|png|gif|ico|swf|js|css|txt|gz|zip|rar|bz2|tgz|tbz|html|htm|pdf|pls|torrent)$") {
            set beresp.ttl = 24h;
        }
    }

This method is where content is returned from Varnish back to nginx.

-  First we set the TTL of the cache to 1 hour.
-  We again set the grace period as above in vcl_recv,
-  again we check for wp-login or wp-admin and drop out of the method if
   it's found, this stops admin pages being cached.
-  Next we unset the Set-Cookie header
-  and finally if we detect the url contains a static content extension
   we set the TTL of the cache to 24 hours.

And last but not least is vcl_deliver, this one simply adds some
X-Cache header information for debug purposes and can be ignored.

::

    sub vcl_deliver {
        if (obj.hits > 0) {
            set resp.http.X-Cache = "HIT";
            set resp.http.X-Cache-Hits = obj.hits;
        } else {
            set resp.http.X-Cache = "MISS";
        }
    }

Varnish is now configured.

You can find a copy of my default.vcl file here -
`https://kura.io/static/files/syslog-varnish-default-vcl-26-sept-2010`_

.. _`https://kura.io/static/files/syslog-varnish-default-vcl-26-sept-2010`: https://kura.io/static/files/syslog-varnish-default-vcl-26-sept-2010

Configuring nginx
-----------------

.. code:: nginx

    server {
        listen 80;
        server_name example.com;
        access_log /var/log/nginx/access.example.com.log;

        gzip on;
        gzip_disable msie6;
        gzip_static on;
        gzip_comp_level 9;
        gzip_proxied any;
        gzip_types text/plain text/css application/x-javascript text/xml application/xml application/xml+rss text/javascript;

        location / {
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass_header Set-Cookie;
            proxy_pass http://localhost:6081;
        }
    }

This nginx host config should be simple to those of you who've read my
other articles, if not then here's a quick summary;

-  listen and server_name are simply the port to listen on and the
   domain name,
-  gzip enables gzip,
-  gzip_disable tells nginx not to gzip compress for IE6,
-  gzip_static is on to enable compression of static content (jpeg, gif
   etc),
-  gzip_comp_level is the level of compression, 1-9 (higher = more
   compressed)
-  gzip_proxied is set to any to gzip proxied content
-  and finally we set the types of files to gzip.
-  Next we set up our location,
-  disable proxy redirects
-  set Host, X-Real-Ip and X-Forwarded-For headers
-  pass back the Set-Cookie header
-  and pass the connection over to Varnish.

Finishing up
------------

Now we simply need to restart the services

    /etc/init.d/apache2 force-reload && /etc/init.d/varnish restart && /etc/init.d/nginx reload

Testing
-------

Now you can browse your site and it should be going through nginx and
Varnish and only hitting Apache if the content is not cached or if
you're using the WordPress admin panel or doing a POST request.

You can test this with Live HTTP Headers extension for Firefox -
`https://addons.mozilla.org/en-US/firefox/addon/3829/`_ (this will only
work if you used my vcl_delivery method in your Varnish config).

.. _`https://addons.mozilla.org/en-US/firefox/addon/3829/`: https://addons.mozilla.org/en-US/firefox/addon/3829/

Go to a page on your site, refresh a few times, open up Live HTTP
Headers and refresh again, you should see the following

::

    HTTP/1.1 200 OK
    Server: nginx
    ... snip ...
    Via: 1.1 varnish
    X-Cache: HIT
    X-Cache-Hits: <numeric value>
