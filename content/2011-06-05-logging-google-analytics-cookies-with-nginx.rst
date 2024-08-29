Logging Google Analytics cookies with nginx
###########################################
:date: 2011-06-05 20:41
:author: kura
:category: tutorials
:tags: google analytics, logging, nginx
:slug: logging-google-analytics-cookies-with-nginx

I was recently tasked with adding Google tracking cookies to our nginx
logging for a couple of sites. It was so it could be pushed through a
log processor.

It turned out too be a little trickier than it would have been with
Apache, but the process itself is still quite simple.

Open up the server definition you wish to add it to and add a custom log
format like below

::

    log_format g-a '$remote_addr - $remote_user [$time_local] ' '"$request" $status $body_bytes_sent ' '"$http_referer" "$http_user_agent" ' '"__utma=$cookie___utma;__utmb=$cookie___utmb;__utmc=$cookie___utmc;__utmv=$cookie___utmv;__utmz=$cookie_umtz"';

This log format can then be added to your access log like below:

.. code-block:: nginx

    access_log /var/log/nginx/access.example.com.log g-a;

Reload nginx

.. code-block:: bash

    sudo /etc/init.d/nginx reload

If all goes well, you should see Google Analytics appearing in your
access logs like below

::

    1.1.1.1 - - [05/Jun/2011:20:35:50 +0100] "GET / HTTP/1.1" 200 368 "" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1" "__utma=65957554.1846091937.1301339836.1306174686.1306258917.5;__utmb=-;__utmc=-;__utmv=-;__utmz=-"
