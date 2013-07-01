Logging Google Analytics cookies with nginx
###########################################
:date: 2011-06-05 20:41
:author: kura
:category: debian, howto, nginx, ubuntu
:tags: google analytics, logging, nginx
:slug: logging-google-analytics-cookies-with-nginx

I was recently tasked with adding Google tracking cookies to our nginx
logging for a couple of sites. It was so it could be pushed through a
log processor.

It turned out too be a little trickier than it would have been with
Apache, but the process itself is still quite simple.

Open up the server definition you wish to add it to and add a custom log
format like below:

    log\_format g-a '$remote\_addr - $remote\_user [$time\_local] ' '"$request" $status $body\_bytes\_sent ' '"$http\_referer" "$http\_user\_agent" ' '"\_\_utma=$cookie\_\_\_utma;\_\_utmb=$cookie\_\_\_utmb;\_\_utmc=$cookie\_\_\_utmc;\_\_utmv=$cookie\_\_\_utmv;\_\_utmz=$cookie\_umtz"';

This log format can then be added to your access log like below:

    access\_log /var/log/nginx/access.example.com.log g-a;

Reload nginx

    /etc/init.d/nginx reload

If all goes well, you should see Google Analytics appearing in your
access logs like below:

    1.1.1.1 - - [05/Jun/2011:20:35:50 +0100] "GET / HTTP/1.1" 200 368 "" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1" "\_\_utma=65957554.1846091937.1301339836.1306174686.1306258917.5;\_\_utmb=-;\_\_utmc=-;\_\_utmv=-;\_\_utmz=-"
