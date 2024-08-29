haproxy1.5-dev22
################
:date: 2014-02-22 05:32
:author: kura
:category: deb builds
:tags: debian, ubuntu, haproxy, spdy, ssl
:slug: haproxy1.5-dev22

.. contents::
    :backlinks: none

Requirements
============

haproxy requires openssl-1.0.1d or higher.

On a standard Debian 7 install you should have openssl-1.0.1e-2, you
can find which version you have by running

.. code-block:: none bash

    dpkg -l openssl

This should return something similar to

::

    ii  openssl        1.0.1e-2        amd64        Secure Socket Layer (SSL) binary and related cryptographic tools

Build notes
===========

Builds were done on Debian 7 AMD64, I will not be providing 32bit versions as
this is mainly for my own usage and amusement.

This haproxy build is compiled against openssl, providing the npn module,
allowing for haproxy to work under SSL/TLS and allowing the use of SPDY/2 and
SPDY/3.

This version is available on `apt.kura.gg </apt.kura.gg/>`__
or as a manual download, from the link below.

Manual download
===============

+----------------------------------------------------------------------+
| `haproxy_1.5-dev22_amd64.deb </files/haproxy_1.5-dev22_amd64.deb>`__ |
+----------------------------------------------------------------------+

MD5
===

.. code-block:: none

    1d258aaf1592ac5d6cb34e495e283591  haproxy_1.5-dev22_amd64.deb

SHA1
====

.. code-block:: none

    f17cb661d2ceb1686a0a4b8566168503a0d372d9  haproxy_1.5-dev22_amd64.deb
