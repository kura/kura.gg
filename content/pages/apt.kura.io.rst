apt.kura.io
###########
:date: 2014-01-26 02:05
:author: kura
:tags: apt
:slug: apt.kura.io

After releasing my own versions of haproxy with SPDY support and nginx with
ngx_pagespeed and SPDY support, I decided it would make sense to actually
host these in my own apt repository, so I did.

Support distros and versions
============================

The packages are built on Debian 7 (Wheezy) AMD 64 and are designed to work on
the following versions but should work on any newer version.

Debian
------

- 7 (Wheezy)

Ubuntu
------

- 12.04 (Precise)

Enabling
========

You can enable this by adding it to your apt config.

.. code:: bash

    wget -qO - https://apt.kura.io/apt.kura.io.key | sudo apt-key add -
    echo "deb https://apt.kura.io/ `lsb_release -cs` main" | sudo tee /etc/apt/sources.list.d/apt.kura.io.list
    sudo apt-get update

By default this repository is run over SSL, to use the non-SSL version you will
simply need to substitute https for http above.