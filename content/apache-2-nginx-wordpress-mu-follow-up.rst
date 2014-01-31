Apache 2, Nginx & WordPress MU - Follow up
##########################################
:date: 2010-01-12 00:37
:author: kura
:category: tutorials
:tags: apache, cache, debian, nginx, wordpress
:slug: apache-2-nginx-wordpress-mu-follow-up

This is a quick follow up to a previous post about getting this blog
`running on nginx with a reverse proxy to Apache 2`_.

.. _running on nginx with a reverse proxy to Apache 2: https://kura.io/2010/01/11/debian-apache-2-nginx-wordpress-mu/

It seems the issue stems from 3 mods I had installed and enabled

1. mod-spamhaus
2. mod-evasive and
3. mod-security

The 3, when running together are a fantastic way to strengthen any web
server from attack, be it DOS, injection, XLS etc. I've sworn by all 3
of them for years now and I thought I had them cracked for
security:performance ratio, when it comes to reverse proxying requests
from nginx to Apache 2 where WordPress is concerned, apparently I was
very wrong.

The issue wasn't so bad when the cache was full, but seeing as my cache
is only alive for an hour that leaves an open point for the cache to be
recreated when a user views the page. This in itself isn't a bad thing
or even the root cause, the actual cause appears to be a huge amount of
requests hitting Apache, these in turn trigger all 3 mods, all for the
same reason; lots and lots of requests in short amounts of time from the
same IP address.

Somehow this was causing Apache to spawn many child processes which it
then tried to kill when the requests were completed or killed, this put
my server load to 15.02 at one point in time, causing the server to go
in to a frenzy as Apache tried to spawn even more children to handle the
requests, getting itself caught in a vicious looping cycle.

As it stands now I have lowered the tolerance of both mod-evasive and
mod-security which has massively improved performance to the point where
now I can clean and recreate the cache of all blogs running from this
WPMU installation at the same time, while browsing and never notice it.

Currently mod-spamhaus has been disabled until such time as I can figure
out it's configuration variables and get it running nicely without it
killing my server when the site in question is a WordPress site.

As a consequence my other non WPMU blogs that are running purely on
Apache with no nginx reverse proxy have also sped up dramatically which
is always a good thing. I guess for now I'll have to write a quick
Python script that temporarily bans people using iptables until I can
get all 3 mods working in harmony.

Will post in the future when I have more info.
