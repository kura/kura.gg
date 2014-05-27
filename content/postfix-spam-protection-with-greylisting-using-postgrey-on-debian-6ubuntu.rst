Postfix spam protection with greylisting using Postgrey on Debian 6/Ubuntu
##########################################################################
:date: 2011-09-24 21:29
:author: kura
:category: tutorials
:tags: debian, email, greylist, mail, postfix, postgrey, spam, ubuntu
:slug: postfix-spam-protection-with-greylisting-using-postgrey-on-debian-6ubuntu

.. contents::
    :backlinks: none

A simple yet effective method for protecting your mail server from spam
is to use greylisting. In simple terms, when an email is received the
server will temporarily reject it with a 450 response code claiming that
the server is busy, the sending server should then attempt to try to
deliver at a later point in time, if enough time has passed the
recipient server will then accept the incoming mail and whitelist the
send address for a period of time.

This is effective because most spam servers are configured not to retry
the send whereas real mail servers generally will retry. This sadly does
not protect against spam coming from comprised mail servers or accounts
like on Hotmail.com.

Installation
------------

.. code:: bash

    sudo apt-get install postgrey

Configuring Postgrey
--------------------

By default Postgrey runs on *127.0.0.1:60000*, which is the local
loopback interface so it is not exposed to the outside world.

If you open up **/etc/default/postgrey** and modify the *POSTGREY_OPTS*
line you can configure how long to grey list for.

.. code:: bash

    --delay=60

would greylist the sending server for 60 seconds (the default value is
300 second, 5 minutes), if a retry was attempted after 60 seconds the
sender would automatically become whitelisted, by default this sender is
whitelisted for 35 days but can be changed using the *--max-age* option

.. code:: bash

    --max-age=10

would whitelist for 10 days.

They can be combined as below.

.. code:: bash

    POSTGREY_OPTS="--inet=127.0.0.1:60000 --delay=60 --max-age=10"

Once you're satisfied save and closed and restart Postgrey.

.. code:: bash

    sudo /etc/init.d/postgrey restart

Configuring Postfix
-------------------

Open up **/etc/postfix/main.cf** and add the following within
*smtpd_receipient_restrictions*

::

    check_policy_service inet:127.0.0.1:60000

This is best added after your SASL and sender domain checks but before
SPF and blacklists, see below for an example

::

    smtpd_recipient_restrictions = permit_mynetworks,
        permit_sasl_authenticated,
        reject_unauth_destination,
        reject_unknown_sender_domain,
        check_policy_service inet:127.0.0.1:60000

Now reload Postfix

.. code:: bash

    sudo /etc/init.d/postfix reload

Testing
-------

Now if you tail your mail.log you will see your Postgrey instance
rejecting incoming email like below.

::

    Sept 24 22:26:18 heimdall postfix/smtpd[4256]: NOQUEUE: reject: RCPT from example.com[xxx.xxx.xxx.xxx]: 450: Recipient address rejected: Greylisted for 300 seconds (see http://isg.ee.ethz.ch/tools/postgrey/help/spammed.com.html); from=to=proto=ESMTP helo=<example.com>
