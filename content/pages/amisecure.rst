Am I Secure?
############
:date: 2011-10-20 11:38
:author: kura
:slug: amisecure

.. contents::
    :backlinks: none

This program is still in Alpha phase and is nowhere
near complete. It's purpose is quite simply to be run on a server and
let you know if there are any possible security holes in your
configuration. It is designed and configured around Debian so will not
work properly on Red Hat-based distributions without modifications to
the tests.

What can it scan?
-----------------

- OpenSSH
- nginx
- Apache2
- PHP5
- DenyHosts

How does it work?
-----------------

Am I secure will open up your configuration files in the order that each
program would include them in, for example Apache2 includes them in the
following order on Debian-based systems;

1. /etc/apache2/apache2.conf,
2. /etc/apache2/mods-enabled/\*,
3. /etc/apache2/httpd.conf,
4. /etc/apache2/ports.conf,
5. /etc/apache2/conf.d/\*,
6. /etc/apache2/sites-enabled/\*,

it will then run through each this, ignoring commented out config
options and show you where things are configured insecurely.

Caveats
-------

Am I Secure is a tool that helps show possible security holes, but it is
just a basic tool.

Downloads
---------

***Please note this is alpha software.***

- `.tar.gz`_
- `.zip`_

.. _.tar.gz: https://github.com/kura/amisecure/tarball/master
.. _.zip: https://github.com/kura/amisecure/zipball/master

Requires
--------

- Python >2.6

Usage
-----

Once downloaded simply run

.. code:: bash

    sudo python amisecure.py

Example output
--------------

.. image:: https://kura.io/images/output-amisecure.png
   :alt: Am I Secure?

Issue tracking
--------------

`Issue tracking is on GitHub`_.

.. _Issue tracking is on GitHub: https://github.com/kura/amisecure/issues

Source
------

You can fork, modify and create pull requests `on GitHub`_.

.. _on GitHub: https://github.com/kura/amisecure
