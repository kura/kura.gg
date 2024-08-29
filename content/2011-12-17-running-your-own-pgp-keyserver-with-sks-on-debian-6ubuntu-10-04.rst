Running your own PGP keyserver with SKS on Debian 6/Ubuntu 10.04
################################################################
:date: 2011-12-17 15:58
:author: kura
:category: tutorials
:tags: debian, keyserver, pgp, sks, ubuntu
:slug: running-your-own-pgp-keyserver-with-sks-on-debian-6ubuntu-10-04

.. contents::
    :backlinks: none

Installation
------------

To install we need to run the following command:

.. code-block:: bash

    sudo apt-get install -y sks

Now we build the key database:

.. code-block:: bash

    sudo sks build

And change the permissions for the sks user:

.. code-block:: bash

    sudo chown -R debian-sks:debian-sks /var/lib/sks/DB

Next we need to make sks start from init, open up **/etc/default/sks**
in your favourite editor and ***initstart*** to look like below:

.. code-block:: bash

    initstart=yes

Now we can start the service with:

.. code-block:: bash

    sudo /etc/init.d/sks start

Your keyserver will now be up and running on port 11371.

Web interface
-------------

We'll need to create a web folder within sks with the following command:

.. code-block:: bash

    sudo mkdir -p /var/lib/sks/www/

Change it's permissions so the sks user can access it.

.. code-block:: bash

    sudo chown -R debian-sks:debian-sks /var/lib/sks/www

And finally we need create a single HTML file for the interface, I have
provided that too.

.. code-block:: bash

    sudo wget /files/sks-index.html -O /var/lib/sks/www/index.html

Now your PGP server should be accessible from a web browser at
`https://YOUR_SERVER:11371/`_ and it should look like mine
`:11371/`_

.. _`https://YOUR_SERVER:11371/`: https://YOUR_SERVER:11371/
.. _`:11371/`: https://syslog.tv/
