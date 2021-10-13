Postfix + SpamAssassin + ClamAV + Procmail on Debian 6/Ubuntu
#############################################################
:date: 2011-09-16 21:28
:author: kura
:category: tutorials
:tags: clamav, clamsmtp, debian, email, mail, postfix, procmail, spamassassin, ubuntu
:slug: postfix-spamassassin-clamav-procmail

.. contents::
    :backlinks: none

This is part 2 of my series on mail servers on Debian 6/Ubuntu 10.04, it
should work on other versions of each though. `Part 1 is available here </2011/09/15/postfix-dovecot-imapimaps-sasl-maildir/>`_.

SpamAssassin
------------

First off we'll get SpamAssassin installed and configured.

.. code-block:: bash

    sudo apt-get install spamassassin

We'll be configuring SpamAssassin as a daemon that Postfix interfaces
with using **spamc**.

SpamAssassin on Debian and Ubuntu runs as root which is NOT a good thing
so we'll need to make some changes.

We'll add a group called **spamd** with GID**5001**.

.. code-block:: bash

    sudo groupadd -g 5001 spamd

Next we add a user spamd with UID **5001** and add it to the spamd
group, as well as set it's home directory as **/var/lib/spamassassin**
and make sure it has no shell access or SSH access.

.. code-block:: bash

    sudo useradd -u 5001 -g spamd -s /usr/sbin/nologin -d /var/lib/spamassassin spamd

Now we make that users home directory.

.. code-block:: bash

    sudo mkdir /var/lib/spamassassin

And finally change the permissions of that directory so the spamd user
can write there.

.. code-block:: bash

    sudo chown spamd:spamd /var/lib/spamassassin

Next up we have to enabled the daemon and configure it. Open up
**/etc/default/spamassassin** and make the following changes.

.. code-block:: bash

    ENABLED=1
    CRON=1

This will actually allow the spamassassin daemon to start. We also need
to configure it's new home directory and more.

.. code-block:: bash

    SAHOME="/var/lib/spamassassin/"
    OPTIONS="--create-prefs --max-children 5 --username spamd --helper-home-dir ${SAHOME} -s /var/log/spamd.log"
    PIDFILE="${SAHOME}spamd.pid"

Next up we'll make some changes to **/etc/spamassassin/local.cf**

::

    rewrite_header Subject ***** SPAM _SCORE_ *****
    report_safe 1

    use_bayes 1
    use_bayes_rules 1
    bayes_auto_learn 1

These changes will rewrite the email subject to show that it is spam and
add the spam score too, like this ***** SPAM 6.0 *****,
report_safe will attach the spam email as a plain text attachment to
the email to filter out any bad stuff. The 3 bayes options enabled the
Bayesian classifier and enable auto learn functionality. For more info
on Bayesian cliassifier, go `here <https://en.wikipedia.org/wiki/Bayesian_spam_filtering>`_.

SpamAssassin is now configured but Postfix doesn't know how to talk to
it, we'll configure that later. Now on to...

ClamAV
------

.. code-block:: bash

    sudo apt-get install clamsmtp clamav-freshclam

Once installed you'll have an SMTP wrapper for ClamAV installed and a
daemon that automatically updates your anti-virus database.

Open up **/etc/clamsmtpd.conf** and make the following changes

::

    OutAddress: 10026

and

::

    Listen: 127.0.0.1:10025

Now we move on to...

Procmail
--------

.. code-block:: bash

    sudo apt-get install procmail

Now we need to create **/etc/procmailrc** and add the following to it

.. code-block:: bash

    DROPPRIVS=YES
    ORGMAIL=$HOME/Maildir
    MAILDIR=$ORGMAIL
    DEFAULT=$ORGMAIL

This tells Procmail to deliver email to your Maildir folder instead of
/var/mail/

And now to glue it all together!

Postfix
-------

Open up **/etc/postfix/main.cf** and add the following lines

::

    content_filter = scan:127.0.0.1:10025
    receive_override_options = no_address_mappings

This tells Postfix to scan content using ClamAV which is listening on
port 10025.

Now add the following to tell Postfix to deliver mail locally using
Procmail.

::

    mailbox_command = procmail -a "$EXTENSION"

Next open up **/etc/postfix/master.cf** and change

::

    smtp inet n - - - - smtpd

to

::

    smtp inet n - - - - smtpd
        -o content_filter=spamassassin

Then add the following lines to the end of the file

::

    scan unix - - n - 16 smtp
        -o smtp_send_xforward_command=yes

    127.0.0.1:10026 inet n - n - 16 smtpd
        -o content_filter=
        -o receive_override_options=no_unknown_recipient_checks,no_header_body_checks
        -o smtpd_helo_restrictions=
        -o smtpd_client_restrictions=
        -o smtpd_sender_restrictions=
        -o smtpd_recipient_restrictions=permit_mynetworks,reject
        -o mynetworks_style=host
        -o smtpd_authorized_xforward_hosts=127.0.0.0/8

    spamassassin unix - n n - - pipe
        user=spamd argv=/usr/bin/spamc -f -e
        /usr/sbin/sendmail -oi -f ${sender} ${recipient}

These changes tell Postfix to talk to ClamAV and SpamAssassin.

Finally
-------

.. code-block:: bash

    sudo /etc/init.d/spamassassin restart
    sudo /etc/init.d/clamsmtp restart
    sudo /etc/init.d/postfix restart

That should be everything done, good luck!

`« Part 1 - Postfix + Dovecot (IMAP/IMAPS) + SASL + Maildir`_
 `Part 2 - Postfix + DK (DomainKeys) + DKIM + SPF »`_

.. _« Part 1 - Postfix + Dovecot (IMAP/IMAPS) + SASL + Maildir: /2011/09/15/postfix-dovecot-imapimaps-sasl-maildir/
.. _Part 2 - Postfix + DK (DomainKeys) + DKIM + SPF »: /2011/09/17/postfix-dk-dkim-spf/
