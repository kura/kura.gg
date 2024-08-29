Moved debian and ubuntu to separate repositories on apt.kura.gg
###############################################################
:date: 2014-03-24 19:19
:author: kura
:category: deb builds
:tags: apt
:slug: moved-debian-and-ubuntu-to-separate-repositories-on-apt.kura.gg

.. contents::
    :backlinks: none

I have made a breaking change to the `apt.kura.gg </apt.kura.gg/>`__ 
repositories.

Ubuntu is now properly supported, but to do this properly it meant separating 
Ubuntu and Debian in to totally separate sections to fix the dependency 
issues.

Breaking changes
================

Anyone currently using apt.kura.gg as it is will get 404 errors and will need to 
reconfigure their APT settings.

Debian
------

.. code-block:: none

    sudo sed -i 's/apt.kura.gg\//apt.kura.gg\/debian\//g' /etc/apt/sources.list.d/apt.kura.gg.list

Ubuntu
------

.. code-block:: none

    sudo sed -i 's/apt.kura.gg\//apt.kura.gg\/ubuntu\//g' /etc/apt/sources.list.d/apt.kura.gg.list
