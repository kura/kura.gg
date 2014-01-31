Advertise multiple NPN protocols with haproxy
#############################################
:date: 2014-01-31 15:25
:author: kura
:category: tutorials
:tags: haproxy, npn, spdy, http/1.1, http/1.0
:slug: advertise-multiple-npn-protocols-with-haproxy

I have previously written an article on `using SPDY with haproxy
<https://kura.io/2013/07/15/haproxy-nginx-and-spdy-with-ssl-termination-debian-7/>`__
but have been spending some time recently being annoyed that the `SPDY check
tool <http://spdycheck.org/#kura.io>`__ said I didn't advertise a fall back to
HTTP over SSL in the NPN protocol list.

After some digging I discovered it was actually quite simple to advertise
multiple protocols using npn and haproxy.

Previously my article called for using the following section of configuration
at the end of the bind line.

.. code::

    npn spdy/2

To advertise HTTP protocols as well as SPDY you simply need to add them to the
npn list, using commas as a delimiter.

.. code::

    npn spdy/2,http/1.1,http/1.0
