Refresh Linux partition table online
####################################
:date: 2010-10-20 17:17
:author: kura
:category: tutorials
:tags: linux, online, partition
:slug: refresh-linux-partition-table-online

If the device is not mounted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    blockdev --rereadpt DEVICE

E.g.

    blockdev --rereadpt /dev/sda

If the device is mounted
~~~~~~~~~~~~~~~~~~~~~~~~

Parted is awesome and does this job amazingly.

    apt-get install parted
    partprobe
