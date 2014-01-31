Debian, Apache 2, Nginx, WordPress MU & WP-Super-Cache
######################################################
:date: 2010-01-11 19:58
:author: kura
:category: tutorials
:tags: apache, cache, debian, nginx, wordpress
:slug: debian-apache-2-nginx-wordpress-mu

.. contents::

*This is a rather old article, for more up-to-date information please
see;*

1. `https://kura.io/2010/02/07/nginx-proxy_cache-and-explained-benchmarked/`_
2. `https://kura.io/2010/02/14/more-nginx-proxy_cache-optimizations-and-nginx-load-balancing/`_

.. _`https://kura.io/2010/02/07/nginx-proxy_cache-and-explained-benchmarked/`: https://kura.io/2010/02/07/nginx-proxy_cache-and-explained-benchmarked/
.. _`https://kura.io/2010/02/14/more-nginx-proxy_cache-optimizations-and-nginx-load-balancing/`: https://kura.io/2010/02/14/more-nginx-proxy_cache-optimizations-and-nginx-load-balancing/

I've started collecting a few blogs on my servers now and figured from
this one on I would consolidate it in to one workable, usable location.
Removing my need to update multiple plugins, themes and WordPress
itself, over and over.

This time round I thought I'd do it properly, and properly in my book is
as complicated and "awesome" as it can possibly be, without growing legs
and running off to stomp a city.

Love
----

I've fallen in-love with nginx (`http://nginx.org/`_) over the last 6
months or so, I'd been an avid user of LighTTPD for a very long time
before but started to look in to nginx mid year as a replacement. I
learned that at my new job they used nginx for image server and, after
reading a few articles online decided nginx greatly outweighed "Lighty".

.. _`http://nginx.org/`: http://nginx.org/

First stop was getting Wordpress MU installed, this itself proved rather
interesting, I've no idea why however. After several failed attempts
(the first showing me pages without images or css, the second
redirecting to nowhere and so on,) I finally got it working. On logging
in I realised how horrid it was, forcing you to set-up weird sub domain
structures that the blogs are *supposed* to work under. This is all well
and good but I don't have blogs running on sub domains, I have blogs
running on their own domains. Ignoring this "feature" you can actually
force set each blog to have it's own url, but this has to be during
editing after initial creation.

The rest was the usual WordPress ease, wget the plugins and themes I
wanted, unzip them as usual and stick them in the right locations,
removing unwanted readme.txt files just to keep the whole place clean.
On a side note; what happened to the "README" files of the past? Why are
they all starting to appear named as "readme.txt" now? I guess the
Windows crowd couldn't figure out how to open them in Notepad...

Hurdles
-------

My first stumble was when I couldn't use my beloved sitemaps plugin I've
used so many times, the problem with it is it stores the files directly
in the doc root, which is fine on a single instance, but with multiple
blogs they just overwrite each other. Luckily I found a nice little
WordPress MU specific one that slotted in nicely, it appears to be
generated each and every time the file is hit, so I wrote a quick script
that uses wget to grab each blogs sitemap every 6 hours, saves them to
the content directory and uses .htaccess to point to the right one.

With that dragon vanquished it was time to get WP-Super-Cache installed,
this proved painless as usual and was running under Apache 2 in no time
at all, I've yet to work out why every time I install it under Apache,
Apache seems go insane, eventually slowing everything down to a crawl...
But that leads me on to the next part.

Nginx reverse proxy to Apache.

This wasn't difficult at all, I've reverse proxied connections to Apache
many times from nginx now, being a Debian user made it quite nice a
simple, I have Apache 2 running bound to 1 IP and nginx bound to
another, I simply created a new vhost for nginx and filled it with the
lovely data needed as shown below.

.. code:: nginx

    server {
        listen 174.143.241.61:80;
        server_name syslog.tv;
        access_log /var/log/nginx/syslog.tv.access.log;

        location / {
            proxy_pass http://apache.syslog.tv;
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            client_max_body_size 10m;
            client_body_buffer_size 128k;
            proxy_connect_timeout 90;
            proxy_send_timeout 90;
            proxy_read_timeout 90;
            proxy_buffer_size 4k;
            proxy_buffers 4 32k;
            proxy_busy_buffers_size 64k;
            proxy_temp_file_write_size 64k;
        }

        location ~* ^.+.(jpg|jpeg|gif|png|ico|css|zip|tgz|gz|rar|bz2|doc|xls|exe|pdf|ppt|txt|tar|mid|midi|wav|bmp|rtf|js)$ {
            root /path/to/wordpress;
        }

        if (-f $request_filename) {
            break;
        }

        if (-d $request_filename) {
            break;
        }

        set $supercache_file .;
        set $supercache_uri $request_uri;

        if ($request_method = POST) {
            set $supercache_uri .;
        }

        if ($query_string) {
            set $supercache_uri .;
        }

        if ($http_cookie ~* .comment_author_|wordpress|wp-postpass_.) {
            set $supercache_uri .;
        }

        if ($supercache_uri ~ ^(.+)$) {
            set $supercache_file /wp-content/cache/supercache/$http_host/$1index.html;
        }

        if (-f $document_root$supercache_file) {
            rewrite ^(.*)$ $supercache_file break;
        }

    }

As you can see, this is rather simple, I patched it together from some
articles already out there on Google, made a couple of changes where
required. The main thing here is that we turn "proxy_redirect" off, and
you may also notice I am pointing at apache.syslog.tv, this domain
doesn't exist, I just created an instance of it pointing to Apache's
local IP in /etc/hosts.

More hurdles
------------

I ran in to some initial problems with this though, sadly. Problems I
was unable to really find a solution to for some time. The first problem
was speed, or lack of it in fact. Apache was quite literally dying on
me, a restart of Apache temporarily solved this problem, in the process
I also restarted nginx, this was probably a bad idea. I'd been tinkering
with the nginx config, setting gzip vars and other things, this caused
serious problems and made nginx throw 301 redirects for every single
http request, Apache also threw 301 redirects just to complete the cycle
of infinite loop. Needless to say I maxed out memory in no time.

I reverted my changes and then found that the caching seemed to be
playing up now, eventually I noticed that this was actually due to my
.htaccess having the supercache data at the bottom of the file, instead
of the top. Fixed.

Again came the speed problems, I noticed that when I used Ctrl+F5
instead of just F5 or opened the site in Firefox instead of Chrome I was
getting the same slow speed problems. While trying to watch my logs go
speeding by I found some very interesting messages. The first was from
mod_spamhaus which claimed my IP address was blacklisted, I ran to
their website and did a lookup, thankfully it seems to only be a local
blacklist, against my better judgement I disable mod_spamhaus for the
time being. The other issue was coming from mod_evasive, a few quick
config changes for it to handle lots of proxied requests from nginx when
the cache was old or not there.

And that solved it, solved excluding mod_spamhaus. Now I need to either
find a solution or weigh the pros and cons of mod_spamhaus.
