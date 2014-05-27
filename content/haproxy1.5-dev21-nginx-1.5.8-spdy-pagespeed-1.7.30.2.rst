haproxy1.5-dev21, nginx 1.5.8, SPDY & pagespeed 1.7.30.2
########################################################
:date: 2014-01-08 13:00
:author: kura
:category: deb builds
:tags: debian, ubuntu, haproxy, nginx, spdy, pagespeed, ngx_pagespeed
:slug: haproxy1.5-dev21-nginx-1.5.8-spdy-pagespeed-1.7.30.2

.. contents::
    :backlinks: none

I have previously released `haproxy1.5-dev19 with SSL & SPDY support enabled
<https://kura.io/2013/07/15/haproxy-nginx-and-spdy-with-ssl-termination-debian-7/>`__
and `nginx 1.4.1 with SPDY support and pagespeed
<https://kura.io/2013/07/10/nginx-spdy-and-ngx-pagespeed/>`__, although I do
not remember which version of pagespeed.

I have received a few messages asking me for the latest version of haproxy,
nginx and pagespeed so I decided to finally build and release them.

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

haproxy
=======

This haproxy build is compiled against openssl, providing the npn module,
allowing for haproxy to work under SSL/TLS and allowing the use of SPDY/2 and
SPDY/3.

+-------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------------+
| `haproxy_1.5-dev21_amd64.deb <https://kura.io/files/haproxy_1.5-dev21_amd64.deb>`__ | `GPG <https://kura.io/files/haproxy_1.5-dev21_amd64.deb.asc>`__ | `MD5 <https://kura.io/files/haproxy_1.5-dev21_amd64.deb.md5>`__ | `SHA1 <https://kura.io/files/haproxy_1.5-dev21_amd64.deb.sha1>`__ |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------------+

Source
------

+-------------------------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------+
| `haproxy-1.5-dev21.tar.gz <https://kura.io/files/haproxy-1.5-dev21.tar.gz>`__ | `GPG <https://kura.io/files/haproxy-1.5-dev21.tar.gz.asc>`__ | `MD5 <https://kura.io/files/haproxy-1.5-dev21.tar.gz.md5>`__ | `SHA1 <https://kura.io/files/haproxy-1.5-dev21.tar.gz.sha1>`__ |
+-------------------------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------+

nginx
=====

All of these builds are compiled with the SPDY module and ngx_pagespeed modules
enabled. The version of pagespeed used is 1.7.30.2.

Sadly nginx 1.5.8 currently only supports SPDY/2, SPDY/3 support is still
unfinished.

Light/Full
----------

You will need to choose one of the two below, if in doubt, just use full.

+-------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------------+
| `nginx-full_1.5.8_amd64.deb <https://kura.io/files/nginx-full_1.5.8_amd64.deb>`__   | `GPG <https://kura.io/files/nginx-full_1.5.8_amd64.deb.asc>`__  | `MD5 <https://kura.io/files/nginx-full_1.5.8_amd64.deb.md5>`__  | `SHA1 <https://kura.io/files/nginx-full_1.5.8_amd64.deb.sha1>`__  |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------------+
| `nginx-light_1.5.8_amd64.deb <https://kura.io/files/nginx-light_1.5.8_amd64.deb>`__ | `GPG <https://kura.io/files/nginx-light_1.5.8_amd64.deb.asc>`__ | `MD5 <https://kura.io/files/nginx-light_1.5.8_amd64.deb.md5>`__ | `SHA1 <https://kura.io/files/nginx-light_1.5.8_amd64.deb.sha1>`__ |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------------+

Meta/Common/Doc
----------------

All three of these are required.

+-----------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------+
| `nginx_1.5.8_all.deb <https://kura.io/files/nginx_1.5.8_all.deb>`__               | `GPG <https://kura.io/files/nginx_1.5.8_all.deb.asc>`__        | `MD5 <https://kura.io/files/nginx_1.5.8_all.deb.md5>`__        |  `SHA1 <https://kura.io/files/nginx_1.5.8_all.deb.sha1>`__       |
+-----------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------+
| `nginx-common_1.5.8_all.deb <https://kura.io/files/nginx-common_1.5.8_all.deb>`__ | `GPG <https://kura.io/files/nginx-common_1.5.8_all.deb.asc>`__ | `MD5 <https://kura.io/files/nginx-common_1.5.8_all.deb.md5>`__ | `SHA1 <https://kura.io/files/nginx-common_1.5.8_all.deb.sha1>`__ |
+-----------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------+
| `nginx-doc_1.5.8_all.deb <https://kura.io/files/nginx-doc_1.5.8_all.deb>`__       | `GPG <https://kura.io/files/nginx-doc_1.5.8_all.deb.asc>`__    | `MD5 <https://kura.io/files/nginx-doc_1.5.8_all.deb.md5>`__    | `SHA1 <https://kura.io/files/nginx-doc_1.5.8_all.deb.sha1>`__    |
+-----------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------+

