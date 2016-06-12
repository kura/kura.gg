Deiman
######
:date: 2013-07-18 20:01
:author: kura
:slug: deiman

.. contents::
    :backlinks: none

Deiman is a Python utility class for daemonizing a process.
It has start and stop methods as well as a method for
retrieving a process status information. It can also detect
stale PIDs and remove them.

Deiman uses the Unix double fork method to push the process
to the background.

Linux/Unix only, untested on Mac OS.

Installation
============

From PyPI
---------

.. code-block:: bash

    pip install deiman

From GitHub
-----------

.. code-block:: bash

    pip install -e git+git://github.com/kura/deiman.git#egg=deiman

From source
-----------

Download the latest tarball from PyPI or GitHub. Unpack and run:

.. code-block:: bash

    python setup.py install

Usage
=====

To use Deiman, you simply need to import the main Deiman class,
passing a path to where you want the pid to be stored and call
the start and stop methods as required

.. code-block:: python

    from deiman import Deiman


    d = Deiman("/tmp/a.pid")
    d.start()

    while True:
        print "This print will be hidden because I am daemonized"

Examples
========

See the `examples <https://github.com/kura/deiman/tree/master/examples>`_
directory for usage examples on GitHub.
