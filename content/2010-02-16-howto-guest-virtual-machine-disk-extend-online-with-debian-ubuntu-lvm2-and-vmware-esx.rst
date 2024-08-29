HOWTO: Guest Virtual Machine disk extend online with Debian/Ubuntu, LVM2 and VMWare ESX
#######################################################################################
:date: 2010-02-16 18:20
:author: kura
:category: tutorials
:tags: cfdisk, debian, esx, howto, logical volume management, lvm, lvm2, partition, ubuntu, vmware
:slug: howto-guest-virtual-machine-disk-extend-online-with-debian-ubuntu-lvm2-and-vmware-esx

.. contents::
    :backlinks: none

Over the last two days I've had the interesting task of online some VMs
from clones and increasing their disk space to accommodate a mass of
user uploaded content. I've done this before but never actually with an
Logical Volume Management (LVM) disk.

My first approach, like a fool, was to clone the VM from source and boot
it from a remotely mounted GParted ISO, this didn't actually go as
expected and I was unable to add it to the LVM, I found a nice guide
online and consulted a colleague because I knew he'd done something
similar recently. After the first successful size increase I realised I
was able to do it without ever rebooting the machine itself, this is
accomplished by actually adding an extra disk to the VM, this disk can
then be partition with cfdisk and then added to the LVM, thus increasing
disk space without the need to resize the actual main disk. The LVM
doesn't care if the disks are physically separate (in this case they
aren't, they're on the same SAN but are still seen by the OS as being
different devices), as far as the LVM is concerned it will actually just
make them appear to the OS as one disk, even though made up from
different parts.

So, onwards.

Assigning the additional space to the VM
----------------------------------------

This is rather easy, I'm going to assume anyone that is reading this
guide has VMWare installed, their host and guests configured properly.
etc. This guide is also aimed at ESX but is still easily applicable to
ESXi, VMWare player, etc.

Within ESX, modify your VMs settings, adding an additional SCSI hard
disk, I'm going to give mine an additional drive with 210GB of space.

Partitioning the newly added space
----------------------------------

Once done, go to your VM, and as root run the following command:

.. code-block:: bash

    sudo echo "- - -" > /sys/class/scsi_host/**host0**/scan && fdisk -l

If the newly added unpartitioned drive isn't displayed, try again with a
different **host#** - host1, host2 etc.

.. code-block:: bash

    sudo cfdisk /dev/sda

If you don't have cfdisk installed, you should be able to install it
with the following command on Debian-based systems:

.. code-block:: bash

    sudo apt-get install cfdisk

Once you have it running the ASCII interface should be simple to follow,
select your unallocated space and partition it, making sure you select
it's type as **Logical Volume** (8E) and **not set it as bootable**.
Write these changes and close cfdisk.

::

    Name Flags Part Type FS Type [Label] Size (MB)

    ------------------------------------------------------------------------------
    sda1 Boot Primary Linux ext3 254.99
    sda5 Logical Linux LVM 10479.01
    sda6 Logical Linux LVM 225487.83

Adding to an existing LVM
-------------------------

Lets take a look at our current list of physical volumes

.. code-block:: bash

    pvs

    PV VG Fmt Attr PSize PFree
    /dev/sda5 jeos-base lvm2 a- 9.76G 0

As you can see we have our existing list of volumes, in my case one.

So now all we need to do is create another physical volume, my partition
is labelled **sda6** so that's what I will be using.

.. code-block:: bash

    sudo pvcreate /dev/sda6

Now that we've added the volume it's time to add it to the volume group,
this is really simple and again I'll be using sda6.

.. code-block:: bash

    sudo vgextend jeos-base /dev/sda6

jeos-root is the name of my volume group, you'd obviously replace this
with your own groups name.

Now if we actually take a look at pvs again you will see that your
physical volume has been created and added to your volume group.

.. code-block:: bash

    pvs && lvdisplay

    PV VG Fmt Attr PSize PFree
    /dev/sda5 jeos-base lvm2 a- 9.76G 0
    /dev/sda6 lvm2 -- 210.00G 0

    --- Logical volume ---
    LV Name /dev/jeos-base/root
    VG Name jeos-base
    LV UUID 1234
    LV Write Access read/write
    LV Status available
    # open 1
    LV Size 9.76 GB
    Current LE 12620
    Segments 2
    Allocation inherit
    Read ahead sectors 0
    Block device 254:0

The first output shows that your device has been added to the volume
group, the second output will show you that it isn't actually added to
the LVM, so the next step is to actually extend the LVM

Thanks to Ivan Marinkovic from the comments for this improved command::

.. code-block:: bash

    sudo lvextend -l+100%FREE /dev/jeos-base/root && lvdisplay

    --- Logical volume ---
    LV Name /dev/jeos-base/root
    VG Name jeos-base
    LV UUID 1234
    LV Write Access read/write
    LV Status available
    # open 1
    LV Size 219.30 GB
    Current LE 56140
    Segments 2
    Allocation inherit
    Read ahead sectors 0
    Block device 254:0

With the output of lvextend you will see that it successfully extending
the logical volume and lvdisplay should confirm that.

Resizing the file system
------------------------

Now that we have the LVM extended we will actually want to extend the
file system too, so that it can use the full extra space freely, this
can be done online, I'd recommend doing a snapshot or backup of your VM
before doing this though.

.. code-block:: bash

    sudo resize2fs /dev/mapper/jeos--base-root && df -h

    Filesystem Size Used Avail Use% Mounted on
    /dev/mapper/jeos--base-root
    218G 1.7G 205G 1% /

And that's it, all done. The output of df should confirm that your free
space has now increased in size.

*Credits*

- `Original guide that I partially followed with a colleague <https://www.randombugs.com/linux/howto-extend-lvm-partition-online.html>`_
- `Federico Marani, the colleague that helped <`https://marro.wordpress.com/`>_ (Italian)
- Thanks to Mike Heald for linking me to reloading SCSI list

