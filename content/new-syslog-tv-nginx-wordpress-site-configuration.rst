New syslog.tv nginx wordpress site configuration explained
##########################################################
:date: 2010-04-18 12:51
:author: kura
:category: tutorials
:tags: apache, cache, nginx, proxy, proxy_cache, wordpress
:slug: new-syslog-tv-nginx-wordpress-site-configuration

Configuration changes
---------------------

I made some modifications to my nginx configuration this weekend to
improve performance and clear up some bugs.

::

    upstream backend {
        server 127.0.0.1:81 fail\_timeout=120s;
    }

    server {
        listen 80;
        server\_name syslog.tv;

        access\_log /var/log/nginx/access.syslog.tv.log;

        gzip on;
        gzip\_disable msie6;
        gzip\_static on;
        gzip\_comp\_level 9;
        gzip\_proxied any;
        gzip\_types text/plain text/css application/x-javascript text/xml
        application/xml application/xml+rss text/javascript;

       location / {
            root /var/www/syslog.tv;

            set $wordpress\_logged\_in "";
            set $comment\_author\_email "";
            set $comment\_author "";

            if ($http\_cookie ~\* "wordpress\_logged\_in\_[^=]\*=([^%]+)%7C") {
                 set $wordpress\_logged\_in wordpress\_logged\_in\_$1;
            }

            if ($http\_cookie ~\* "comment\_author\_email\_[^=]\*=([^;]+)(;\|$)") {
                set $comment\_author\_email comment\_author\_email\_$1;
            }

            if ($http\_cookie ~\* "comment\_author\_[^=]\*=([^;]+)(;\|$)") {
                set $comment\_author comment\_author\_$1;
            }

            set $my\_cache\_key "$scheme://$host$uri$is\_args$args$wordpress\_logged\_in$comment\_author\_email$comment\_author";

            client\_max\_body\_size 8m;

            proxy\_redirect off;
            proxy\_set\_header Host $host;
            proxy\_set\_header X-Real-IP $remote\_addr;
            proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
            proxy\_pass\_header Set-Cookie;
            proxy\_cache cache;
            proxy\_cache\_key $my\_cache\_key;
            proxy\_cache\_valid 200 302 60m;
            proxy\_cache\_valid 404 1m;
            proxy\_pass http://backend;
        }

        location ~\* .(jpg\|png\|gif\|jpeg\|js\|css\|mp3\|wav\|swf\|mov\|doc\|pdf\|xls\|ppt\|docx\|pptx\|xlsx)$ {
            root /var/www/syslog.tv;
        }
    }

Sadly Wordpress messes up the config when displayed like that so you can
view the proper version `here`_.

.. _here: http://syslog.tv/downloads/syslog-nginx-config-18-apr-2010

Explanation
-----------

It'd be a good idea to actually explain what the configuration is doing
and why it's configured that way, I'll do this "chunk-by-chunk".

upstream
~~~~~~~~

::

    upstream backend {
        server 127.0.0.1:81 fail\_timeout=120s;
    }

This one is relatively simple, it basically configures an upstream proxy
to 127.0.0.1 on port 81, fail\_timeout controls how long nginx will try
talking to that server before giving up.

I'll assume you understand the basic listen, server\_name and
access\_log parameters in the first section of the server definition.

gzip
~~~~

::

    gzip on;
    gzip\_disable msie6;
    gzip\_static on;
    gzip\_comp\_level 9;
    gzip\_proxied any;
    gzip\_types text/plain text/css application/x-javascript text/xml
    application/xml application/xml+rss text/javascript;

Again, this one is rather simple. We enabled GZIP, disable it for anyone
still using IE6, we explicitly enable GZIP compression of static files,
set the compression level to 9 which is the highest level but also uses
the most resource, tell GZIP to compress any proxied data and then set
the mimetypes which GZIP is allowed to compress.

location
~~~~~~~~

::

    root /var/www/syslog.tv;

    set $wordpress\_logged\_in "";
    set $comment\_author\_email "";
    set $comment\_author "";

    if ($http\_cookie ~\* "wordpress\_logged\_in\_[^=]\*=([^%]+)%7C") {
        set $wordpress\_logged\_in wordpress\_logged\_in\_$1;
    }

    if ($http\_cookie ~\* "comment\_author\_email\_[^=]\*=([^;]+)(;\|$)") {
        set $comment\_author\_email comment\_author\_email\_$1;
    }

    if ($http\_cookie ~\* "comment\_author\_[^=]\*=([^;]+)(;\|$)") {
        set $comment\_author comment\_author\_$1;
    }

This is a rather large chunk but is very simple once you understand it.
I'm setting up my document root, then setting some basic variables for
"" so that I can overwrite them further down. This is actually by the
following set of three if statements. I check for three different HTTP
cookies and then set the relevant variable to the correct value if it
exists, this is later used in the cache key to make sure each user has
their own private cache if they have certain cookies.

$my\_cache\_key
~~~~~~~~~~~~~~~

::

    set $my\_cache\_key
    "$scheme://$host$uri$is\_args$args$wordpress\_logged\_in$comment\_author\_email$comment\_author";

This sets up a variable called $my\_cache\_key which contains the
current scheme (HTTP or HTTPS), host (syslog.tv), uri, various arguments
and then finally sets the variables from the previous block from the
cookie checks.

Proxy time!
~~~~~~~~~~~

::

    client\_max\_body\_size 8m;

    proxy\_redirect off;
    proxy\_set\_header Host $host;
    proxy\_set\_header X-Real-IP $remote\_addr;
    proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
    proxy\_pass\_header Set-Cookie;
    proxy\_cache cache;
    proxy\_cache\_key $my\_cache\_key;
    proxy\_cache\_valid 200 302 60m;
    proxy\_cache\_valid 404 1m;
    proxy\_pass http://backend;

Here I am setting the maximum size of the client body content to 8MB,
disabling proxy redirects, passing through some basic headers to the
backend which allows my backend system to see which host the user is
trying to access, their real IP address rather than the IP of the nginx
server and x-Forwarded-For also contains the users IP address, it's
basically standard when proxying.

Next I pass Set-Cookie headers back to the backend, tell it to use a
cache definition called "cache" which I set up in a `previous blog
post`_. I set the proxy\_cache\_key to use the variable defined earlier
contains all of the users cookie information in it's key to make it a
private cache.

.. _previous blog post: http://syslog.tv/2010/02/14/more-nginx-proxy_cache-optimizations-and-nginx-load-balancing/

I then pass through some basic validation rules that set HTTP 200 and
302 responses to cache for 60 minutes and 404 responses to cache for 1
minute, then I simply pass back to the backend system.

Static location block
~~~~~~~~~~~~~~~~~~~~~

::

    location ~\* .(jpg\|png\|gif\|jpeg\|js\|css\|mp3\|wav\|swf\|mov\|doc\|pdf\|xls\|ppt\|docx\|pptx\|xlsx)$ {
        root /var/www/syslog.tv;
    }

This one could look a little scary but is actually really simple. I do a
location check again some defined extensions, if it matches then it will
simply serve these up from nginx rather than reverse proxy.

In layman's terms
-----------------

Although possibly daunting it really is quite simple, I am configuring
nginx to reverse proxy back to Apache on port 81, setting up some GZIP
compression rules to decrease the size of static files, checking to see
if a user has a WordPress cookie and giving them a private cache if they
do, serving dynamic (PHP) content via the reverse proxy to Apache if no
cache exists, serving cached content from nginx and also serving static
content from nginx.

This basically means that Apache is used very sparingly and nginx is
doing what it does best, serving static/cached content.
