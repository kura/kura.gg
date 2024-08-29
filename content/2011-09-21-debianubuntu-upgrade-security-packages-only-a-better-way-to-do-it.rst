Debian/Ubuntu upgrade security packages only - a better way to do it
####################################################################
:date: 2011-09-21 13:21
:author: kura
:category: tutorials
:tags: apt, debian, security, ubuntu, upgrades
:slug: debianubuntu-upgrade-security-packages-only-a-better-way-to-do-it

**I have created a scripts that handle these tasks for you, available
`here`_.**

.. _here: /apt-security/

First thing we need to do is create an sources list specifically for
security.

.. code-block:: bash

    sudo grep "-security" /etc/apt/sources.list | sudo grep -v "#" > /etc/apt/security.sources.list

Now that this is done we can simply continue to use the command below to
trigger security-only upgrades

.. code-block:: bash

    sudo apt-get upgrade -o Dir::Etc::SourceList=/etc/apt/security.sources.list

Note
----

**This will work until you upgrade your distro (e.g. 10.04 -> 12.04), at
which point you will need to re-run the first command to regenerate the
security.sources.list file.**
