HOWTO: DomainKeys with Postfix on Debian/Ubuntu
###############################################
:date: 2010-02-12 19:08
:author: kura
:category: tutorials
:tags: debian, dkim, domainkeys, howto, mail, postfix, ubuntu
:slug: howto-domainkeys-with-postfix-on-debian-ubuntu

**I have written a much newer, clearer and better article on DomainKeys
signing email `here`_.**

.. _here: https://kura.io/2011/09/17/postfix-dk-dkim-spf/

About
-----

This guide is a sister to another guide I wrote a while back about how
to use DomainKeys Identified Mail (DKIM) with Postfix on Debian, which
can be read here - `https://kura.io/2010/01/11/dkim-on-debian-with-postfix/`_.

.. _`https://kura.io/2010/01/11/dkim-on-debian-with-postfix/`: https://kura.io/2010/01/11/dkim-on-debian-with-postfix/

DomainKeys is an older implementation than DKIM, DKIM is a merge of
DomainKeys and Identified Mail. Both DomainKeys and DKIM are used so
having both configured is a good idea.

Getting started
---------------

Lets start off by installing the dk-filter

.. code:: bash

    sudo apt-get install dk-filter

Once installed you can can create a public and private key set using the
commands below, if you're already using DKIM you can skip this step and
just use your already existing key.

.. code:: bash

    openssl genrsa -out private.key 1024
    openssl rsa -in private.key -out public.key -pubout -outform PEM
    sudo mkdir /etc/mail
    sudo cp private.key /etc/mail/dk.key

So that's the key sorted, now we'll configure dk-filter.

Open the following file

    /etc/default/dk-filter

You should see something like this

.. code:: bash

    # Sane defaults: log to syslog
    DAEMON_OPTS="-l"
    # Sign for domain.tld with key in /etc/mail/domainkey.key using
    # selector '2007' (e.g. 2007._domainkey.domain.tld)
    DAEMON_OPTS="$DAEMON_OPTS -d domain.tld -s
    /etc/mail/domainkey.key -S 2007"
    # See dk-filter(8) for a complete list of options
    #
    # Uncomment to specify an alternate socket
    #SOCKET="/var/run/dk-filter/dk-filter.sock" # default
    #SOCKET="inet:54321" # listen on all interfaces on port 54321
    #SOCKET="inet:8892@localhost" # listen on loopback on port 8892
    #SOCKET="inet:12345@192.0.2.1" # listen on 192.0.2.1 on port 12345

You will need to modify the DAEMON_OPTS, changing the domain (-d), key
file and location (-s) and selector (-S), an example is below

.. code:: bash

    # Sane defaults: log to syslog
    DAEMON_OPTS="-l"
    # Sign for domain.tld with key in /etc/mail/domainkey.key using
    # selector '2007' (e.g. 2007._domainkey.domain.tld)
    DAEMON_OPTS="$DAEMON_OPTS -d syslog.tv -s /etc/mail/dk.key -S mail"
    # See dk-filter(8) for a complete list of options
    #
    # Uncomment to specify an alternate socket
    #SOCKET="/var/run/dk-filter/dk-filter.sock" # default
    #SOCKET="inet:54321" # listen on all interfaces on port 54321
    #SOCKET="inet:8892@localhost" # listen on loopback on port 8892
    SOCKET="inet:12345@localhost" # listen on loopback on port 12345

You should notice that I specifically told the daemon to run on loopback
on port 12345, you should do the same, if you already have something
running on that port (like DKIM, which uses the same port in my other
guide,) you should set this to something different, like 12346.

On Debian Sid I had problems with DAEMON_OPTS, for some reason the
second DAEMON_OPTS was not overwriting and including the first, so I
modified it to look like this

.. code:: bash

    # Sane defaults: log to syslog
    #DAEMON_OPTS="-l"
    # Sign for domain.tld with key in /etc/mail/domainkey.key using
    # selector '2007' (e.g. 2007._domainkey.domain.tld)
    DAEMON_OPTS="-l -d syslog.tv -s /etc/mail/dk.key -S mail"

The problem meant that when the daemon was actually started, it would
not know which domain, key or selector to use, doing the above solved
this issue for me.

Now that dk-filter is configured, we can start it

.. code:: bash

    sudo /etc/init.d/dk-filter start

Configuring Postfix
-------------------

Next we need to modify Postfix to tell it to use dk-filter to sign
emails. Lets open up

    /etc/postfix/main.cf

Place the following as the end of that file

::

    milter_default_action = accept
    milter_protocol = 6
    smtpd_milters = inet:localhost:12345
    non_smtpd_milters = inet:localhost:12345

If you've already got this defined you simple append to the end,
separating with commas

::

    milter_default_action = accept
    milter_protocol = 6
    smtpd_milters = inet:localhost:12345, inet:localhost:12346
    non_smtpd_milters = inet:localhost:12345, inet:localhost:12346

That's Postfix configured, we'll reload it once the DNS is configured.

Configuring the DNS
-------------------

How you configured your DNS is up to you, you will need to add the
following 2 new records

    _domainkey.DOMAIN.TLD. IN TXT "t=y; o=-;"

    SELECTOR._domainkey.DOMAIN.TLD. IN TXT "k=rsa; t=y; p=YOUR_PUBLIC_KEY_HERE"

Replace the instances of **DOMAIN.TLD** with your actual mail domain
name in both records, **SELECTOR** was configured in to opendkim
earlier, in my example I used **mail**.

Your key will be called public.key, we created both public and private
keys earlier. You only need to add the actual key from between the BEGIN
and END lines, e.g. my test one below

::

    -----BEGIN PUBLIC KEY-----
    MIGfMWGwregWREGREwgERGREGergerDGdEPzFCAdYnf1Z9nRtfTqwP/mcdGg
    NmbY11tCtwwFMu8/qEQwaK/Nc61q0D/z7NYwlsPFi08lnVSHGrewherh5630n
    F6S0z961h6li/pOHiJy/l2ehnenhehO3d/NmATY90WlpEDmnlVAMTYgALBFJplp
    1ruZ66Bgrewhg43y634567gewrgB
    -----END PUBLIC KEY-----

Becomes

:

    MIGfMWGwregWREGREwgERGREGerg [...snip...] plp1ruZ66Bgrewhg43y634567gewrgB

Now we simply reload the Postfix config with

.. code:: bash

    sudo /etc/init.d/postfix reload

Now you can send test mails once you're sure DNS changes have
propagated. You will see any errors in **/var/log/mail.log**.

