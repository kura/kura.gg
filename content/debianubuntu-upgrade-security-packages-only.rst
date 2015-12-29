Debian/Ubuntu upgrade security packages only
############################################
:date: 2010-12-13 16:27
:author: kura
:category: tutorials
:tags: apt-get, aptitude, security, update, upgrade
:slug: debianubuntu-upgrade-security-packages-only

**The command below no longer works, for an updated version that does
work and should continue to work (until you upgrade to a new distro
version e.g. 10.04 -> 12.04) please see `here`_.**

.. _here: /2011/09/21/debianubuntu-upgrade-security-packages-only-a-better-way-to-do-it/

Really simple, should work for most cases, I've not found anything wrong
with it.

.. code:: bash

    sudo aptitude update && sudo aptitude install '?and(~U,~Asecurity)'
