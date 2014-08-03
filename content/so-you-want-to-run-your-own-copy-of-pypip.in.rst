So you want to run your own copy of pypip.in?
#############################################
:date: 2014-07-26 23:40
:author: kura
:category: coding
:tags: python, pypipins, pypip.in, shields
:slug: so-you-want-to-run-your-own-copy-of-pypip.in

.. contents::
    :backlinks: none

While pypip.in is available under the MIT license on `GitHub
<https://github.com/badges/pypipins>`_, it's not explained how to really use it
properly.

You can gather how to set-up the Python source of the project and get the
`Twisted <https://twistedmatrix.com>`_ process running, this is totally reliant
on using the `img.shields.io <https://img.shields.io>`_.

I decided to write this article explaining how to install your own copy of the
shields nodejs code, pypipin itself and even cover off supervisord and Varnish
too.

shields & nodejs
================

nodejs
------

First of all you'll need to get the latest source code copy of nodejs from the
`nodejs download page <http://nodejs.org/download/>`_.

Extract it.

.. code:: bash

    tar -xvzf node-<VERSION>.tar.gz

.. code:: bash

    cd node-<VERSION>

You'll need to install the build tools, if you don't have them already.

.. code:: bash

    sudo apt-get install build-essential

And then make and install node.

.. code:: bash

    make && sudo make install

shields
-------

You'll need to install git for the next step.

.. code:: bash

    sudo apt-get install git-core

And get a copy of the shields repository.

.. code:: bash

    git clone git@github.com:badges/shields.git

Once it's checked out, you'll need to install it's requirements.

.. code:: bash

    cd shields && npm install

You can confirm this works by running the shields server.

.. code:: bash

    node server 8080

pypipin
=======

Clone the shields repository, the same way you did for shields above.

.. code:: bash

    git clone git@github.com:badges/pypipins.git

To do this properly, you'll need to make sure you have virtualenv for Python.

.. code:: bash

    sudo apt-get install python-dev
    sudo wget -O - https://bootstrap.pypa.io/get-pip.py | python
    sudo pip install virtualenv

Next, you'll need to create a virtual environment.

.. code:: bash

    virtualenv /path/to/where/you/want/it/

Then you can active it.

.. code:: bash

    . /path/to/your/virtualenv/bin/activate

And install the dev requirements from the pypipins directory.

.. code:: bash

    pip install -r /path/to/pypipins/clone/requirements-dev.txt

You'll need to edit shields.py, commenting out the img.shields.io host and
uncommon the local one.

.. code:: python

    /path/to/pypipins/clone/shields/shields.py


    # SHIELD_URL = "http://img.shields.io/badge/%s-%s-%s.%s"
    SHIELD_URL = "http://localhost:9000/badge/%s-%s-%s.%s"  # pypip.in uses a local version of img.shields.io

Once this is done, you can test the pypipins server.

.. code:: bash

    /path/to/your/virtualenv/bin/python /path/to/pypipins/clone/shields/shields.py

supervisor(d)
=============

Always install supervisor from apt, rather than from pip.

.. code:: bash

    sudo apt-get install supervisor

Then cd to where conf.d config files are stored for supervisor.

.. code:: bash

    cd /etc/supervisor/conf.d/

In here, you'll need to create a configuration for the shields nodejs server
and also for pypipins server.

.. code::

    shields.conf


    [program:shields]
    directory=/path/to/shields/
    command=node server 9000
    stdout_logfile=/var/log/supervisor/shields.log
    stderr_logfile=/var/log/supervisor/shields.error.log
    autostart=true
    autorestart=true

.. code::

    pypipin.conf


    [program:pypipin]
    command=/path/to/virtualenv/bin/python /path/to/pypipin/clone/shields/shields.py
    stdout_logfile=/var/log/supervisor/pypipin.log
    stderr_logfile=/var/log/supervisor/pypipin.error.log
    autostart=true
    autorestart=true

Once this is done, you'll need to load them in to supervisor itself.

.. code:: bash

    sudo supervisorctl

.. code::

    reread
    add shields
    add pypipin

Now supervisor will automatically start both processes and keep them alive.

Varnish
=======

The final step is to put Varnish in front of the system to cache images for you.
The shields server has the ability to use redis for caching but, I'd rather do
this with a proper HTTP cache rather than use redis.

.. code:: bash

    sudo apt-get install varnish

Tell Varnish to run on port 80.

.. code::

    /etc/default/varnish


    DAEMON_OPTS="-a :80 \
                 -T localhost:6082 \
                 -f /etc/varnish/default.vcl \
                 -S /etc/varnish/secret \
                 -s malloc,256m"

This will run the Varnish HTTP server on port 80 and keep it's admin interface
hidden from the world, binding it to port 6082 on the lo interface.

The final step is to tell Varnish about the pypipins server.

.. code::

    /etc/varnish/default.vcl


    backend default {
        .host = "127.0.0.1";
        .port = "8888";
    }

    sub vcl_recv {
        if (req.request != "GET") {
            return(pipe);
        }

        if (req.request == "GET") {
            remove req.http.cookie;
            remove req.http.authenticate;
            remove req.http.Etag;
            remove req.http.If-None-Match;
            return(lookup);
        }
        return(pass);
    }

    sub vcl_fetch {
        if (beresp.status >= 300) {
            return(hit_for_pass);
        }

        set beresp.ttl = 1h;
        set beresp.grace = 6h;
        unset beresp.http.Set-Cookie;
        unset beresp.http.Etag;
        unset beresp.http.Cache-Control;
        set beresp.http.Cache-Control = "no-cache";
        return (deliver);
    }

    sub vcl_deliver {
          if (obj.hits > 0) {
                set resp.http.X-Cache = "HIT";
                set resp.http.X-Cache-Hits = obj.hits;
          } else {
                set resp.http.X-Cache = "MISS";
          }
    }

All done, restart Varnish.

.. code:: bash

    sudo /etc/init.d/varnish restart

You'll be able to go to `http://yourserver.tld/download/<PACKAGE>/badge.svg
<http://yourserver.tld/download/PACKAGE/badge.svg>`_ and everything should be
working as expected.

Notes on PyPy
=============

I personally use PyPy for running the pypipins server because, it's a long
running process and PyPy speeds it up wonderfully.

If you're using Debian 7, the latest version of PyPy as of writing is 2.3.1 and
requires libffi6, if you're using one of the prebuilt binaries. libffi6 is only
available in Jessie which is currently in testing.

You can either use an older version of PyPy or, backport libffi6 from Jessie.

.. code::

    /etc/apt/sources.list


    deb ftp://ftp.debian.org/debian/ jessie main

.. code::

    /etc/apt/preferences.d/jessie


    Package: *
    Pin: release a=wheezy
    Pin-Priority: 900

    Package: libffi*
    Pin: release a=jessie
    Pin-Priority: 910

This will keep all packages pinned to wheezy except libffi+wildcard, which will
be pulled from Jessie.

You can then simply install libffi6 from Jessie.

.. code:: bash

    sudo apt-get update
    sudo apt-get -u install libffi6/jessie

SSL
===

If you want to use SSL with your shields, you'll need to install nginx in front
of Varnish.

So instead of running Varnish on port 80, as shown above. Put it on a different
port, install and use nginx as you would for any other website and simply proxy
all requests back to Varnish.
