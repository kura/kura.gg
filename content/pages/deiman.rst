Deiman
######
:date: 2013-07-18 20:01
:author: kura
:slug: deiman

.. contents::

Deiman is a Python utility class for daemonizing a process.
It has start and stop methods as well as a method for
retrieving a process status information. It can also detect
stale PIDs and remove them.

.. image:: https://pypip.in/d/deiman/badge.png
    :alt: Deiman downloads
    :target: https://crate.io/packages/deiman

.. image:: https://pypip.in/v/deiman/badge.png
    :alt: Deiman version
    :target: https://crate.io/packages/deiman


Deiman uses the Unix double fork method to push the process
to the background.

Linux/Unix only, untested on Mac OS.

Installation
============

From PyPI
---------

.. code:: bash

    pip install deiman

From GitHub
-----------

.. code:: bash

    pip install -e git+git://github.com/kura/deiman.git#egg=deiman

From source
-----------

Download the latest tarball from PyPI or GitHub. Unpack and run:

.. code:: bash

    python setup.py install

Usage
=====

To use Deiman, you simply need to import the main Deiman class,
passing a path to where you want the pid to be stored and call
the start and stop methods as required

.. code:: python

    from deiman import Deiman


    d = Deiman("/tmp/a.pid")
    d.start()

    while True:
        print "This print will be hidden because I am daemonized"

Examples
========

See the `examples <https://github.com/kura/deiman/tree/master/examples>`_
directory for usage examples on GitHub.
