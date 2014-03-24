Moved debian and ubuntu to separate repositories on apt.kura.io
###############################################################
:date: 2014-03-24 19:19
:author: kura
:category: deb builds
:tags: apt
:slug: moved-debian-and-ubuntu-to-separate-repositories-on-apt.kura.io

.. contents::

I have made a breaking change to the `apt.kura.io <https://kura.io/apt.kura.io/>`__ 
repositories.

Ubuntu is now properly supported, but to do this properly it meant separating 
Ubuntu and Debian in to totally separate sections to fix the dependency 
issues.

Breaking changes
================

Anyone currently using apt.kura.io as it is will get 404 errors and will need to 
reconfigure their APT settings.

Debian
------

.. code::

    sudo sed -i 's/apt.kura.io\//apt.kura.io\/debian\//g' /etc/apt/sources.list.d/apt.kura.io.list

Ubuntu
------

.. code::

    sudo sed -i 's/apt.kura.io\//apt.kura.io\/ubuntu\//g' /etc/apt/sources.list.d/apt.kura.io.list
