haproxy stateful SSL session resumption
#######################################
:date: 2014-02-22 05:10
:author: kura
:category: tutorials
:tags: haproxy, ssl
:slug: haproxy-stateful-ssl-session-resumption

.. contents::
    :backlinks: none

By default haproxy enables stateless SSL session resumption, but you can enable
stateful session resumption in accordance with
`RFC 5077 <https://www.ietf.org/rfc/rfc5077.txt>`__. This functionality, like
the SSL handling it relies on is only available from haproxy 1.5.

Configuration
=============

The option to enable stateful SSL session resumption is as below

::

    no-tls-tickets

You will need to add it in to your bind line, like below

::

    bind 0.0.0.0:443 ssl ... no-tls-tickets
