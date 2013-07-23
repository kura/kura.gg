HOWTO: IPTables on Debian/Ubuntu
#################################
:date: 2010-02-11 16:51
:author: kura
:category: tutorials
:tags: debian, howto, iptables, networking, security, ubuntu
:slug: howto-iptables-on-debian-ubuntu

Installation
------------

Simple, if it's not installed already then run the following commands

.. code:: bash

    sudo apt-get install iptables
    sudo /etc/init.d/iptables start

The safest and best way of configuring iptables, in my opinion, is to
have two files. The first is a temporary/test set that you will save to
first, the second is the actual rule set that will be loaded to
iptables.

Configuration
-------------

So, first we'll create an empty temp rules file

.. code:: bash

    sudo touch /etc/iptables.temp.rules

Add some simple rules to it::

    *filter
    # Allows all loopback traffic and drop all traffic to 127/8 that doesn't use lo

    -A INPUT -i lo -j ACCEPT
    -A INPUT ! -i lo -d 127.0.0.0/8 -j REJECT

    # Accepts all established inbound connections
    -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

    # Allows all outbound traffic
    -A OUTPUT -j ACCEPT

    #SSH
    -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
    #HTTP
    -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
    #HTTPS
    -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
    #SMTP
    -A INPUT -p tcp -m tcp --dport 25 -j ACCEPT
    #IMAP
    -A INPUT -p tcp -m tcp --dport 143 -j ACCEPT
    #POP3
    -A INPUT -p tcp -m tcp --dport 110 -j ACCEPT
    #PING
    -A INPUT -p icmp -m icmp --icmp-type 8 -j ACCEPT

    # Log
    -I INPUT 5 -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7

    # Reject all other inbound - default deny unless explicitly allowed
    policy
    -A INPUT -j REJECT
    -A FORWARD -j REJECT

    COMMIT

Next we apply this rule set to the currently running iptables instance

.. code:: bash

    sudo iptables-restore < /etc/iptables.temp.rules

Check to make sure they loaded correctly

.. code:: bash

    sudo iptables -L

If everything looks OK and ready to go then we simply save, this time to
the secondary file that I mentioned earlier

.. code:: bash

    sudo iptables-save > /etc/iptables.up.rules

Network interface configuration
-------------------------------

Open up the following file with your favourite editor

    /etc/network/interfaces

Find the following lines::

    auto lo
    iface lo inet loopback

And add this to the end

.. code:: bash

    pre-up iptables-restore < /etc/iptables.up.rules

So that it becomes

.. code:: bash

    auto lo
    iface lo inet loopback
        pre-up iptables-restore < /etc/iptables.up.rules

This will restore your custom set of iptables rules when it instantiates
the network devices.

The future
----------

When you need to add more rules in the future, simply add them to your
iptables.temp.rules set, load them in to iptables as shown, if
everything looks good then save to iptables.up.rules

*Please note; this is only an extremely basic rule set and will need to
be improved upon by you or another sys admin in your team to properly
secure your server.*
