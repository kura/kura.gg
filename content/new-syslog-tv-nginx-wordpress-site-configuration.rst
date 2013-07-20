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

.. code:: nginx

    upstream backend {
        server 127.0.0.1:81 fail_timeout=120s;
    }

    server {
        listen 80;
        server_name syslog.tv;

        access_log /var/log/nginx/access.syslog.tv.log;

        gzip on;
        gzip_disable msie6;
        gzip_static on;
        gzip_comp_level 9;
        gzip_proxied any;
        gzip_types text/plain text/css application/x-javascript text/xml
        application/xml application/xml+rss text/javascript;

       location / {
            root /var/www/syslog.tv;

            set $wordpress_logged_in "";
            set $comment_author_email "";
            set $comment_author "";

            if ($http_cookie ~* "wordpress_logged_in_[^=]*=([^%]+)%7C") {
                 set $wordpress_logged_in wordpress_logged_in_$1;
            }

            if ($http_cookie ~* "comment_author_email_[^=]*=([^;]+)(;|$)") {
                set $comment_author_email comment_author_email_$1;
            }

            if ($http_cookie ~* "comment_author_[^=]*=([^;]+)(;|$)") {
                set $comment_author comment_author_$1;
            }

            set $my_cache_key "$scheme://$host$uri$is_args$args$wordpress_logged_in$comment_author_email$comment_author";

            client_max_body_size 8m;

            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass_header Set-Cookie;
            proxy_cache cache;
            proxy_cache_key $my_cache_key;
            proxy_cache_valid 200 302 60m;
            proxy_cache_valid 404 1m;
            proxy_pass http://backend;
        }

        location ~* .(jpg|png|gif|jpeg|js|css|mp3|wav|swf|mov|doc|pdf|xls|ppt|docx|pptx|xlsx)$ {
            root /var/www/syslog.tv;
        }
    }

Sadly Wordpress messes up the config when displayed like that so you can
view the proper version `here`_.

.. _here: https://kura.io/satic/files/syslog-nginx-config-18-apr-2010

Explanation
-----------

It'd be a good idea to actually explain what the configuration is doing
and why it's configured that way, I'll do this "chunk-by-chunk".

upstream
~~~~~~~~

.. code:: nginx

    upstream backend {
        server 127.0.0.1:81 fail_timeout=120s;
    }

This one is relatively simple, it basically configures an upstream proxy
to 127.0.0.1 on port 81, fail_timeout controls how long nginx will try
talking to that server before giving up.

I'll assume you understand the basic listen, server_name and
access_log parameters in the first section of the server definition.

gzip
~~~~

.. code:: nginx

    gzip on;
    gzip_disable msie6;
    gzip_static on;
    gzip_comp_level 9;
    gzip_proxied any;
    gzip_types text/plain text/css application/x-javascript text/xml
    application/xml application/xml+rss text/javascript;

Again, this one is rather simple. We enabled GZIP, disable it for anyone
still using IE6, we explicitly enable GZIP compression of static files,
set the compression level to 9 which is the highest level but also uses
the most resource, tell GZIP to compress any proxied data and then set
the mimetypes which GZIP is allowed to compress.

location
~~~~~~~~

.. code:: nginx

    root /var/www/syslog.tv;

    set $wordpress_logged_in "";
    set $comment_author_email "";
    set $comment_author "";

    if ($http_cookie ~* "wordpress_logged_in_[^=]*=([^%]+)%7C") {
        set $wordpress_logged_in wordpress_logged_in_$1;
    }

    if ($http_cookie ~* "comment_author_email_[^=]*=([^;]+)(;|$)") {
        set $comment_author_email comment_author_email_$1;
    }

    if ($http_cookie ~* "comment_author_[^=]*=([^;]+)(;|$)") {
        set $comment_author comment_author_$1;
    }

This is a rather large chunk but is very simple once you understand it.
I'm setting up my document root, then setting some basic variables for
"" so that I can overwrite them further down. This is actually by the
following set of three if statements. I check for three different HTTP
cookies and then set the relevant variable to the correct value if it
exists, this is later used in the cache key to make sure each user has
their own private cache if they have certain cookies.

$my_cache_key
~~~~~~~~~~~~~~~

.. code:: nginx

    set $my_cache_key "$scheme://$host$uri$is_args$args$wordpress_logged_in$comment_author_email$comment_author";

This sets up a variable called $my_cache_key which contains the
current scheme (HTTP or HTTPS), host (syslog.tv), uri, various arguments
and then finally sets the variables from the previous block from the
cookie checks.

Proxy time!
~~~~~~~~~~~

.. code:: nginx

    client_max_body_size 8m;

    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass_header Set-Cookie;
    proxy_cache cache;
    proxy_cache_key $my_cache_key;
    proxy_cache_valid 200 302 60m;
    proxy_cache_valid 404 1m;
    proxy_pass http://backend;

Here I am setting the maximum size of the client body content to 8MB,
disabling proxy redirects, passing through some basic headers to the
backend which allows my backend system to see which host the user is
trying to access, their real IP address rather than the IP of the nginx
server and x-Forwarded-For also contains the users IP address, it's
basically standard when proxying.

Next I pass Set-Cookie headers back to the backend, tell it to use a
cache definition called "cache" which I set up in a `previous blog
post`_. I set the proxy_cache_key to use the variable defined earlier
contains all of the users cookie information in it's key to make it a
private cache.

.. _previous blog post: http://syslog.tv/2010/02/14/more-nginx-proxy_cache-optimizations-and-nginx-load-balancing/

I then pass through some basic validation rules that set HTTP 200 and
302 responses to cache for 60 minutes and 404 responses to cache for 1
minute, then I simply pass back to the backend system.

Static location block
~~~~~~~~~~~~~~~~~~~~~

.. code:: nginx

    location ~* .(jpg|png|gif|jpeg|js|css|mp3|wav|swf|mov|doc|pdf|xls|ppt|docx|pptx|xlsx)$ {
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
