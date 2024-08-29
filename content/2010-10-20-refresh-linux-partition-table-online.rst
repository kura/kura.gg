Refresh Linux partition table online
####################################
:date: 2010-10-20 17:17
:author: kura
:category: tutorials
:tags: linux, online, partition
:slug: refresh-linux-partition-table-online

.. contents::
    :backlinks: none

If the device is not mounted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    sudo blockdev --rereadpt DEVICE

E.g.

.. code-block:: bash

    sudo blockdev --rereadpt /dev/sda

If the device is mounted
~~~~~~~~~~~~~~~~~~~~~~~~

Parted is awesome and does this job amazingly.

.. code-block:: bash

    sudo apt-get install parted
    sudo partprobe
