nginx config for reverse proxying Wordpress & WP Super Cache and keeping the load off Apache2
#############################################################################################
:date: 2011-09-30 23:21
:author: kura
:category: tutorials
:tags: apache2, nginx, wordpress, wp-super-cache
:slug: nginx-config-for-reverse-proxying-wordpress-wp-super-cache-and-keeping-the-load-off-apache2

.. contents::
    :backlinks: none

The point
---------

The whole point of this is to get as much load off of Apache as possible
to keep the server running nice and smoothly.

Configuration
-------------

The configuration below will mean that nginx will serve basically
everything;

- static files
- uploaded files and
- cached content

simply replace the **VARIABLES** below and everything should be good to
go, if copy-pasting from below isn't working properly you can download a
full copy from `here`_.

.. _here: /files/2011/09/server.txt

.. code-block:: nginx

    server {
      listen 80;
      server_name **DOMAIN_HERE**;
      access_log /var/log/nginx/access.**DOMAIN_HERE**.log;

      gzip on;
      gzip_disable msie6; # disable gzip for IE6
      gzip_static on;
      gzip_comp_level 9; # highest level of compression
      gzip_proxied any;
      gzip_types text/plain text/css application/x-javascript text/xml application/xml application/xml+rss text/javascript;

      proxy_redirect off;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_pass_header Set-Cookie;root **/PATH/TO/WORDPRESS**;

      # default location, used for the basic proxying
      location / {
        # if we're requesting a file and it exists, return it and bail out
        if (-f $request_filename) {
          break;
        }

        client_max_body_size 2m; # increase this to increase file upload size
        proxy_pass http://localhost:**APACHE_PORT**;
      }

      # handle uploaded files
      location ~* files/ {
        root **/PATH/TO/WORDPRESS**/blogs.dir/**BLOG_ID**/;
      }

      # handle static files
      location ~* \.(jpg|png|gif|jpeg|js|css|mp3|wav|swf|mov|doc|pdf|xls|ppt|docx|pptx|xlsx|txt|htm|html)$ {
        # if the static file doesn't exist, handle it with Apache
        if (!-f $request_filename) {
        break;
        proxy_pass http://localhost:**APACHE_PORT**;
      }

      }

      set $supercache_file "";
      set $supercache_uri $request_uri;

      # reset cache URI if POSTing - bypass cache
      if ($request_method = POST) {
        set $supercache_uri "";
      }

      # bypass cache if there's a query string
      if ($query_string) {
        set $supercache_uri "";
      }

      # bypass cache if one of the cookies below is set
      if ($http_cookie ~* "comment_author_|wordpress|wp-postpass_") {
        set $supercache_uri "";
      }

      # if the URI is still set (rules above don't trigger) then set our file location!
      if ($supercache_uri ~ ^(.+)$) {
        set $supercache_file /wp-content/cache/supercache/$http_host$1index.html;
      }

      # rewrite the request to the cached HTML file
      if (-f $document_root$supercache_file) {
        rewrite ^(.*)$ $supercache_file break;
      }

      # if file exists, return it - will bypass back to Apache if not
      if (-f $request_filename) {
        break;
      }
    }
