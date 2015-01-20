Block yourself from emailing someone with Postfix
#################################################
:date: 2015-01-20 23:38
:author: kura
:category: tutorials
:tags: postfix, smtp
:slug: block-yourself-from-emailing-someone-with-postfix

.. contents::

I think most of us have been in a position where we really shouldn't continue
communicating with someone or contact that person when drunk... You know what I
mean, ex relationships etc (it happens.)

With Postfix you can block yourself from emailing that person again, which is
quite useful.

In `/etc/postfix/main.cf` add make the start of your `smtpd_recipient_restrictions`
look like below.

.. code::

    smtpd_recipient_restrictions =
        check_recipient_access hash:/etc/postfix/recipient_access,

Create a new file `/etc/postfix/recipient_access` and add the email address you
wish to block, the word `REJECT` in capitals and optionally; a  reason. Example
below.

.. code::

    test@example.com REJECT Don't be silly... You're probably drunk.

For every address you wish to block yourself from emailing, simply add them on
a new line.

You can see the email is blocked from being sent in `/var/log/mail.log`.

.. code::

    NOQUEUE: reject: RCPT from 123.123.123.123: 554 5.7.1 <test@example.com>: Recipient address rejected: Don't be silly... You're probably drunk.; from=<me@domain.tld> to=<test@example.com> proto=ESMTP helo=<[123.123.123.123]>


Each time you change the file, you need to generate a new hashed version and
reload Postfix.

.. code:: bash

    sudo postmap hash:/etc/postfix/recipient_access
    sudo /etc/init.d/postfix reload