Extras
------

I'd only recommend installing this if you know what optional extras are
installed with this package.

+---------------------------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+
| `nginx-extras_1.5.8_amd64.deb <https://kura.io/files/nginx-extras_1.5.8_amd64.deb>`__ | `GPG <https://kura.io/files/nginx-extras_1.5.8_amd64.deb.asc>`__ | `MD5 <https://kura.io/files/nginx-extras_1.5.8_amd64.deb.md5>`__ | `SHA1 <https://kura.io/files/nginx-extras_1.5.8_amd64.deb.sha1>`__ |
+---------------------------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+

Naxsi
-----

The Naxsi WAF.

+---------------------------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+
| `nginx-naxsi_1.5.8_amd64.deb <https://kura.io/files/nginx-naxsi_1.5.8_amd64.deb>`__   | `GPG <https://kura.io/files/nginx-naxsi_1.5.8_amd64.deb.asc>`__  | `MD5 <https://kura.io/files/nginx-naxsi_1.5.8_amd64.deb.md5>`__  | `SHA1 <https://kura.io/files/nginx-naxsi_1.5.8_amd64.deb.sha1>`__  |
+---------------------------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+
| `nginx-naxsi-ui_1.5.8_all.deb <https://kura.io/files/nginx-naxsi-ui_1.5.8_all.deb>`__ | `GPG <https://kura.io/files/nginx-naxsi-ui_1.5.8_all.deb.asc>`__ | `MD5 <https://kura.io/files/nginx-naxsi-ui_1.5.8_all.deb.md5>`__ | `SHA1 <https://kura.io/files/nginx-naxsi-ui_1.5.8_all.deb.sha1>`__ |
+---------------------------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+

Debug symbols
-------------

+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `nginx-full-dbg_1.5.8_amd64.deb <https://kura.io/files/nginx-full-dbg_1.5.8_amd64.deb>`__     | `GPG <https://kura.io/files/nginx-full-dbg_1.5.8_amd64.deb.asc>`__    | `MD5 <https://kura.io/files/nginx-full-dbg_1.5.8_amd64.deb.md5>`__   | `SHA1 <https://kura.io/files/nginx-full-dbg_1.5.8_amd64.deb.sha1>`__   |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `nginx-light-dbg_1.5.8_amd64.deb <https://kura.io/files/nginx-light-dbg_1.5.8_amd64.deb>`__   | `GPG <https://kura.io/files/nginx-light-dbg_1.5.8_amd64.deb.asc>`__   | `MD5 <https://kura.io/files/nginx-light-dbg_1.5.8_amd64.deb.md5>`__  | `SHA1 <https://kura.io/files/nginx-light-dbg_1.5.8_amd64.deb.sha1>`__  |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `nginx-extras-dbg_1.5.8_amd64.deb <https://kura.io/files/nginx-extras-dbg_1.5.8_amd64.deb>`__ | `GPG <https://kura.io/files/nginx-extras-dbg_1.5.8_amd64.deb.asc>`__  | `MD5 <https://kura.io/files/nginx-extras-dbg_1.5.8_amd64.deb.md5>`__ | `SHA1 <https://kura.io/files/nginx-extras-dbg_1.5.8_amd64.deb.sha1>`__ |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `nginx-naxsi-dbg_1.5.8_amd64.deb <https://kura.io/files/nginx-naxsi-dbg_1.5.8_amd64.deb>`__   | `GPG <https://kura.io/files/nginx-naxsi-dbg_1.5.8_amd64.deb.asc>`__   | `MD5 <https://kura.io/files/nginx-naxsi-dbg_1.5.8_amd64.deb.md5>`__  | `SHA1 <https://kura.io/files/nginx-naxsi-dbg_1.5.8_amd64.deb.sha1>`__  |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------+------------------------------------------------------------------------+

Source
~~~~~~

+-------------------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------+
| `nginx-1.5.8.tar.gz <https://kura.io/files/nginx-1.5.8.tar.gz>`__ | `GPG <https://kura.io/files/nginx-1.5.8.tar.gz.asc>`__ | `MD5 <https://kura.io/files/nginx-1.5.8.tar.gz.md5>`__ | `SHA1 <https://kura.io/files/nginx-1.5.8.tar.gz.sha1>`__ |
+-------------------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------+
