SimpleMTA
#########
:date: 2011-09-09 20:53
:author: kura
:slug: simplemta

.. contents::
    :backlinks: none

SimpleMTA is a Python and Eventlet powered MTA that can be configured to pretend to receive, bounce or mix responses to incoming messages. It can also be used to fake outbound sends.

No mail spools, no disk I/O (unless logging is turned on), low memory and CPU usage - SimpleMTA is designed to blindly accept or bounce all incoming and outgoing mail so you can test your send rate, email scripts and things like that.

Downloads
=========

- `.tar.gz`_
- `.zip`_

.. _.tar.gz: https://github.com/kura/simplemta/tarball/master
.. _.zip: https://github.com/kura/simplemta/zipball/master

Requires
========

- eventlet==0.9.15
- greenlet==0.3.1

These can be installed by simply running the following command:

.. code-block:: bash

    pip install -r requirements.txt

Configuration
=============

Sadly configuration is done directly in to src/simplemta.py but is well documented within the file itself.

Please note it is generally not a good idea to enable DEBUG mode, if you're receiving or sending a lot of email it can harm you disk.

Usage
=====

+----------------+---------+---------------------+
| ./simplemta.py | start   | Starts the server   |
+================+=========+=====================+
| ./simplemta.py | stop    | Stops the server    |
+----------------+---------+---------------------+
| ./simplemta.py | restart | Restarts the server |
+----------------+---------+---------------------+

Source
======

You can download, edit, fork and mess with the source as much as you want, it's available `here`_.

.. _here: https://github.com/kura/simplemta
