Bash portforwarding with autocompletion
#######################################
:date: 2013-03-12 18:00
:author: kura
:category: tutorials
:tags: autocompletion, bash, port forwarding
:slug: bash-portforwarding-with-autocompletion

.. contents::
    :backlinks: none

I spend a LOT of time with tunnels open to multiple machines, connecting
directly to PostgreSQL, RabbitMQ and many other services all via SSH.

I have written several helper functions and this is the final version
that I created in a small competition with `@codeinthehole.`_

.. _@codeinthehole.: https://twitter.com/codeinthehole

Gist removed. Sorry.

Installation
------------

Simply add the contents to *~/.bashrc*

Usage
-----

Usage is pretty simply, just called portforward from the command line,
pressing <TAB> as you type in a server name from your ~/.ssh/config file
and the same with the port.

.. code-block:: bash

    portforward sy<TAB>

Will become:

.. code-block:: bash

    portforward syslog.tv

And finally

.. code-block:: bash

    portforward syslog.tv 15672
