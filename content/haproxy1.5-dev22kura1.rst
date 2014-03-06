haproxy1.5-dev22kura1
#####################
:date: 2014-03-06 03:32
:author: kura
:category: deb builds
:tags: debian, ubuntu, haproxy, spdy, ssl
:slug: haproxy1.5-dev22kura1

.. contents::

Changes
=======

This patched version is built using the `USE_ZLIB` option, allowing for usage
of compression or using haproxy as a compression offloader.

Requirements
============

haproxy requires openssl-1.0.1d or higher.

On a standard Debian 7 install you should have openssl-1.0.1e-2, you
can find which version you have by running

.. code:: bash

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

This version is available on `apt.kura.io <https://kura.io/apt.kura.io/>`__
or as a manual download, from the link below.

Manual download
===============

+-----------------------------------------------------------------------------------------------+
| `haproxy_1.5-dev22kura1_amd64.deb <https://kura.io/files/haproxy_1.5-dev22kura1_amd64.deb>`__ |
+-----------------------------------------------------------------------------------------------+

MD5
===

.. code::

    5b1fbc3121fdc4ecb6687acd0bf7d83a  haproxy_1.5-dev22kura1_amd64.deb

SHA1
====

.. code::

    9d87ddacde26b75f8c9d723093cf2ef51615ec6e  haproxy_1.5-dev22kura1_amd64.deb

