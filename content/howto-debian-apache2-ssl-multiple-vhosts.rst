HOWTO: Debian - Apache 2 SSL on multiple virtual hosts
######################################################
:date: 2010-01-15 06:24
:author: kura
:category: tutorials
:tags: apache, debian, eth0, howto, mod_ssl, networking, ssl, vhost
:slug: howto-debian-apache2-ssl-multiple-vhosts

Figured I'd write this one up quickly as it proved to annoy the hell out
of me at 4:30am this morning getting it working on a live server.

Apache 2 can serve SSL content to multiple vhosts on your setup,
provided they use different IP addresses, this post will give you a
quick run down on how to do it.

First up we need to actually add the new IP to the machine in
/etc/network/interfaces.

::

    auto eth0
    iface eth0 inet static
        address 10.1.1.7
        netmask 255.255.255.0
        gateway 10.1.1.1

    auto eth0:1
    iface eth0:1 inet static
        address 10.1.1.8
        netmask 255.255.255.0

Replace my IPs with your own.

Restart networking.

.. code-block:: bash

    sudo /etc/init.d/networking restart

Next task is Apache 2 to configure it to listen on both IPs.

    /etc/apache2/ports.conf

My changes

.. code-block:: apache

    <IfModule mod_ssl.c>
        Listen 10.1.1.7:443
        Listen 10.1.1.8:443
        NameVirtualHost 10.1.1.7:443
        NameVirtualHost 10.1.1.8:443
    </IfModule>

That basically tells Apache to listen to port 443 on both those IP
addresses and sets up 2 NameVirtualHosts, 1 for each IP:PORT.

The next step is to set up the VirtualHosts, I am going to use a sample
that has almost no directives, excluding all of the actual SSL
directives to make things easier to read.

Host 1

.. code-block:: apache

    <VirtualHost 10.1.1.7:443>
        ServerName web1.example.com
        DocumentRoot /path/to/html1
    </VirtualHost>

Host 2

.. code-block:: apache

    <VirtualHost 10.1.1.8:443>
        ServerName web2.example.com
        DocumentRoot /path/to/html2
    </VirtualHost>

That is a very basic config but I hope it helps you understand how each
VirtualHost actually works when multiple IPs are used.

.. code-block:: bash

    sudo apache2ctl configtest
    sudo /etc/init.d/apache2 restart
