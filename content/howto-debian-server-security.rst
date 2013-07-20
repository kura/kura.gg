HOWTO: Debian server security
#############################
:date: 2010-01-14 19:57
:author: kura
:category: tutorials
:tags: apache, debian, denyhosts, howto, logwatch, php, security
:slug: howto-debian-server-security

Server security is something I've always tried to keep myself up-to-date
on. I have at least a dozen RSS feeds that I read daily to learn about
the latest flaws, holes releases etc. That being said I am by no means
an "expert", I've learned what I've needed to learn over time. I like to
think that over the years I've gained enough knowledge to almost
completely secure servers with all the programs installed that I
generally use.

The aim of this article is to introduce you to some of the programs I
use for security and some config changes that can be made to other
programs to make them more secure. It is aimed at web servers but other
changes work anywhere, like the SSH changes.

SSH
---

We'll start with a very simple change that makes a very big difference,
a change to the security of SSH. The file is located in the location
below on a Debian system.

    /etc/ssh/sshd_config

Replace this.

    PermitRootLogin yes

With this.

    PermitRootLogin no

This one change will massively reduce risk on your servers, no root SSH
access means no chance of brute forced accounts, well, not direct
attacks. Please be advised though, this change applies to you too, you
will have to log in to the server as another user and use **su** or
**sudo su**. You can always read my article on sudo/sudoers to learn
more about sudo.

DenyHosts
---------

This is one of my favourite programs, if not my favourite program and is
of course available from the Debian repository.

.. code:: bash

    sudo apt-get install denyhosts

Once installed it will configure itself and should start on it's own
too. DenyHosts will monitor your SSH logs and ban people that it sees
attacking you. One thing that should be mentioned is DenyHosts will only
work if SSH is compiled with TLS wrappers enabled. If you installed SSH
using apt-get this won't be an issue.

The way it works is really simple and partly explained above, DenyHosts
can be configured so you can set your own failed attempt thresholds, the
banned hosts are put in your denied hosts file, on a Debian system this
is:

    /etc/hosts.deny

If you're worried about banning yourself then put your IP address in
this file.

    /etc/hosts.allow

    ALL: YOUR.IP.HERE

Some changes I always make are shown below, don't use these without
reading the config file to see what they actually do.

::

    BLOCK_SERVICE = ALL
    DENY_THRESHOLD_INVALID = 5
    DENY_THRESHOLD_VALID = 10
    DENY_THRESHOLD_ROOT = 1
    DENY_THRESHOLD_RESTRICTED = 1
    HOSTNAME_LOOKUP=YES
    ADMIN_EMAIL = myemail@mydomain.tld
    SMTP_HOST = localhost
    SMTP_PORT = 25
    SMTP_HOST = localhost
    SMTP_PORT = 25
    SMTP_FROM = DenyHosts <denyhosts@SERVERNAME>
    SMTP_SUBJECT = DenyHosts Report from $[HOSTNAME]

Once configured simply restart the DenyHosts daemon.

.. code:: bash

    sudo /etc/init.d/denyhosts restart

Logwatch
--------

Next up is another fantastic little program. It's simple, it's
lightweight and... it's in the Debian repository.

.. code:: bash

    sudo apt-get install logwatch

This program does as it's name suggests, it watches your log files, it
then emails them to you every day and runs from **/etc/cron.daily**.

There really is no configuration required for logwatch, I personally
just edit the cron job to force a mailto.

.. code:: bash

    /usr/sbin/logwatch --mailto myemail@mydomain.tld

Logwatch will send you a nice, tidy email every day giving you stats
etc.

::

    --------------------- httpd Begin ------------------------
    Requests with error response codes

    400 Bad Request
    /w00tw00t.at.ISC.SANS.DFind:): 1 Time(s)
    /w00tw00t.at.ISC.SANS.test0:): 1 Time(s)

    404 Not Found
    //phpMyAdmin//scripts/setup.php: 1 Time(s)
    //phpmyadmin//scripts/setup.php: 1 Time(s)

As you can see, a few people have tried to find holes in my Apache and
also things that aren't even present on my server.

::

    Snip.

    --------------------- SSHD Begin ------------------------

    Users logging in through sshd:

    hidden:
    \*\*\*.\*\*\*.\*\*\*.\*\*\* (my.hostname.com): 4 times

    Refused incoming connections:
    190.144.99.98 (190.144.99.98): 2 Time(s)
    61.168.227.12 (61.168.227.12): 2 Time(s)
    host.united-rx.com (209.59.172.198): 2 Time(s)

    ---------------------- SSHD End -------------------------

    Snip.

    --------------------- Sudo (secure-log) Begin------------------------

    myuser => root
    ------------
    /bin/su - 1 Times.
    ---------------------- Sudo (secure-log) End-------------------------

With that said it's now time to move on to the actual "web server" side
of things, the following changes are all personal preference but do help
increase security.

Apache 2 changes
----------------

These changes are made to the following conf file on a Debian server.

    /etc/apache2/apache2.conf

Only show minimal information in headers.

.. code:: apache

    ServerTokens Prod

Don't include server version in server-generated pages.

.. code:: apache

    ServerSignature Off

Disable the icons alias that FancyIndexed directory listings use.

.. code:: apache

    #Alias /icons/ "/var/www/icons/"

The following change will need to be done to your vhosts too, it
disallows users from browsing your directory structures when no index
file is present.

.. code:: apache

    Options -Indexes

Restart apache and you're good.

.. code:: bash

    sudo /etc/init.d/apache2 restart

PHP
---

The following changes help to hide and secure PHP. You need to make them
in the following file.

    /etc/php5/apache2/php.ini

Turn off PHP exposure.

.. code:: ini

    expose_php = Off

Preventing session fixation. For more information on this please see
`this paper`_.

.. _this paper: http://www.acros.si/papers/session_fixation.pdf

.. code:: ini

    session.use_only_cookies = 1
    session.cookie_httponly = 1
    session.use_trans_sid = 0

Once changed simply restart Apache.

.. code:: bash

    sudo /etc/init.d/apache2 restart

Round up
--------

There are many more ways to secure a server but I hope these changes
help you secure yours.
