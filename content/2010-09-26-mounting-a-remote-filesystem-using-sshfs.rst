Mounting a remote filesystem using sshfs
########################################
:date: 2010-09-26 01:55
:author: kura
:category: tutorials
:tags: ssh, sshfs
:slug: mounting-a-remote-filesystem-using-sshfs

First we need to install sshfs.

.. code-block:: bash

    sudo apt-get install sshfs fuse-utils

Now we make a mount point, I'm going to use a directory in my home
directory for this.

.. code-block:: bash

    mkd﻿ir ~/remote-content

And now we simply mount our remote directory to it.

.. code-block:: bash

    sshfs user@host:/path/to/location ~/remote-content

It's as simple as that.
