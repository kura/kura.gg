rabbitmq-nagios
###############
:date: 2011-11-10 20:56
:author: kura
:tags: nagios, rabbitmq, rabbitmqctl
:slug: rabbitmq-nagios

.. contents::
    :backlinks: none

A set of plugins for Nagios to monitor RabbitMQ using rabbitmqctl.

Downloads
---------

- `.tar.gz`_
- `.zip`_

.. _.tar.gz: https://github.com/kura/rabbitmq-nagios/tarball/master
.. _.zip: https://github.com/kura/rabbitmq-nagios/zipball/master

Requires
--------

-  Python 2.6+

Installation
------------

Download the zipball or tarball, extract it on to the server you wish to
monitor.

Then move it to the directory where your Nagios plugins are installed,
on Debian/Ubuntu with an APT installed Nagios this is:

    /var/lib/nagios/plugins

You will need to give the nagios user sudo privileges to run these
scripts, making sure that you only allow a passwordless sudo to the
scripts you want to use

.. code:: bash

    nagios ALL=(ALL)
    NOPASSWD:/usr/lib/nagios/plugins/check_rabbitmq_queue_length

Usage
-----

You simply need to add a command to NRPE to allow the plugin to be
called

::

    command[check_rabbitmq_queue_length]=sudo /usr/lib/nagios/plugins/check_rabbitmq_queue_length -w 10000 -c 20000 -v /

And finally add that check to your host within your main Nagios
installation.

Source
------

`Here`_.

.. _Here: https://github.com/kura/rabbitmq-nagios
