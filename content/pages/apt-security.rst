apt-security
############
:date: 2011-09-22 12:13
:author: kura
:tags: apt, security
:slug: apt-security

.. contents::

A set of programs to update packages from the APT security repositories.

This program does not improve your system security, it is merely a tool
to help you download security updates without having to download all
updated packages at the same time.

Downloads
---------

- `.tar.gz`_
- `.zip`_

.. _.tar.gz: https://github.com/kura/apt-security/tarball/master
.. _.zip: https://github.com/kura/apt-security/zipball/master

Requires
--------

- Debian or Debian-based operating system
- APT

Install
-------

Extract the tarball or zipball and run

.. code:: bash

    sudo ./installer

within the extracted directory.

Usage
-----

You will need to resynchronise your package index just like you would
normally using

.. code:: bash

    sudo apt-get update

Both commands listed below need to be run as root or sudo.

apt-security-sources
~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    /usr/bin/apt-security-sources

Refreshes the repository list from */etc/apt/sources.list* and stores it
in */etc/apt/security.sources.list*, this is called by the installer but
also should be run when you've upgraded to a new version of your
operating system.

apt-get-security
~~~~~~~~~~~~~~~~

.. code:: bash

    /usr/bin/apt-get-security

Does an upgrade of packages from the security repositories

Issues
------

`Issues go here <https://github.com/kura/apt-security/issues>`_.

Source
------

`Source is here <https://github.com/kura/apt-security>`_.
