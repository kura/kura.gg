Postfix + DK (DomainKeys) + DKIM + SPF on Debian 6/Ubuntu
#########################################################
:date: 2011-09-17 18:18
:author: kura
:category: tutorials
:tags: debian, dk, dkim, domainkeys, email, mail, postfix, spf, ubuntu
:slug: postfix-dk-dkim-spf

This is part 3 of my guide to getting a mail server configured with all
the sexy bits to improve deliverability, spam and virus protection.

You can view `part 1 here <http://syslog.tv/2011/09/15/postfix-dovecot-imapimaps-sasl-maildir/>`_ and `part 2 here <http://syslog.tv/2011/09/16/postfix-spamassassin-clamav-procmail/>`_.

The key pair
------------

We need to create a key pair to sign emails with::

.. code:: bash

    openssl genrsa -out private.key 1024
    openssl rsa -in private.key -out public.key -pubout -outform PEM
    sudo mkdir /etc/dk/
    sudo cp private.key /etc/dk/dk.key

Now we can move on to DK and DKIM signing, make sure you keep the public
key for later.

DKIM
----

First we'll need to install an application to sign our emails.

.. code:: bash

    sudo apt-get install dkim-filter

Once installed we need to configure it, open up
**/etc/default/dkim-filter**, modify the file to look like below
replacing <DOMAIN> with the domain you want to sign email from.

.. code:: bash

    DAEMON_OPTS="-l -o X-DomainKeys,DomainKey-Signature"
    DAEMON_OPTS="$DAEMON_OPTS -d <DOMAIN> -k /etc/dk/dk.key -s mail"
    SOCKET="inet:12345@localhost" # listen on loopback on port 12345

We use the **-o** flag to tell the filter to ignore any DomainKeys
headers when signing.

DK (DomainKeys)
---------------

The dk-filter package is not installable from APT on Debian 6 for me,
try to install it using APT

.. code:: bash

    sudo apt-get install dk-filter

If it doesn't work then install it by hand, go to
`http://ftp.us.debian.org/debian/pool/main/d/dk-milter/`_ and download
the .deb file for your architecture. To install it run the command below
replacing <FILE> with the file you downloaded.

.. _`http://ftp.us.debian.org/debian/pool/main/d/dk-milter/`: http://ftp.us.debian.org/debian/pool/main/d/dk-milter/

.. code:: bash

    sudo dpkg -i <FILE>

Now that it's installed we can configure it, open up
**/etc/default/dk-filter**, modify the file to look like below replacing
<DOMAIN> with the domain you want to sign email from.

.. code:: bash

    DAEMON_OPTS="-l -o DKIM-Signature,X-DKIM"
    DAEMON_OPTS="$DAEMON_OPTS -d <DOMAIN> -s /etc/dk/dk.key -S mail"
    SOCKET="inet:12346@localhost" # listen on loopback on port 12346

We use the **-o** flag to tell the filter to ignore any DKIM headers
when signing.

SPF
---

Install with

.. code:: bash

    sudo apt-get install postfix-policyd-spf-python

Postfix
-------

Open up **/etc/postfix/main.cf** and add the following lines to it

::

    milter_default_action = accept
    milter_protocol = 6
    smtpd_milters = inet:localhost:12345 inet:localhost:12346
    non_smtpd_milters = inet:localhost:12345 inet:localhost:12346
    spf-policyd_time_limit = 3600s

This tells Postfix to pass incoming and outgoing email through the DK
and DKIM filters, as well as mail that arrives from the queue, local
commands like sendmail and cleanup. It also sets a time limit on SPF
checks.

Add the following to *smtpd_recipient_restrictions =* it should look
like this

::

    smtpd_recipient_restrictions = permit_mynetworks,

    permit_sasl_authenticated,
    reject_unauth_destination,
    reject_unknown_sender_domain,
    check_policy_service unix:private/policy-spf

Now open up **/etc/postfix/master.cf** and add the following

::

    policy-spf unix - n n - - spawn
        user=nobody argv=/usr/bin/policyd-spf

DNS
---

We need to modify your DNS entries so that DK and DKIM actually work and
we also need to add SPF records.

We need to create 3 TXT records, 1 for SPF and 2 for DK/DKIM.

Creating the SPF record is easy, create a new TXT record called
**<DOMAIN>.** e.g. **syslog.tv.** with the following content. replacing
<IP> with the IP of your mail server.

::

    v=spf1 a mx ip4:<IP>

The DK and DKIM records are a little trickier, first create a TXT record
with the following name **_domainkey.<DOMAIN>.** e.g.
**_domainkey.syslog.tv** with the following content

::

    t=y; o=-

With **t** set to **y** it puts your DK and DKIM in test mode, just
in-case.

Now we need to create a second record called
**mail._domainkey.<DOMAIN>.** e.g. **mail._domainkey.syslog.tv**,
you'll need to copy the contents of the public key file we created
earlier. Open it up and copy everything between **-----BEGIN PUBLIC
KEY-----** and **-----END PUBLIC KEY-----** in to one long line. Once
done put it in the DNS record like below

::

    k=rsa; p=<KEY_CONTENT>

like this

::

    k=rsa; p=MIGfMA0GCSqGSIb3DQE ... snip ... 03hFbY5y2QbQIDAQAB

Finally
-------

.. code:: bash

    sudo /etc/init.d/dk-filter restart
    sudo /etc/init.d/dkim-filter restart
    sudo /etc/init.d/postfix restart

Try send an email to yourself, you should see both DK and DKIM
signatures in the source.

`« Part 2 - Postfix + SpamAssassin + ClamAV + Procmail`_

`Part 4 - SpamAssassin + Razor + Pyzor »`_

.. _« Part 2 - Postfix + SpamAssassin + ClamAV + Procmail: http://syslog.tv/2011/09/16/postfix-spamassassin-clamav-procmail/
.. _Part 4 - SpamAssassin + Razor + Pyzor »: http://syslog.tv/2011/09/22/spamassassin-razor-pyzor/
