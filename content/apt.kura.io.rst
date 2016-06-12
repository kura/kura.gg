apt.kura.io
###########
:date: 2014-01-26 02:05
:author: kura
:category: deb builds
:tags: apt
:slug: apt.kura.io

After releasing my own versions of haproxy with SPDY support and nginx with
ngx_pagespeed and SPDY support, I decided it would make sense to actually
host these in my own apt repository, so I did.

You can enable this by adding it to your apt config.

.. code-block:: bash

    wget -qO - http://apt.kura.io/apt.kura.io.key | sudo apt-key add -
    echo "deb http://apt.kura.io/ `lsb_release -cs` main" | sudo tee /etc/apt/sources.list.d/apt.kura.io.list
    sudo apt-get update

Simple.
