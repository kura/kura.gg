Debian Wheezy encrypted Maildir using encfs
###########################################
:date: 2015-01-26 21:25
:author: kura
:category: tutorials
:tags: debian, wheezy, postfix, dovecot, mail, encrypted
:slug: debian-wheezy-encrypted-maildir-using-encfs

.. contents::

This is really a follow up article to `one I wrote earlier this year
</debian-wheezy-tls-mailserver-with-mysql-clamav-domainkeys-dkim-spf-solr-imap-search/>`_
but is really applicable to any similar set-up, with some modifications. The
only configuration similarity this requires is that mail for all users is
stored on the filesystem in the same place, rather than to separate locations
i.e. each user having ~/.Maildir.

EncFS
=====

.. code-block:: bash

    sudo apt-get install encfs

Once installed, you'll need to make a directory for encrypted and decrypted
mail to live.

.. code-block:: bash

    sudo mkdir /var/mail/encrypted /var/mail/decrypted

You'll need to set up permissions so your mail user can access the fuse device
and the new directories.

For me, this user and group are called *vmail* but yours may be different.

.. code-block:: bash

    sudo chgrp mail /var/mail/decrypted
    sudo g+rw /var/mail/decrypted
    sudo usermod -a -g fuse vmail
    sudo chgrp fuse /dev/fuse
    sudo chmod g+rw /dev/fuse

Next you need to build the encrypted volume.

.. code-block:: bash

    sudo encfs /var/mail/encrypted /var/mail/decrypted --public

When prompted for an option, choose **p** for paranoid mode.

Finally, **don't forget to choose a good, strong passphrase. Really this
should be a phrase, not a password.** It'll be needed each time you unmount the
volume or reboot the machine.

It is important to include the `--public` argument, this forces Fuse to be more
Linux multi-user friendly, it's kind of a bad option to use due to it being a
hammer option. You could always try to do this properly but for me I think it's
fine in this case.

If you unmount the volume for any reason, you can remount it using the same
command that was used to create the volume.

Now you'll just want to copy over your existing mail in to `/var/mail/decrypted/`.

Dovecot
=======

The final step to getting this to work is to tell Dovecot to use this mail
location.

With my setup there are two pleces to modify this, the first is
`/etc/dovecot/conf.d/10-mail.conf`. It's really hard to tell you what this
exact value should be, due to set-ups being different but if you followed my
previous article, it'll look like below.

.. code-block:: none

    mail_location = maildir:/var/mail/decrypted/vhosts/%d/%n/maildir

The other file that is likely to need modification is
`/etc/dovecot/conf.d/auth-sql.conf.ext`

.. code-block:: none

    userdb {
        driver = static
        args = uid=vmail gid=vmail home=/var/spool/mail/decrypted/vhosts/%d/%n/maildir
    }

That's everything you technically need to do, just restart Dovecot.

.. code-block:: bash

    sudo /etc/init.d/dovecot restart

Tomcat/Solr
===========

If you use Solr for IMAP SEARCH, you'll just want to move that index inside of
the new directory.

.. code-block:: bash

    sudo /etc/init.d/tomcat6 stop
    sudo mv /var/lib/solr /var/mail/decrypted/

You'll need to tell Solr to get it's data from this directory, this is done in
`/etc/solr/conf/solrconfig.xml`

.. code-block:: xml

    <dataDir>/var/mail/decrypted/solr</dataDir>

Start tomcat again.

.. code-block:: bash

    sudo /etc/init.d/tomcat6 start

And finally, it's always good when you mess with Solr's indexes like this to
run optimize task.

.. code-block:: bash

    curl https://localhost:8080/solr/update?optimize=true

init.d
======

Something to remember is that encfs will not mount on it's own, that's the
entire point of doing this. This means that Postfix, Dovecot, Solr etc will
not have any data to read on a server reboot.

I just "fix" this by forcing the init scripts for those processes to look for
the mount point and fail if it's not there.

In each init script for Postfix, Dovecot, Tomcat6 and anything else that will
try to read data from /var/mail/decrypted you'll want to find where
`/lib/lsb/init-functions` is loaded and a check after it.

.. code-block:: bash

    if ! mount | grep "on /var/mail/decrypted" > /dev/null
    then
        log_daemon_msg "/var/mail/decrypted not mounted";
        log_end_msg 1;
        exit 1;
    fi

It'll look similar to below if you put it in the right place.

.. code-block:: bash

    # Define LSB log_* functions.
    # Depend on lsb-base (>= 3.0-6) to ensure that this file is present.
    . /lib/lsb/init-functions

    if ! mount | grep "on /var/mail/decrypted" > /dev/null
    then
        log_daemon_msg "/var/mail/decrypted not mounted";
        log_end_msg 1;
        exit 1;
    fi
