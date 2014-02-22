nginx 1.5.10 with SPDY 3.1
##########################
:date: 2014-02-06 03:30
:author: kura
:category: deb builds
:tags: debian, ubuntu, nginx, spdy, pagespeed, ngx_pagespeed
:slug: nnginx-1.5.10-with-spdy3.1

.. contents::

I have built and released nginx 1.5.10 with SPDY 3.1. Like the `nginx 1.5.9
release <https://kura.io/2014/02/02/nginx-1.5.9-and-ngx_pagespeed-1.7.30.3-beta/>`__
, this release comes with ngx_pagespeed 1.7.30.3-beta and is available
on `apt.kura.io <http://apt.kura.io>`__ or as downloads below.

Manual download
===============

+-------------------------------------------------------------------------------------------------+
| `nginx_1.5.10_all.deb <https://kura.io/files/nginx_1.5.10_all.deb>`__                           |
+-------------------------------------------------------------------------------------------------+
| `nginx-common_1.5.10_all.deb <https://kura.io/files/nginx-common_1.5.10_all.deb>`__             |
+-------------------------------------------------------------------------------------------------+
| `nginx-doc_1.5.10_all.deb <https://kura.io/files/nginx-doc_1.5.10_all.deb>`__                   |
+-------------------------------------------------------------------------------------------------+
| `nginx-light_1.5.10_amd64.deb <https://kura.io/files/nginx-light_1.5.10_amd64.deb>`__           |
+-------------------------------------------------------------------------------------------------+
| `nginx-full_1.5.10_amd64.deb <https://kura.io/files/nginx-full_1.5.10_amd64.deb>`__             |
+-------------------------------------------------------------------------------------------------+
| `nginx-extras_1.5.10_amd64.deb <https://kura.io/files/nginx-extras_1.5.10_amd64.deb>`__         |
+-------------------------------------------------------------------------------------------------+
| `nginx-naxsi_1.5.10_amd64.deb <https://kura.io/files/nginx-naxsi_1.5.10_amd64.deb>`__           |
+-------------------------------------------------------------------------------------------------+
| `nginx-naxsi-ui_1.5.10_all.deb <https://kura.io/files/nginx-naxsi-ui_1.5.10_all.deb>`__         |
+-------------------------------------------------------------------------------------------------+
| `nginx-light-dbg_1.5.10_amd64.deb <https://kura.io/files/nginx-light-dbg_1.5.10_amd64.deb>`__   |
+-------------------------------------------------------------------------------------------------+
| `nginx-full-dbg_1.5.10_amd64.deb <https://kura.io/files/nginx-full-dbg_1.5.10_amd64.deb>`__     |
+-------------------------------------------------------------------------------------------------+
| `nginx-extras-dbg_1.5.10_amd64.deb <https://kura.io/files/nginx-extras-dbg_1.5.10_amd64.deb>`__ |
+-------------------------------------------------------------------------------------------------+
| `nginx-naxsi-dbg_1.5.10_amd64.deb <https://kura.io/files/nginx-naxsi-dbg_1.5.10_amd64.deb>`__   |
+-------------------------------------------------------------------------------------------------+

MD5
===

.. code::

    9fe2e5273cc195161268f7d85261c4e2  nginx_1.5.10_all.deb
    edc55aa4866036eade02cd49957a9126  nginx-common_1.5.10_all.deb
    0361cdb3d00ac6e65c5e9d6167ba0d36  nginx-doc_1.5.10_all.deb
    833264c08fc6212f55ae37c26bd5cbc5  nginx-light_1.5.10_amd64.deb
    c5c1ffa0dd93673ac4a859a11d1b3b50  nginx-full_1.5.10_amd64.deb
    245d7628f143a6116ceb30c707264737  nginx-extras_1.5.10_amd64.deb
    dc404a346db86006672b5a6f8b016402  nginx-naxsi_1.5.10_amd64.deb
    ad3b7cf166752c2a8017bba8f6810496  nginx-naxsi-ui_1.5.10_all.deb
    cdb47100b4fef09bb8a8e414cd48554e  nginx-light-dbg_1.5.10_amd64.deb
    1ee2067aef2e1fcbc559dfdf9b8269ad  nginx-full-dbg_1.5.10_amd64.deb
    9f528d80802dd6a78d85b8558e65f650  nginx-extras-dbg_1.5.10_amd64.deb
    324dbf6afdff615d7c2bbe367f73bd1f  nginx-naxsi-dbg_1.5.10_amd64.deb


SHA1
====

.. code::

    7d66910ba00a49d04f8f00bd82470f8c9fbcb99f  nginx_1.5.10_all.deb
    6ce87bbcd1f87bc10bf75db5dc54470987bc6074  nginx-common_1.5.10_all.deb
    e18587fa5ce6638105455c1ef2b761cde848b9cf  nginx-doc_1.5.10_all.deb
    4add8919e34e3c95375d41fd2d14a07aad983f4e  nginx-light_1.5.10_amd64.deb
    87cfa2171f47e662c95599011500c9aa9ef26b2e  nginx-full_1.5.10_amd64.deb
    153f77b5d21b396f603bbd8486641b3d7fcde8a8  nginx-extras_1.5.10_amd64.deb
    5392e0dd57df0475d028766aceda7630d486a23f  nginx-naxsi_1.5.10_amd64.deb
    a294cbe57021eed9ddcd2e921a6e2644f601bd77  nginx-naxsi-ui_1.5.10_all.deb
    b61ace4af4be8bef7210e5bbf4b69410b7bca010  nginx-light-dbg_1.5.10_amd64.deb
    b334bb1e57d3920f68e2dd37399156281105eefb  nginx-full-dbg_1.5.10_amd64.deb
    05bac4c8bbb913ca0e3bdb11b2a82befe84198c4  nginx-extras-dbg_1.5.10_amd64.deb
    97b51fc8e05be3ba00e8daf11050d4bde67d5824  nginx-naxsi-dbg_1.5.10_amd64.deb
