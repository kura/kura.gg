nginx config for reverse proxying Wordpress & WP Super Cache and keeping the load off Apache2
#############################################################################################
:date: 2011-09-30 23:21
:author: kura
:category: tutorials
:tags: apache2, nginx, wordpress, wp-super-cache
:slug: nginx-config-for-reverse-proxying-wordpress-wp-super-cache-and-keeping-the-load-off-apache2

The point
---------

The whole point of this is to get as much load off of Apache as possible
to keep the server running nice and smoothly.

Configuration
-------------

The configuration below will mean that nginx will serve basically
everything;

-  static files
-  uploaded files and
-  cached content

simply replace the **VARIABLES** below and everything should be good to
go, if copy-pasting from below isn't working properly you can download a
full copy from `here`_.

.. _here: http://syslog.tv/files/2011/09/server.txt

::

    server {
      listen 80;
      server\_name **DOMAIN\_HERE**;
      access\_log /var/log/nginx/access.**DOMAIN\_HERE**.log;

      gzip on;
      gzip\_disable msie6; # disable gzip for IE6
      gzip\_static on;
      gzip\_comp\_level 9; # highest level of compression
      gzip\_proxied any;
      gzip\_types text/plain text/css application/x-javascript text/xml application/xml application/xml+rss text/javascript;

      proxy\_redirect off;
      proxy\_set\_header Host $host;
      proxy\_set\_header X-Real-IP $remote\_addr;
      proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
      proxy\_pass\_header Set-Cookie;root **/PATH/TO/WORDPRESS**;

      # default location, used for the basic proxying
      location / {
        # if we're requesting a file and it exists, return it and bail out
        if (-f $request\_filename) {
          break;
        }

        client\_max\_body\_size 2m; # increase this to increase file upload size
        proxy\_pass http://localhost:**APACHE\_PORT**;
      }

      # handle uploaded files
      location ~\* files/ {
        root **/PATH/TO/WORDPRESS**/blogs.dir/**BLOG\_ID**/;
      }

      # handle static files
      location ~\* \\.(jpg\|png\|gif\|jpeg\|js\|css\|mp3\|wav\|swf\|mov\|doc\|pdf\|xls\|ppt\|docx\|pptx\|xlsx\|txt\|htm\|html)$ {
        # if the static file doesn't exist, handle it with Apache
        if (!-f $request\_filename) {
        break;
        proxy\_pass http://localhost:**APACHE\_PORT**;
      }

      }

      set $supercache\_file "";
      set $supercache\_uri $request\_uri;

      # reset cache URI if POSTing - bypass cache
      if ($request\_method = POST) {
        set $supercache\_uri "";
      }

      # bypass cache if there's a query string
      if ($query\_string) {
        set $supercache\_uri "";
      }

      # bypass cache if one of the cookies below is set
      if ($http\_cookie ~\* "comment\_author\_\|wordpress\|wp-postpass\_") {
        set $supercache\_uri "";
      }

      # if the URI is still set (rules above don't trigger) then set our file location!
      if ($supercache\_uri ~ ^(.+)$) {
        set $supercache\_file /wp-content/cache/supercache/$http\_host$1index.html;
      }

      # rewrite the request to the cached HTML file
      if (-f $document\_root$supercache\_file) {
        rewrite ^(.\*)$ $supercache\_file break;
      }

      # if file exists, return it - will bypass back to Apache if not
      if (-f $request\_filename) {
        break;
      }
    }
