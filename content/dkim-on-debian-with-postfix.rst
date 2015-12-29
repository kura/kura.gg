HOWTO: DKIM with Postfix on Debian
##################################
:date: 2010-01-11 20:53
:author: kura
:category: tutorials
:tags: debian, dkim, howto, mail, postfix
:slug: dkim-on-debian-with-postfix

*There is a much newer article on this subject `here`_ and covers
DomainKeys and DKIM.*

.. _here: /2011/09/17/postfix-dk-dkim-spf/

Mail and mail servers have always been my forté if I'm to be honest, my
home mail server has been spam free for years now, nothing really gets
past due to my love of all things installable and configurable.

Several months ago I started a new job and after a few weeks I was
tasked with getting DKIM signing to work on our mail platform, DKIM was
semi-new to me, I'd never bothered with anything but SPF before so I
figured I'd give it a shot.

At work our servers are Debian based but are the evil that is Ubuntu,
strangely though I was able to find an Ubuntu specific article that
wasn't absolute rubbish, which surprised me no end. I was able to get
dkim-milter working with Postfix and signing emails first time round.
Google was failing to match against our DNS records but after some
repeat changes I was able to get it working.

Debian was a completely different kettle of fish.

I'll have to go through a bit of the background to my problem before the
actual installation tutorial. I had everything installed and running but
dkim-filter was refusing to start correctly, Postfix couldn't connect to
it and no emails could be signed. After a lot of banging my head against
the desk I decided to try dkimproxy, I had the same issues with this
too. Then I spotted opendkim which used the same config as dkim-filter
but this time actually worked. I'm not sure what exactly is wrong with
the dkim-filter package, I've noticed a few people writing posts about
it but opendkim saved me so I'll stick with it.

First off I'm going to assume you have Postfix installed and running, if
you don't there are plenty of articles on Google for how to get it
running.

First step is to install opendkim.

.. code:: bash

    sudo apt-get install opendkim

Leave the install process to complete, we'll configure it later, first
we'll make the public and private keys required for signing.

.. code:: bash

    openssl genrsa -out private.key 1024
    openssl rsa -in private.key -out public.key -pubout -outform PEM
    sudo /etc/mail/
    sudo cp private.key /etc/mail/dkim.key

So that's the key sorted, now we'll configure opendkim.

First open **/etc/opendkim.conf** and put the following in, replacing
the _DOMAIN_ with your domain name.

::

    # Log to syslog
    Syslog yes
    # Required to use local socket with MTAs that access the socket as a non-
    # privileged user (e.g. Postfix)
    UMask 002

    # Sign for example.com with key in /etc/mail/dkim.key using
    # selector '2007' (e.g. 2007._domainkey.example.com)
    Domain _DOMAIN_
    KeyFile /etc/dkim/private.key
    Selector mail

    # Commonly-used options; the commented-out versions show the defaults.
    #Canonicalization simple
    #Mode sv
    #SubDomains no
    #ADSPDiscard no

Set a custom selector if you want.

Next we open up **/etc/default/opendkim** and change it to the
following:

.. code:: bash

    # Command-line options specified here will override the contents of
    # /etc/opendkim.conf. See opendkim(8) for a complete list of options.
    #DAEMON_OPTS=""
    #

    # Uncomment to specify an alternate socket

    # Note that setting this will override any Socket value in opendkim.conf

    #SOCKET="local:/var/run/opendkim/opendkim.sock" # default
    #SOCKET="inet:54321" # listen on all interfaces on port 54321
    SOCKET="inet:12345@localhost" # listen on loopback on port 12345
    #SOCKET="inet:12345@192.0.2.1" # listen on 192.0.2.1 on port 12345

That's opendkim all configured, start the daemon with

.. code:: bash

    sudo /etc/init.d/opendkim start

Next we need to modify Postfix to tell it to use opendkim to sign
emails. Lets open up **/etc/postfix/main.cf**

Place the following as the end of that file

::

    milter_default_action = accept
    milter_protocol = 6
    smtpd_milters = inet:localhost:12345
    non_smtpd_milters = inet:localhost:12345

That's Postfix configured, we'll reload it once the DNS is configured.

How you configured your DNS is up to you, you will need to add the
following 2 new records

::

    _domainkey.DOMAIN.TLD. IN TXT "t=y; o=-;" SELECTOR._domainkey.DOMAIN.TLD. IN TXT "k=rsa; t=y; p=YOUR_PUBLIC_KEY_HERE"

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

::

    MIGfMWGwregWREGREwgERGREGerg [...snip...]
    plp1ruZ66Bgrewhg43y634567gewrgB

Now we simply reload the Postfix config with **/etc/init.d/postfix
reload**

Now you can send test mails once you're sure DNS changes have
propagated. You will see any errors in **/var/log/mail.log**.
