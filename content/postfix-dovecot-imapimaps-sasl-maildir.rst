Postfix + Dovecot (IMAP/IMAPS) + SASL + Maildir on Debian 6/Ubuntu
##################################################################
:date: 2011-09-15 23:04
:author: kura
:category: tutorials
:tags: debian, dovecot, email, imap, imaps, mail, maildir, postfix, sasl, ubuntu
:slug: postfix-dovecot-imapimaps-sasl-maildir

This guide is part 1 of what I plan will be a couple of guides that take
you through installing a base mail system, SpamAssassin, DKIM and much
more. Stay tuned.

This guide was written for Debian 6 but should be the same or similar
for Debian 5 and Ubuntu 10.04 and above.

The installation
----------------

.. code:: bash

    sudo apt-get install dovecot-imapd postfix sasl2-bin libsasl2-2 libsasl2-modules

Choose "Internet site" when prompted and enter the fully qualified name
of your server.

Once all this is done installing we'll need to make some changes, first
off will be Postfix.

Postfix
-------

Open up **/etc/postfix/main.cf** and add the following to the end of the
file

::

    home_mailbox = Maildir/
    smtpd_sasl_auth_enable = yes
    smtpd_sasl_security_options = noanonymous
    smtpd_sasl_local_domain = $myhostname
    broken_sasl_auth_clients = yes

    smtpd_sender_restrictions = permit_sasl_authenticated,
        permit_mynetworks,

    smtpd_recipient_restrictions = permit_mynetworks,
        permit_sasl_authenticated,
        reject_unauth_destination,
        reject_unknown_sender_domain,

Here we basically tell Postfix to store all email in maildir format in
the user's home directory. We then enable SASL with and tell it to not
allow anonymous auth and, tell it the hostname and enabled broken SASL
auth clients, just in-case.

The next section tells Postfix to allow users to send if they pass SASL
auth or are listed in the allowed networks section.

Finally we set Postfix's recipient rules where we allow our networks,
SASL auth and reject any unauthorised destinations and unknown senders.

Dovecot
-------

Open up **/etc/dovecot/dovecot.conf**

Uncomment the IMAP and IMAPS protocols

::

    protocols = imap imaps

Next we configure the protocols, add the following lines just below the
protocols option

::

    protocol imap {
        listen = *:143
        ssl_listen = *:993/
    }

Search through the file for "*mail_location =*" without the quotes,
make sure it's commented out and add the following below it:

::

    mail_location = maildir:~/Maildir/

Now we need to search down the file and comment out everything within
the "*auth default*" section and add the following below it

::

    auth default {
        mechanisms = plain login
        passdb pam {
        }

        userdb passwd {
        }

        socket listen {
            client {
                path = /var/spool/postfix/private/auth
                mode = 0660
                user = postfix
                group = postfix
            }
        }
    }

Just to explain what we've done, we've enabled IMAP and IMAPS protocols
and configured the ports to be used, both ports are the standard ports.

Next up we configure Dovecot to handle Maildir, just like with Postfix.

And finally we set up our auth mechanism, specifying that it needs to do
so via Postfix.

SASL
----

Open up the following file**/etc/default/saslauthd**, we need to modify
a couple of things. Set START to yes and MECHANISMS to pam.

.. code:: bash

    START=yes
    MECHANISMS="pam"

Due to the fact Postfix will be chrooted we need to make a few system
changes for SASL.

First we remove the default SASL run location.

.. code:: bash

    sudo rm -r /var/run/saslauthd/

Now we make one within the Postfix chroot.

.. code:: bash

    sudo mkdir -p /var/spool/postfix/var/run/saslauthd

Symlink it back to /var/run so things work.

.. code:: bash

    sudo ln -s /var/spool/postfix/var/run/saslauthd /var/run

Change the group for the directory we created.

.. code:: bash

    sudo chgrp sasl /var/spool/postfix/var/run/saslauthd

And finally add the Postfix user to the SASL group.

.. code:: bash

    sudo adduser postfix sasl

Finally
-------

Now we just need to restart our services.

.. code:: bash

    sudo /etc/init.d/dovecot restart
    sudo /etc/init.d/postfix restart
    sudo /etc/init.d/saslauthd restart

If all went according to plan normal system users should now be able to
send and receive mail.

`Part 2 - Postfix + SpamAssassin + ClamAV + Procmail »`_

.. _Part 2 - Postfix + SpamAssassin + ClamAV + Procmail »: http://syslog.tv/2011/09/16/postfix-spamassassin-clamav-procmail/
