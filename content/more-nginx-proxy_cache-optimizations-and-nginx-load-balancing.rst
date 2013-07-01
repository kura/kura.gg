More nginx proxy_cache optimizations and nginx load balancing
##############################################################
:date: 2010-02-14 14:27
:author: kura
:category: apache, debian, howto, nginx, ubuntu
:tags: apache, cache, debian, howto, load balancing, nginx, ubuntu, wordpress
:slug: more-nginx-proxy_cache-optimizations-and-nginx-load-balancing

This is yet another follow up to post to several previous posts about
using nginx as a reverse proxy with caching. It is actually a direct
addition to my post from a week or so ago which outlined how to actually
using nginx's proxy caching feature which can be read here --
`http://syslog.tv/2010/02/07/nginx-proxy\_cache-and-explained-benchmarked/`_.

.. _`http://syslog.tv/2010/02/07/nginx-proxy\_cache-and-explained-benchmarked/`: https://syslog.tv/2010/02/07/nginx-proxy_cache-and-explained-benchmarked/

Even more changes?
------------------

Yes, even more changes, these are basic changes that are there to
improve the caching capabilities and also implement load balancing.

Cache changes
~~~~~~~~~~~~~

The first set of changes are in the main nginx configuration file

    /etc/nginx/nginx.conf

These changes basically just change the proxy\_cache key

    proxy\_cache\_path /var/www/nginx\_cache levels=1:2 keys\_zone=cache:8m max\_size=1000m inactive=600m;
    proxy\_temp\_path /tmp/nginx;
    proxy\_cache\_key "$scheme://$host$request\_uri";

I've decided to put the temporary caches file in to an nginx specific
directory, just to separate them from other cache files. I've also
modified the proxy\_cache\_key to add the following variables:

-  **$scheme** - This will be the protocol; http or https
-  **$host** - Host name, this will be set as syslog.tv for me
-  **$request\_uri** - The full request uri, this is simple

Why add these variables? Quite simple really, it means I can have
multiple sites running with proxy caching enabled and have them set a
meaningful key so they don't clash.

Load balancing changes
~~~~~~~~~~~~~~~~~~~~~~

The next set of changes will be specific to my site specific
configuration file, the first of which is an addition on an upstream
definition.

/etc/nginx/sites-available/syslog.tv

::

    upstream apachesyslogtv {
        server apache.syslog.tv weight=1 fail\_timeout=60s;
    }

So what does this mean? This is really actually quite simple, we define
an upstream set called **apachesyslogtv**, which contains, in this
example, a single server definition with a weight of 1 and a fail
timeout of 60 seconds. You would actually be able to add multiple server
definitions to this with different weights and fail timeouts. This is
used for load balancing.

::

    upstream apachesyslogtv {
        server apache1.syslog.tv weight=1 fail\_timeout=60s;
        server apache2.syslog.tv weight=1 fail\_timeout=60s;
    }

Server definition changes
~~~~~~~~~~~~~~~~~~~~~~~~~

There are quite a lot of changes that are made to the actual server
definition, I will go through these step-by-step to explain what has
changed and why it's changed.

::

    location / {
        root /path/to/site;
        proxy\_redirect off;
        proxy\_set\_header Host $host;
        proxy\_set\_header X-Real-IP $remote\_addr;
        proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;

        if ($http\_cookie ~\* "comment\_author\_\|wordpress\_(?!test\_cookie)\|wp-postpass\_") {
            set $do\_not\_cache 1;
        }

        proxy\_cache\_key "$scheme://$host$request\_uri $do\_not\_cache";
        proxy\_cache cache;
        proxy\_cache\_valid 200 302 60m;
        proxy\_cache\_valid 404 1m;
        proxy\_pass http://apachesyslogtv;
    }

Ok, so that's the first location, definition. Several things have
changed with this.

The first change is an addition of a cookie check, in my case I'm
running a WordPress site so I check for various WordPress cookies, if
they exist I set the variable **$do\_not\_cache** to 1.

Next is a change to the proxy\_cache\_key to incorporate the
$do\_not\_cache variable, this tells nginx not to cache the current
page.

And finally is a change to proxy\_pass, this now points to the name of
my upstream definition, which nginx will then use to decide which server
to use.

::

    location ~\* .(jpg\|png\|gif\|jpeg\|css\|mp3\|wav\|swf\|mov\|doc\|pdf\|xls\|ppt\|docx\|pptx\|xlsx)$ {
        proxy\_cache\_valid 200 120m;
        expires 604800;
        proxy\_pass http://apachesyslogtv;
        proxy\_cache cache;
    }

The second and final location definition, which will match a file
extension in the URL, if a match is found it will set the cache validity
to 2 hours, expire to 7 days, pass back to our upstream definition and
cache the result. You may notice that out of all of these static file
extensions .js is missing, this is because a lot of my site is generated
by Javascript/Ajax and this will not work with caching.

Why the changes?
----------------

With these changes I am able to properly store with a cache key which
allows me to cache all of my nginx sites, I've added the ability to
balance load across multiple servers and I've increased the power of the
caching to only cache pages if you're not logged in and to always cache
static files for a long time. Meaning that the cache shouldn't need to
be regenerated very often.

All in all these changes do not increase the power of the server at all,
but with a load balanced environment this would obviously increase the
performance dramatically.

The full config
---------------

::

    upstream apachesyslogtv {
        server apache.syslog.tv weight=1 fail\_timeout=60s;
    }

    server {
        listen 174.143.241.61:80;
        server\_name syslog.tv;
        access\_log /var/log/nginx/syslog.tv.access.log;
        gzip\_vary on;
        gzip\_static on;

        location / {
            root /path/to/site;
            proxy\_redirect off;
            proxy\_set\_header Host $host;
            proxy\_set\_header X-Real-IP $remote\_addr;
            proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;

            if ($http\_cookie ~\* "comment\_author\_\|wordpress\_(?!test\_cookie)\|wp-postpass\_") {
                set $do\_not\_cache 1;
            }

            proxy\_cache\_key "$scheme://$host$request\_uri $do\_not\_cache";
            proxy\_cache cache;
            proxy\_cache\_valid 200 302 60m;
            proxy\_cache\_valid 404 1m;
            proxy\_pass http://apachesyslogtv;
        }

        location ~\* .(jpg\|png\|gif\|jpeg\|css\|mp3\|wav\|swf\|mov\|doc\|pdf\|xls\|ppt\|docx\|pptx\|xlsx)$ {
            proxy\_cache\_valid 200 120m;
            expires 604800;
            proxy\_pass http://apachesyslogtv;
            proxy\_cache cache;
        }

    }
