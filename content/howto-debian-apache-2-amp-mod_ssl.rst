HOWTO: Debian, Apache 2 & mod_ssl with self signed cert. or officially signed cert.
###################################################################################
:date: 2010-01-12 22:57
:author: kura
:category: tutorials
:tags: apache, debian, mod_ssl, ssl
:slug: howto-debian-apache-2-amp-mod_ssl

.. contents::

This is gonna be quite a simple tutorial that should be the same
(excluding pathing and apt) across other Linux distros.

Installation
------------

First off we'll get Apache and mod_ssl install

.. code:: bash

    sudo apt-get install apache2

SSL should be enabled by default, if not run the following

.. code:: bash

    sudo a2enmod ssl

SSL certificate
---------------

There are several ways of doing this, the first you need to figure out
is if you want a self signed certificate or one signed by a provider
like GeoTrust, this type is not free. In this article I'll cover both,
starting with self signed.

Self signed
~~~~~~~~~~~

.. code:: bash

    sudp mkdir /etc/apache2/ssl
    sudo /usr/sbin/make-ssl-cert /usr/share/ssl-cert/ssleay.cnf /etc/apache2/ssl/apache.pem

Provider signed
~~~~~~~~~~~~~~~

Please note, this type of certificate has to be paid for, prices at time
of writing range from £15/year to £2,000/year.

There are actually some more options when it comes to generating a key
for this CRT, the first way creates a key that does not require a
passphrase, the second way requires a passphrase and, unless you make a
special change to your Apache config along with a small bash script
(will go through later) will ask you for the passphrase for each key
every time you restart Apache.

Without a passphrase
^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    openssl genrsa -out DOMAINNAME.key 4096

With a passphrase
^^^^^^^^^^^^^^^^^

.. code:: bash

    openssl genrsa -des3 -out DOMAINNAME.key 4096

Replace DOMAINNAME with your domain name, I find this makes it much
easier if all of my certs and keys are named accordingly, but that's
just me. I also generally use at least a 4096bit modulus, feel free to
change this to whatever you wish, some signers will only take a key of a
specific size.

Next up is actually generating the CSR from the key.

.. code:: bash

    openssl req -new -key DOMAINNAME.key > DOMAINNAME.csr

As a note, it's very badly wordly but COMMON NAME is the actual fully
qualified domain name that you want to use SSL on, if your domain name
is example.com and you want this to work on www.example.com but did not
buy a wildcard certificate then put www.example.com as your Common Name.

Once generated, send this off to your signer and they will send you a
CRT in return.

Once you have your CRT it's time to put them on the server, move your
key file to Debian's SSL directory.

Put your CRT on the server and move it to Debian's SSL directory too.

Apache configuration
--------------------

First thing we need to do is check your Apache ports.conf file to make
sure SSL is enabled.

It should have the following at the bottom.

.. code:: apache

    <IfModule mod_ssl.c>
        # SSL name based virtual hosts are not yet supported, therefore no
        # NameVirtualHost statement here
        Listen 443
    </IfModule>

Now that's sorted we'll move on to your actual virtualhost.

.. code:: bash

    sudo nano /etc/apache2/sites-available/DOMAINNAME.conf

We'll use a config template I've always used, feel free to edit it at
need.

.. code:: apache

    <VirtualHost *>
        ServerAdmin webmaster@DOMAINNAME
        ServerName DOMAINNAME
        DocumentRoot /var/www/DOMAINNAME

        <Directory />
            Options FollowSymLinks
            AllowOverride None
        </Directory>

        <Directory /var/www/DOMAINNAME>
            Options -Indexes FollowSymLinks MultiViews
            AllowOverride All
            Order allow,deny
            allow from all
        </Directory>
    </VirtualHost>

    <VirtualHost *:443>
        ServerAdmin webmaster@DOMAINNAME
        ServerName DOMAINNAME
        DocumentRoot /var/www/DOMAINNAME

        <Directory />
            Options FollowSymLinks
            AllowOverride None
        </Directory>

        <Directory /var/www/DOMAINNAME>
            Options -Indexes FollowSymLinks MultiViews
            AllowOverride All
            Order allow,deny
            allow from all
        </Directory>

         SSLEngine On
         SSLCertificateFile /etc/apache2/ssl/apache.pem
    </VirtualHost>

If you used the self signed approach then the above
**SSLCertificateFile** will be correct, if not replace it with what is
shown below.

.. code:: apache

    SSLCertificateFile /etc/ssl/certs/DOMAINANE.crt
    SSLCertificateKeyFile /etc/ssl/private/DOMAINNAME.key

If you received a bundle file as well as your domains CRT then copy it
to /etc/ssl/certs/ on your server and add the following line after
**SSLCertificateKeyFile**.

.. code:: apache

    SSLCertificateChainFile /etc/ssl/certs/DOMAINNAME.bundle.crt

Save and exit, with that done we need to enable the site.

.. code:: bash

    sudo a2ensite DOMAINNAME.conf

If you used a self signed certificate or passphrase-free key, this
should be all you need to do, feel free to test your config and restart
Apache and test your site.

.. code:: bash

    sudo apache2ctrl configtest
    sudo /etc/init.d/apache2 restart

If you used a key with a passphrase you will either have to type your
passphrase in each time you restart Apache or, use this wonderful Apache
supported "hack" below...

The nasty SSL passphrase hack...
--------------------------------

.. code:: bash

    sudo nano /etc/apache2/apache2.conf

Place the following at the end of the file

.. code:: apache

    SSLPassPhraseDialog exec:/etc/apache2/ssl.sh

Now we need to create this bash file, so...

.. code:: bash

    sudo nano /etc/apache2/ssl.sh

Place the following in it

.. code:: bash

    #!/bin/bash
    if [ $1 = 'DOMAINNAME:443' ]; then
        echo "PASSPHRASE"
    fi

This is actually supported by Apache, when it's restarted it will call
this script for every SSL virtualhost you have enabled, passing the
hostname and the port through to the script as $1, so you can add
multiple sites to this file.

Now save and make it only usable by root.

.. code:: bash

    sudo chmod 0700 /etc/apache2/ssl.sh
    sudo chown root:root /etc/apache2/ssl.sh

Now we can follow the config test and restart call from above.

.. code:: bash

    sudo apache2ctl configtest
    sudo /etc/init.d/apache2 restart

And that is it, we should be done!
