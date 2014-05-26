Using nginx, Varnish and Apache
###############################
:date: 2010-02-06 10:36
:author: kura
:category: tutorials
:tags: apache, cache, nginx, varnish
:slug: using-nginx-varnish-and-apache

.. contents::

The problem
-----------

So lets get to the problem first. I have several lightly to medium
loaded sites running on some virtual servers, they servers themselves
are highly configured to run beautifully on our host environments, very,
very RAM intensive but low disk I/O and low CPU usage.

As mentioned, the sites are relatively low loaded, they'll generally
hang around at between 3,000-5,000 unique hits a day and are run through
Apache using PHP, various PHP modules and MySQL, a simple generic LAMP
environment, yet customised to suit it's surroundings and host.

The sites themselves run fine on that setup, no issues at all on normal
days, but on set days of the week these sites can double in unique hits
or even more than double, with KeepAlive enabled and a KeepAliveTimeout
set low Apache has problems handling this kind of load (I should point
out that Apache only starts to struggle if there are a lot of concurrent
requests or if there's a lot of SSL activity).

We're serving a lot of static content with each request, at least half a
dozen CSS files and half a dozen JS files, literally dozens of images
and this will increase depending on the pages you're viewing and to top
it all off, an entire subset of pages that use SSL with obviously all
assets being run through SSL too.

So now we have a problem, even with double the average load on a single
server with all those assets we're greatly increasing the strain on
Apache, Apache can handle it but the server isn't very happy so I have
to make a decision, do I load balance Apache or do I set up a way of
serving static content through an HTTPD that is designed for it?

The first solution
------------------

The choice was simple, we serve static content through nginx, much like
I do with this blog but even more restrictive since this whole blog is
cached.

This is relatively easy and is covered in other blog post that should be
linked in the "related posts" section below, I successfully configured
nginx to reverse proxy connections back to when the content was non
static, i.e. PHP.

This in itself yielded a much higher rate of requests/second because
nginx was doing a lot of the grunt work, not content with this though I
wanted to actually cache the dynamic pages that were hit the most. This
was the homepage, various offer pages and some other site-specific
pages.

The second solution
-------------------

The next step of this, as mentioned above is to get some caching in
place, I've had experience caching proxy requests using nginx, as
mentioned above this blog uses the same configuration but is very less
restrictive, it literally caches everything except my admin pages. This
is not at all viable on these websites due to dynamic user content etc.

So the next step was to introduce conditional nginx caching.

I was rather unsure of exactly how to achieve this but the nginx forums
yielded amazingly useful information (`http://forum.nginx.org/`_) which
helped me create a very simple caching mechanism; a user hits the
website, all content is served by nginx which reverse proxies dynamic
content to Apache, the page content is cached when a user does not have
a login session cookie and any other requests to this page will serve
the cached version which dies after 1 hour, when a user does have a
login session cookie nginx does not serve the cached content but
continues to reverse proxy to Apache. Simple.

.. _`http://forum.nginx.org/`: http://forum.nginx.org/

This in itself is still untested on the testing environment because I
only completed it at 2am GMT and was rather tired at the time. I have
high hopes for it though, but it doesn't stop there...

The final phase
---------------

The final phase is still on my planning board and is probably overkill
for what we need, but it doesn't hurt to test things and the techie in
me is desperate to waste more of my free time on squeezing as much
performance out of our applications as I can. And, to be perfectly
honest, we may need something like this in the future for some much
higher traffic sites or to port older, high traffic sites on to.

So what's the plan? **Varnish**. Not the kind you use on wood or on your
nails but a very powerful HTTP caching engine -
`http://varnish-cache.org/wiki/Introduction`_

.. _`http://varnish-cache.org/wiki/Introduction`: http://varnish-cache.org/wiki/Introduction

Varnish is currently used in conjunction with nginx on some very highly
used sites; WordPress.com, Gravatar and I'm sure many more.

The idea is simple, a visitor will come to the site, nginx will do one
of two things which are outlined above but I will go through them again;
all static content will be served with nginx but directly from the
varnish cache, if a visitor has no login session cookie then nginx will
serve the page cache from Varnish, if a user does have a login session
cookie Varnish will proxy the request back to Apache. It's a sort of
double reverse proxy setup and I can't wait to see it in action.

I will report back here once I have some more time to even get this
setup but I doubt it'll happen for a week or more, sadly.
