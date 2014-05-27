Nagios3 + MK Livestatus + xinetd on Debian 6/Ubuntu
###################################################
:date: 2011-10-13 23:17
:author: kura
:category: tutorials
:tags: mk livestatus, nagios, nagios 3, nagios broker, xinetd
:slug: nagios3-mk-livestatus-xinetd

.. contents::
    :backlinks: none

Preparation
-----------

First we need to make sure we have all the stuff we need to compile mk
livestatus and run it

.. code:: bash

    sudo apt-get install make build-essential xinetd ucspi-unix

MK Livestatus
-------------

Grab the mk livestatus source from `here`_, currently it's version
1.1.10p3 but update the commands below to match your version.

.. _here: http://mathias-kettner.de/check_mk_download.html

.. code:: bash

    wget http://mathias-kettner.de/download/mk-livestatus-1.1.10p3.tar.gz
    tar xvzf mk-livestatus-1.1.10p3.tar.gz
    cd mk-livestatus-1.1.10p3
    ./configure
    make
    sudo make install

Xinetd
------

Now that it's compiled we need to write a xinetd config for it, create a
new file called **/etc/xinetd.d/livestatus** and put the following in it

::

    service livestatus {
        type = UNLISTED
        port = 6557
        socket_type = stream
        protocol = tcp
        wait = no
        cps = 100 3
        instances = 500
        per_source = 250
        flags = NODELAY
        user = nagios
        server = /usr/bin/unixcat
        server_args = /var/lib/nagios3/rw/live
        only_from = 127.0.0.1 # modify this to only allow specific hosts to connect, currenly localhost only
        disable = no
    }

Now we restart xinetd using

.. code:: bash

    sudo /etc/init.d/xinetd restart

Nagios3
-------

Now we need to open up **/etc/nagios3/nagios.cfg** and add the following
line

::

    event_broker_options=-1 broker_module=/usr/local/lib/mk-livestatus/livestatus.o /var/lib/nagios3/rw/live

Now we need to restart Nagios

.. code:: bash

    sudo /etc/init.d/nagios3 restart

If you take a look in **/var/log/nagios3/nagios.log**

.. code:: bash

    sudo tail -n 100 /var/log/nagios3/nagios.log

you should see something like below

::

    [1318547328] livestatus: Livestatus 1.1.10p3 by Mathias Kettner. Socket: '/var/lib/nagios3/rw/live'
    [1318547328] livestatus: Please visit us at http://mathias-kettner.de/
    [1318547328] livestatus: Hint: please try out OMD - the Open Monitoring Distribution
    [1318547328] livestatus: Please visit OMD at http://omdistro.org
    [1318547328] Event broker module '/usr/local/lib/mk-livestatus/livestatus.o' initialized successfully.

Also, we can ls the newly created socket

.. code:: bash

    ls -lah /var/lib/nagios3/rw/live

    srw-rw---- 1 nagios www-data 0 2011-10-14 00:08 /var/lib/nagios3/rw/live

We can test is by creating a test file called host_query with the
following content

::

    GET hosts

And run the following command

.. code:: bash

    sudo unixcat < host_query /var/lib/nagios3/rw/live

If all worked you should see output.
