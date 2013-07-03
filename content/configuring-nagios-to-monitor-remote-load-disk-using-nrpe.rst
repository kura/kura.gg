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

    apt-get install nagios-plugins nagios-nrpe-server

Once installed, open up **/etc/nagios/nrpe\_local.cfg**

And place the following in it::

    allowed\_hosts=NAGIOS.SERVER.IP,127.0.0.1

    command[check\_users]=/usr/lib/nagios/plugins/check\_users -w 5 -c 10
    command[check\_load]=/usr/lib/nagios/plugins/check\_load -w 15,10,5 -c 30,25,20
    command[check\_all\_disks]=/usr/lib/nagios/plugins/check\_disk -w 20 -c 10
    command[check\_zombie\_procs]=/usr/lib/nagios/plugins/check\_procs -w 5 -c 10 -s Z
    command[check\_total\_procs]=/usr/lib/nagios/plugins/check\_procs -w 150 -c 200
    command[check\_swap]=/usr/lib/nagios/plugins/check\_swap -w 20 -c 10

Save and exit.

Commands need to explicitly be enabled on the remote server to actually
be runnable remotely, so you can add more plugins to this command list
any time you want.

Start the nagios-nrpe-server daemon.

    /etc/init.d/nagios-nrpe-server start

Monitoring server -- the server with Nagios installed
-----------------------------------------------------

Install the nagios nrpe plugin

    apt-get install nagios-nrpe-plugin

Now test the connection to the remote server we set up just now.

::

    #> /usr/lib/nagios/plugins/check\_nrpe -H REMOTE.SERVER.IP
    NRPE v2.8.1

If you get a version response it means it all works.

Now we simply add a service check for the host but use the check\_nrpe
plugin to do so.

::

    define service {
        host\_name HOSTNAME
        service\_description Load
        check\_command check\_nrpe\_1arg!check\_load
        use generic-service
        notification\_interval 0
    }

We have already defined the tolerances on the remote server in
nrpe\_local.cfg so we only need to use the check\_nrpe\_1arg command,
you can actually pass arguments using check\_nrpe as below.

::

    define service {
        host\_name HOSTNAME
        service\_description Load
        check\_command check\_nrpe!check\_load!5!10
        use generic-service
        notification\_interval 0
    }

Save, exit and reload nagios.

    /etc/init.d/nagios2 restart
