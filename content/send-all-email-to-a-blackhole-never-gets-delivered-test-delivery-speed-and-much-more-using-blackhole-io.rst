Send all email to a blackhole (never gets delivered), test delivery speed and much more using blackhole.io
##########################################################################################################
:date: 2012-06-26 23:05
:author: kura
:category: howto, mail
:tags: blackhole, blackhole.io, email, mail
:slug: send-all-email-to-a-blackhole-never-gets-delivered-test-delivery-speed-and-much-more-using-blackhole-io

I have built and released an open-source email server in the past for
testing send rates and speeds, this project was called SimpleMTA and is
available `here`_.

.. _here: https://syslog.tv/simplemta/

Recently I have rebuilt this project for an internal project at work
using the `Tornado framework`_. Sadly this project as a whole cannot be
released but a version of this code will be released in the near future.

.. _Tornado framework: http://www.tornadoweb.org/

Until that is released I have launched a new service called
`blackhole.io`_

.. _blackhole.io: http://blackhole.io

What is blackhole.io?
---------------------

blackhole.io is a completely open mail relay that forgets anything that
is sent to it, meaning there is no auth requirements and no storage of
email data within the service. Literally anyone can send anything to it
and have it never get delivered.

You can even send commands out of order, meaning you can call the DATA
command without ever using HELO, MAIL FROM or RCPT TO.

What can I use it for?
----------------------

Honestly, anything. I have spoken to a few people and have come up with
a few use cases but I'm sure there will be more:

1. You want to work on production data but do not want to accidentally send an email to real users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is bit of a nasty situation to be in but, it happens every so
often. Sure, you can spend time anonymising all of your user data (and
that is the best thing to do), but sometimes you don't have time or you
cannot be 100% sure that you have got it all.

If you application is written in such a way that changing it's SMTP
settings will work across the whole application then you can simply
point the SMTP host to "blackhole.io" and ensure that any outgoing
emails will go to the blackhole and thus, never reach real people.

2. Testing the speed of your email sends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Maybe you're writing your own mail platform and want to see how fast you
can really send email. blackhole.io is a very fast server and, because
it does no real validation and has no data storage it has an extremely
low CPU and memory footprint. You can fire a vast amount of mail at it
and it should not feel it in the slightest.

I have managed to send over 150,000 emails within an 10 minute period
and it didn't feel any stress.

3. Integration tests
~~~~~~~~~~~~~~~~~~~~

This one was pointed out by a colleague of mine - you have a system,
you've done your basic testing and unit testing but you want to test
integration. blackhole.io allows you to do this, you can send all of
your test email data at the service to test your SMTP outbound
connections.

In a future release of blackhole.io you will be able to create a free
account and set-up logging of mail, allowing you to log the from address
and subject line and possibly some custom header data, but this feature
is not available currently.

Outro
-----

I hope some people will find this service useful, let me know if you use
it and what you think of it.
