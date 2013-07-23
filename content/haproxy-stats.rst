haproxy stats
#############
:date: 2013-07-19 13:00
:author: kura
:category: tutorials
:tags: haproxy, stats
:slug: haproxy-stats

I recently wrote an article on `using haproxy, SSL and
SPDY with nginx backend servers
<https://kura.io/2013/07/15/haproxy-nginx-and-spdy-with-ssl-termination-debian-7/>`_.

This article is a little extra on top of that to explain
how to enable statistics for haproxy so you can monitor
the backend statuses etc.

Example stats page
------------------

.. image:: https://kura.io/static/images/haproxy-stats.png
   :alt: Moar stats!

Enabling stats
--------------

::

    listen stats :8000
        mode http
        stats enable
        stats hide-version
        stats realm haproxy\ stats
        stats uri /
        stats auth admin:admin

Place the above content in the haproxy configuration
file (*/etc/haproxy/haproxy.cfg*).

Be sure to replace *admin:admin* with your a proper
username and password, username first, password
after the colon.

Restart haproxy, and then browse to `http://yousite.com:8000
<http://yoursite.com:8000>`_.

