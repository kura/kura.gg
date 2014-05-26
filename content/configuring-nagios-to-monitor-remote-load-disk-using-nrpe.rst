Configuring Nagios to monitor remote load, disk, swap etc using NRPE
####################################################################
:date: 2010-03-21 21:55
:author: kura
:category: tutorials
:tags: debian, monitoring, nagios, nrpe, ubuntu
:slug: configuring-nagios-to-monitor-remote-load-disk-using-nrpe



I'll assume you already have Nagios installed and configured and have an
understanding of actually configuring and using Nagios.

Remote server -- the server to be monitored
-------------------------------------------

First we'll install the needed plugins and daemon on the **remote**
server.

.. code:: bash

    sudo apt-get install nagios-plugins nagios-nrpe-server

Once installed, open up **/etc/nagios/nrpe_local.cfg**

And place the following in it

::

    allowed_hosts=NAGIOS.SERVER.IP,127.0.0.1

    command[check_users]=/usr/lib/nagios/plugins/check_users -w 5 -c 10
    command[check_load]=/usr/lib/nagios/plugins/check_load -w 15,10,5 -c 30,25,20
    command[check_all_disks]=/usr/lib/nagios/plugins/check_disk -w 20 -c 10
    command[check_zombie_procs]=/usr/lib/nagios/plugins/check_procs -w 5 -c 10 -s Z
    command[check_total_procs]=/usr/lib/nagios/plugins/check_procs -w 150 -c 200
    command[check_swap]=/usr/lib/nagios/plugins/check_swap -w 20 -c 10

Save and exit.

Commands need to explicitly be enabled on the remote server to actually
be runnable remotely, so you can add more plugins to this command list
any time you want.

Start the nagios-nrpe-server daemon.

.. code:: bash

    sudo /etc/init.d/nagios-nrpe-server start

Monitoring server -- the server with Nagios installed
-----------------------------------------------------

Install the nagios nrpe plugin

.. code:: bash

    sudo apt-get install nagios-nrpe-plugin

Now test the connection to the remote server we set up just now.

.. code:: bash

    /usr/lib/nagios/plugins/check_nrpe -H REMOTE.SERVER.IP
    NRPE v2.8.1

If you get a version response it means it all works.

Now we simply add a service check for the host but use the check_nrpe
plugin to do so.

::

    define service {
        host_name HOSTNAME
        service_description Load
        check_command check_nrpe_1arg!check_load
        use generic-service
        notification_interval 0
    }

We have already defined the tolerances on the remote server in
nrpe_local.cfg so we only need to use the check_nrpe_1arg command,
you can actually pass arguments using check_nrpe as below.

::

    define service {
        host_name HOSTNAME
        service_description Load
        check_command check_nrpe!check_load!5!10
        use generic-service
        notification_interval 0
    }

Save, exit and reload nagios.

.. code:: bash

    sudo /etc/init.d/nagios2 restart
