Postfix + SpamAssassin + ClamAV + Procmail on Debian 6/Ubuntu
#############################################################
:date: 2011-09-16 21:28
:author: kura
:category: tutorials
:tags: clamav, clamsmtp, debian, email, mail, postfix, procmail, spamassassin, ubuntu
:slug: postfix-spamassassin-clamav-procmail

This is part 2 of my series on mail servers on Debian 6/Ubuntu 10.04, it
should work on other versions of each though. `Part 1 is available here <http://syslog.tv/2011/09/15/postfix-dovecot-imapimaps-sasl-maildir/>`_.

SpamAssassin
------------

First off we'll get SpamAssassin installed and configured.

    apt-get install spamassassin

We'll be configuring SpamAssassin as a daemon that Postfix interfaces
with using **spamc**.

SpamAssassin on Debian and Ubuntu runs as root which is NOT a good thing
so we'll need to make some changes.

We'll add a group called **spamd** with GID**5001**.

    groupadd -g 5001 spamd

Next we add a user spamd with UID **5001** and add it to the spamd
group, as well as set it's home directory as **/var/lib/spamassassin**
and make sure it has no shell access or SSH access.

    useradd -u 5001 -g spamd -s /usr/sbin/nologin -d /var/lib/spamassassin spamd

Now we make that users home directory.

    mkdir /var/lib/spamassassin

And finally change the permissions of that directory so the spamd user
can write there.

    chown spamd:spamd /var/lib/spamassassin

Next up we have to enabled the daemon and configure it. Open up
**/etc/default/spamassassin** and make the following changes.

::

    ENABLED=1
    CRON=1

This will actually allow the spamassassin daemon to start. We also need
to configure it's new home directory and more.

::

    SAHOME="/var/lib/spamassassin/"
    OPTIONS="--create-prefs --max-children 5 --username spamd --helper-home-dir ${SAHOME} -s /var/log/spamd.log"
    PIDFILE="${SAHOME}spamd.pid"

Next up we'll make some changes to **/etc/spamassassin/local.cf**

::

    rewrite\_header Subject \*\*\*\*\* SPAM \_SCORE\_ \*\*\*\*\*
    report\_safe 1

    use\_bayes 1
    use\_bayes\_rules 1
    bayes\_auto\_learn 1

These changes will rewrite the email subject to show that it is spam and
add the spam score too, like this \*\*\*\*\* SPAM 6.0 \*\*\*\*\*,
report\_safe will attach the spam email as a plain text attachment to
the email to filter out any bad stuff. The 3 bayes options enabled the
Bayesian classifier and enable auto learn functionality. For more info
on Bayesian cliassifier, go `here <http://en.wikipedia.org/wiki/Bayesian_spam_filtering>`_.

SpamAssassin is now configured but Postfix doesn't know how to talk to
it, we'll configure that later. Now on to...

ClamAV
------

    apt-get install clamsmtp clamav-freshclam

Once installed you'll have an SMTP wrapper for ClamAV installed and a
daemon that automatically updates your anti-virus database.

Open up **/etc/clamsmtpd.conf** and make the following changes

    OutAddress: 10026

and

    Listen: 127.0.0.1:10025

Now we move on to...

Procmail
--------

    apt-get install procmail

Now we need to create **/etc/procmailrc** and add the following to it

::

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

    content\_filter = scan:127.0.0.1:10025
    receive\_override\_options = no\_address\_mappings

This tells Postfix to scan content using ClamAV which is listening on
port 10025.

Now add the following to tell Postfix to deliver mail locally using
Procmail.

    mailbox\_command = procmail -a "$EXTENSION"

Next open up **/etc/postfix/master.cf** and change

    smtp inet n - - - - smtpd

to::

    smtp inet n - - - - smtpd
        -o content\_filter=spamassassin

Then add the following lines to the end of the file::

    scan unix - - n - 16 smtp
        -o smtp\_send\_xforward\_command=yes

    127.0.0.1:10026 inet n - n - 16 smtpd
        -o content\_filter=
        -o receive\_override\_options=no\_unknown\_recipient\_checks,no\_header\_body\_checks
        -o smtpd\_helo\_restrictions=
        -o smtpd\_client\_restrictions=
        -o smtpd\_sender\_restrictions=
        -o smtpd\_recipient\_restrictions=permit\_mynetworks,reject
        -o mynetworks\_style=host
        -o smtpd\_authorized\_xforward\_hosts=127.0.0.0/8

    spamassassin unix - n n - - pipe
        user=spamd argv=/usr/bin/spamc -f -e
        /usr/sbin/sendmail -oi -f ${sender} ${recipient}

These changes tell Postfix to talk to ClamAV and SpamAssassin.

Finally
-------

::

    /etc/init.d/spamassassin restart
    /etc/init.d/clamsmtp restart
    /etc/init.d/postfix restart

That should be everything done, good luck!

`« Part 1 - Postfix + Dovecot (IMAP/IMAPS) + SASL + Maildir`_
 `Part 2 - Postfix + DK (DomainKeys) + DKIM + SPF »`_

.. _« Part 1 - Postfix + Dovecot (IMAP/IMAPS) + SASL + Maildir: http://syslog.tv/2011/09/15/postfix-dovecot-imapimaps-sasl-maildir/
.. _Part 2 - Postfix + DK (DomainKeys) + DKIM + SPF »: http://syslog.tv/2011/09/17/postfix-dk-dkim-spf/
