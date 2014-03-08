apt.kura.io
###########
:date: 2014-01-26 02:05
:author: kura
:tags: apt
:slug: apt.kura.io

.. contents::

After releasing my own versions of haproxy with SPDY support and nginx with
ngx_pagespeed and SPDY support, I decided it would make sense to actually
host these in my own apt repository, so I did.

Supported distros and versions
==============================

The packages are built on Debian 7 (Wheezy) AMD64 and i386 and are designed to
work on the following versions but should work on any newer version.

Supported
---------

Debian
~~~~~~

- 7 (Wheezy)

Ubuntu
~~~~~~

- 12.04 (Precise)

Unsupported but enabled
-----------------------

Ubuntu
~~~~~~

- 12.10 (Quantal)
- 13.04 (Raring)
- 13.10 (Saucy)
- 14.04 (Trusty)

Enabling
========

You can enable this by adding it to your apt config.

.. code:: bash

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D38F85FF650A63B9
    sudo wget https://apt.kura.io/`lsb_release -cs`.list -O /etc/apt/sources.list.d/apt.kura.io.list
    sudo apt-get update

By default this repository is run over SSL, to use the non-SSL version you will
simply need to substitute https for http above.
