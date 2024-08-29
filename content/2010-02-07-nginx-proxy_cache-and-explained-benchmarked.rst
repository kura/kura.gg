nginx, proxy_cache and reverse proxying explained & benchmarked
###############################################################
:date: 2010-02-07 10:27
:author: kura
:category: tutorials
:tags: apache, cache, debian, howto, nginx, php, ubuntu, wordpress
:slug: nginx-proxy_cache-and-explained-benchmarked

.. contents::
    :backlinks: none

The beginning
-------------

Where to begin? nginx would be a good start I suppose. It's far easier
and makes much for sense for you to actually read about nginx from it's
own website - `https://nginx.org/en/`_ - but just to give a simple
explanation too; \`nginx is king of static content HTTP servers.\`

.. _`https://nginx.org/en/`: https://nginx.org/en/

Anyone that has dealt with Apache on medium to high traffic websites
will know that Apache is bit of a \`wheezy, old geezer\` when it comes
to content serving using it's mpm-worker (threaded). Very often high
traffic will cause server load to go through the roof but for serving
dynamic content, there really is no better HTTP server than Apache, so
this leaves us in a bit of a predicament; a high powered website with
dynamic content and lots of static files like JS, CSS and imagery, what
do we do?!

In this example \`dynamic content\` means content that is drawn from the
SQL DB and used to generate pages using PHP; pages of products, category
trees, etc, a typical ecommerce platform.

I opted to use nginx to reverse proxy to Apache and serve up just the
static content through nginx itself long ago and, looking down through
the \`Related Posts\` section of this page you will find at least half a
dozen articles about it, including my original article on how to get
nginx to actually reverse proxy and use WP-Super-Cache to actually
generate cached HTML content that nginx could serve. This article takes
that further.

If you've not read the aforementioned article I would strongly suggest
you do before continuing with this one - `Debian, Apache 2, Nginx, WordPress MU & WP-Super-Cache`_.

.. _Debian, Apache 2, Nginx, WordPress MU & WP-Super-Cache: /2010/01/11/debian-apache-2-nginx-wordpress-mu/

Everything has changed?
-----------------------

So now that you've read that it's time to explain what's different and,
quite simply, everything is. Everything? Everything.

Gone are the location checks and file checks, all replaced with several
lines that tell nginx that it needs to cache the page content.

Before I get stuck in on the changes it's worth pointing out that this
is only possible with version of nginx >= 0.7.65 and within the 0.8.*
branch. According to the nginx website there was a bug in the proxy
caching engine that meant nginx would ignore comma separate cache
controls. So upgrade before attempting this.

Back to the changes, lets take a look at a small change I made to the
actual nginx main configuration file, on Debian/Ubuntu this is in

    /etc/nginx/nginx.conf

.. code-block:: nginx

    proxy_cache_path /var/www/syslog.tv/cache levels=1:2 keys_zone=one:8m max_size=1000m inactive=600m;
    proxy_temp_path /tmp;

These 2 lines need to be within the main nginx configuration before any
of your server {} definitions, otherwise nginx's config test will fail
and nginx won't start.

The biggest chain was in this site's server definition, it now looks
like this

.. code-block:: nginx

    server {
        listen 174.143.241.61:80;
        server_name syslog.tv;
        access_log /var/log/nginx/syslog.tv.access.log;

        location / {
            root /var/www/syslog.tv; #the path to your actual site, used for serving static files
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_cache one;
            proxy_cache_key syslog.tv$request_uri;
            proxy_cache_valid 200 302 60m;
            proxy_cache_valid 404 1m;
            proxy_pass https://apache.syslog.tv;
        }
    }

The server definition should be relatively easy to understand, we have
the general listen, server_name, access_log and root which are used
everywhere, the only difference now is that I am serving root from
/var/www/syslog.tv/cache which is where nginx is configured to store
it's cache.

We set several proxy specific options, proxy_redirect and three
proxy_set_header instances, these are really quite self explanatory;
do not redirect proxy requests, ever and the three headers are passed
over to Apache so it is able to properly log access and see the original
IP rather than seeing nginx's IP.

The new and important part is from proxy_cache down to proxy_pass,
proxy_pass exists in my original config file but here it is now used in
conjunction with proxy_cache, which sets the zone (zone definition are
in the two lines added to nginx.conf), set the key, sets some timers on
valid responses, in this case 200, 302 and 404 and then passed back to
Apache with proxy_pass.

So what does it do?
-------------------

I'm going to assume that you're with me so far if you're reading this,
I've not lost you or anything, I hope.

So what is the point of this? What does it do?

It's really quite simple; this tells nginx to cache all proxy responses
when they meet the response type requirements for the times defined,
that's it.

When nginx loads it will automatically look for a cached version
residing in our root directory before even thinking about reverse
proxying back to Apache, if it finds a cached variant that is still
valid it will serve it, if not it will proxy back to Apache which
generates our page content, which nginx serves and then caches. This
means that the load on Apache is greatly reduced and I mean **greatly**
reduced.

Controlling the cache
---------------------

The best thing about this setup is how you actually control what gets
cached. Headers. It's as simple as that.
These are basic HTTP Cache-Control headers:

    Cache-Control: private, max-age=0

The one above sets Cache-Control to private with a max-age of 0 and the
one below sets to public with a max age of one hour.

    Cache-Control: public, max-age=3600

nginx will respect these headers and handle the caching accordingly, you
can set these headers through PHP and have pages not get cached, you can
even use .htaccess to set the headers on specific directories, files or
file extensions or you could even just set them in your site's server
definition. Amazing stuff.

The numbers
-----------

::

    Benchmarking this setup actually scared me, I was completely amazed
    out how well nginx performed.
    Benchmarking syslog.tv (be patient)
    ...
    Finished 10000 requests

    Server Software: nginx/0.7.65
    Server Hostname: syslog.tv
    Server Port: 80
    ...
    Concurrency Level: 200
    Time taken for tests: 93.371 seconds
    Complete requests: 10000
    Failed requests: 0
    Write errors: 0
    Total transferred: 74634408 bytes
    HTML transferred: 72015948 bytes
    Requests per second: 107.10 [#/sec] (mean)
    Time per request: 1867.419 [ms] (mean)
    Time per request: 9.337 [ms] (mean, across all concurrent requests)
    Transfer rate: 780.60 [Kbytes/sec] received

    Connection Times (ms)
    min mean[+/-sd] median max
    Connect: 10 611 245.9 600 3640
    Processing: 70 1238 142.0 1250 5100
    Waiting: 70 611 100.5 600 4100
    Total: 80 1849 266.2 1860 6240

    Percentage of the requests served within a certain time (ms)
    50% 1860
    66% 1860
    75% 1860
    80% 1880
    90% 1880
    95% 1900
    98% 1920
    99% 2260
    100% 6240 (longest request)

That is very good, the server this website runs on is very underpowered,
256MB of RAM, single virtual core just in case anyone thinks I cheated
and used a 32 core machine.

What is also worth mentioning is the load average

    load average: 0.08, 0.06, 0.03

I'm hoping your eyes are as wide as mine were when I saw this average,
200 concurrent connections on nginx and the load average doesn't go
above 0.08 the whole time. It served 10,000 requests with 0 failures,
200 at a time in 93.371 seconds...

I tried the same with proxy_caching disable and also directly against
Apache, both times with a KeepAlive On and KeepAliveTimeOut 5 Apache
fell over, load went through the roof and I had to hard reset the server
both times. Apache couldn't even handle 50 concurrent requests, let
alone 200.

The conclusion
--------------

The conclusion is simple for me; I love nginx and will continue to use
it as much as I can to increase performance, this does not mean I have
any dislike for Apache at all, in fact I know very well that to do
things well in this field you need to have multiple systems in place to
handle multiple things, especially with high traffic sites.

For me the future is simple, cache as much content as I possibly can and
use nginx to serve it.

The next steps for me will be using Varnish for caching, nginx for load
balancing and also trying caching content to Memcached. As always
finding will be reported here.
