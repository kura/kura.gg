Using dpkg selections to backup and install packages
####################################################
:date: 2010-07-02 18:32
:author: kura
:category: tutorials
:tags: apt, backup, dpkg, packages
:slug: using-dpkg-selections-to-backup-and-install-packages

.. contents::
    :backlinks: none

Sometimes you want to be able to install packages on another machine
without the hassle of a long apt-get install command or having to write
down every single package you've installed.

Luckily Debian has the wonderful dpkg which has 2 methods for generating
a list of installed packages and another for importing a list.

Generating a list of installed packages
---------------------------------------

.. code:: bash

    sudo dpkg --get-selections > selections

This will generate a file called *selections* which will contain
something like

::

    ... snip ...
    adduser install
    apache2 install
    apache2-mpm-prefork install
    apache2-utils install
    apache2.2-bin install
    apache2.2-common install
    apt install
    ... snip...

This is just a simple, plain text file so can be copied between servers.

Installing packages from an exported list
-----------------------------------------

This is almost just as easy, first we need to actually set the list of
selected packages

.. code:: bash

    sudo dpkg --set-selections < selections

Then we need to actually do an update and install

.. code:: bash

    sudo apt-get update && sudo apt-get -u dselect-upgrade

This last command will update your apt cache and then install all of the
selected packages.

*Please note that version numbers are **not** remembered so you will
install the latest version of each package.*
