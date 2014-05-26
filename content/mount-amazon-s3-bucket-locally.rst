Mount Amazon S3 bucket locally on Debian 5 & 6/Ubuntu 10.04
###########################################################
:date: 2012-03-03 16:05
:author: kura
:category: tutorials
:tags: aws, fstab, fuse, mount, s3, s3fs
:slug: mount-amazon-s3-bucket-locally

.. contents::

I've recently been toying with my `Raspberry Pi mirror`_ including
moving it out on to Amazon's S3. I've written an article on `how to back
up to S3`_, but that isn't enough when it comes to serving data
from S3.

.. _Raspberry Pi mirror: http://rpi.syslog.tv/
.. _how to back up to S3: https://syslog.tv/2012/02/29/backup-a-linux-server-to-amazon-s3-on-debian-6ubuntu-10-04/

I needed the ability to RSYNC data from the official Raspberry Pi
servers on to mine and then in to S3 and for that I used `s3fs`_ and
`FUSE`_.

.. _s3fs: http://code.google.com/p/s3fs/
.. _FUSE: http://fuse.sourceforge.net/

FUSE
----

You can actually do this successfully without requiring FUSE, just by
installing the s3fs binary on to your system, but this only allows the
user who mounted to access the mounted bucket and also is not possible
via /etc/fstab.

FUSE allows you to implement a filesystem within a userspace program,
thus allowing us to give other users access and auto-mount using
/etc/fstab.

Installation
------------

Fuse
~~~~

Installing FUSE is simple

.. code:: bash

    sudo apt-get install fuse-utils

s3fs
~~~~

We'll need to get build-essential, pkg-config, libfuse-dev,
libcurl4-openssl-dev and libxml2-dev to be able to compile s3fs

.. code:: bash

    sudo apt-get install build-essential pkg-config libfuse-dev libcurl4-openssl-dev libxml2-dev

Debian 5 & Ubuntu 10.04
^^^^^^^^^^^^^^^^^^^^^^^

If installing either Debian 5 or Ubuntu 10.04, you'll need to install a
newer version of fuse than is packaged, I found this info on the `s3fs
issue tracker`_.

.. _s3fs issue tracker: http://code.google.com/p/s3fs/issues/detail?id=143#c2

First we need to remove the install fuse-utils and libfuse-dev that we
install above.

.. code:: bash

    sudo apt-get purge fuse-utils libfuse-dev

You'll need to export a variable with your arch, i.e

.. code:: bash

    export PLATFORM=amd64
    wget http://ftp.us.debian.org/debian/pool/main/f/fuse/libfuse2_2.8.4-1.1_${PLATFORM}.deb
    wget http://ftp.us.debian.org/debian/pool/main/f/fuse/libfuse-dev_2.8.4-1.1_${PLATFORM}.deb
    wget http://ftp.us.debian.org/debian/pool/main/f/fuse/fuse-utils_2.8.4-1.1_${PLATFORM}.deb
    sudo dpkg -i libfuse2_2.8.4-1.1_${PLATFORM}.deb libfuse-dev_2.8.4-1.1_${PLATFORM}.deb fuse-utils_2.8.4-1.1_${PLATFORM}.deb

Fix missing dependencies

.. code:: bash

    sudo apt-get -f install

Now run the command below and confirm the output

.. code:: bash

    pkg-config --modversion fuse
    2.8.4

s3fs has to be done manually, first off go download the latest revision
archive from `Google code`_.

.. _Google code: http://code.google.com/p/s3fs/downloads/list

Once download, gunzip and untar it.

.. code:: bash

    tar xvzf s3fs-x.xx.tar.gz

Change directory in to your newly extracted archive, and configure.

.. code:: bash

    ./configure --exec-prefix=/usr/ --prefix=/ --includedir=/usr/include/ --mandir=/usr/share/man/

This configure command will install the s3fs binary in to /usr/bin and
man pages in to /usr/share/man/ which is Debian and Ubuntu correct
locations.

Then you'll need to compile and install.

.. code:: bash

    make
    sudo make install

*You'll noticed I only run make install as sudo/root, because the other
commands do not require it and you should never compile as root.*

Configure s3fs
--------------

The only configuration you need to do for s3fs is store your S3
credential which you can get `the Amazon website`_.

.. _the Amazon website: https://aws-portal.amazon.com/gp/aws/securityCredentials

Create a file called **/etc/passwd-s3fs** - **MAKE SURE YOU DON'T BREAK
/etc/passwd**

In it you need to put your access key ID and secret access key,
separated with a colon.

    ACCESS_KEY_ID:SECRET_ACCESS_KEY

And for security reasons, change the file permissions

.. code:: bash

    sudo chmod 0600 /etc/passwd-s3fs

Mounting
--------

Manual
~~~~~~

Once all the above is done you can mount a bucket using the s3fs binary,
I'm going to mount directly to /mnt

.. code:: bash

    sudo s3fs your-bucket-name /mnt

This will mount it and make it usable for your user.

fstab
~~~~~

Mounting via fstab requires the above FUSE step to be completed.

Your **/etc/fstab** entry should look like this

.. code:: bash

    s3fs#your-bucket-name /mnt fuse allow_other,_netdev,nosuid,nodev,url=https://s3.amazonaws.com 0 0

A brief description of the mount arguments;

- **allow_other** - allow all users to access the mount point,
- **_netdev** - The filesystem resides on a device that requires
  network access,
- **nosuid** - Do not allow set-user-identifier or set-group-identifier
  bits to take effect,
- **nodev** - Do not interpret character or block special devices on
  the file system and
- **url** - Use HTTPS instead of HTTP when configure as above
