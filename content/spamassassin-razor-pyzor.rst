SpamAssassin + Razor + Pyzor on Debian 6/Ubuntu
###############################################
:date: 2011-09-22 19:17
:author: kura
:category: tutorials
:tags: email, mail, postfix, pyzor, razor, spam, spamassassin
:slug: spamassassin-razor-pyzor

.. contents::

This is part 4 of my series on configuring a mail server, please see
`part one`_, `part two`_ and `part three`_ if you're not familiar with
them.

.. _part one: http://syslog.tv/2011/09/15/postfix-dovecot-imapimaps-sasl-maildir/
.. _part two: http://syslog.tv/2011/09/16/postfix-spamassassin-clamav-procmail/
.. _part three: http://syslog.tv/2011/09/17/postfix-dk-dkim-spf/

The content of this article was written to work with the previous three
articles but should work on any SpamAssassin set-up.

Razor
-----

First off we need to install Razor.

.. code:: bash

    sudo apt-get install razor

Now we need to run three commands to register and configure Razor.

.. code:: bash

    sudo razor-admin -home=/etc/spamassassin/.razor -register
    sudo razor-admin -home=/etc/spamassassin/.razor -create
    sudo razor-admin -home=/etc/spamassassin/.razor -discover

These 3 commands should be pretty self explanatory, they register Razor,
create it's configuration and discover the Razor servers.

Pyzor
-----

Now we'll install Pyzor.

.. code:: bash

    sudo apt-get install pyzor

Now we also need to tell Pyzor to discover it's servers.

.. code:: bash

    sudo pyzor discover

SpamAssassin
------------

Add the following lines to the end of **/etc/spamassassin/local.cf**

.. code:: bash

    sudo razor_config /etc/spamassassin/.razor/razor-agent.conf
    sudo pyzor_options --homedir /etc/spamassassin

Finally we restart SpamAssassin

.. code:: bash

    sudo /etc/init.d/spamassasin restart

And we're all done.

`« Part 3 - Postfix + DK (DomainKeys) + DKIM + SPF`_

.. _« Part 3 - Postfix + DK (DomainKeys) + DKIM + SPF: http://syslog.tv/2011/09/22/spamassassin-razor-pyzor/
