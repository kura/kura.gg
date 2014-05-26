Adding swap while the server is online with Debian and VMWare ESX
#################################################################
:date: 2010-07-07 18:56
:author: kura
:category: tutorials
:tags: debian, swap, vmware
:slug: adding-swap-while-the-server-is-online-with-debian-and-vmware-esx

.. contents::

Recently I had to install Oracle on a virtual machine but didn't find
out until after I'd spun up of the machine that Oracle required at least
2GB of swap space, my machine did not have enough.

Thankfully it's quite simple to increase swap space, using VMWare ESX,
simple add a new drive to the machine as you normally would, I used 5GB.

Detecting the new SCSI drive and partitioning it
------------------------------------------------

This bit is simple, I'm going to assume you're logged in as root.

.. code:: bash

    sudo echo "- - -" > /sys/class/scsi_host/**host0**/scan && fdisk -l

If host0 doesn't work, try changing to host1, host2 etc.

Now we need to format the drive, for me it was /dev/sdb.

.. code:: bash

    sudo cfdisk /dev/sdb

Create a new logical partition, set it's type to **82 Linux Swap** and
simply write the changes.

Adding swap
-----------

Next we simply add the swap space to the machine and enable it, for me
it was /dev/sdb5

.. code:: bash

    sudo mkswap /dev/sdb5
    sudo swapon /dev/sdb5

Add on reboot

And now we simply need to be sure to add the swap when the machine
reboots. Open the following file:

    /etc/fstab

And add

::

    /dev/sdb5 swap swap defaults 0 0

Simple.
