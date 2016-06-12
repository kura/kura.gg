Debian Wheezy TLS mailserver with MySQL, ClamAV, DomainKeys, DKIM, SPF and Solr-powered IMAP SEARCH
###################################################################################################
:date: 2015-01-03 19:48
:author: kura
:category: tutorials
:tags: debian, wheezy, postfix, dovecot, clamav, domainkeys, dkim, spf, imap
:slug: debian-wheezy-tls-mailserver-with-mysql-clamav-domainkeys-dkim-spf-solr-imap-search

.. contents::

This mail platform does use a fair amount of memory, the memory usage is ClamAV
and Solr, the latter being used for IMAP SEARCH. I personally use 2 GB.

I'll warn you all now, this is a long article.

SSL
===

.. code-block:: none bash

    sudo openssl genrsa -out /etc/ssl/private/mail.key 4096
    sudo openssl req -new -key /etc/ssl/private/mail.key -out /tmp/mail.csr
    sudo openssl x509 -req -days 365 -in /tmp/mail.csr -signkey /etc/ssl/private/mail.key -out /etc/ssl/certs/mail.crt

MySQL
=====

.. code-block:: none bash

    sudo apt-get install mysql-server

You'll be prompted several times for a password for MySQL during the installation,
just come up with something nice and secure.

The first thing to set-up will be the MySQL database and schema.

.. code-block:: none bash

    mysql -u root -p

Next up, create the database.

.. code-block:: none sql

     CREATE DATABASE mailserver CHARACTER SET utf8 COLLATE utf8_general_ci;

And grant some privileges, you'll need to set a password yourself.

.. code-block:: none sql

    GRANT ALL PRIVILEGES ON mailserver.* TO 'mailuser'@'localhost' IDENTIFIED BY '<PASSWORD_HERE>';
    FLUSH PRIVILEGES;

Next, set up the schema.

.. code-block:: none sql

    CREATE TABLE `virtual_domains` (
        `id` int(11) NOT NULL auto_increment,
        `name` varchar(50) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

    CREATE TABLE `virtual_users` (
        `id` int(11) NOT NULL auto_increment,
        `domain_id` int(11) NOT NULL,
        `password` varchar(106) NOT NULL,
        `email` varchar(100) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY `email` (`email`),
        FOREIGN KEY (domain_id) REFERENCES virtual_domains(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

    CREATE TABLE `virtual_aliases` (
        `id` int(11) NOT NULL auto_increment,
        `domain_id` int(11) NOT NULL,
        `source` varchar(100) NOT NULL,
        `destination` varchar(100) NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (domain_id) REFERENCES virtual_domains(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

Finally, add a domain name, user and alias.

.. code-block:: none sql

    INSERT INTO virtual_domains (name) VALUES ('example.com');
    INSERT INTO virtual_users (domain_id, password, email) VALUES (1, ENCRYPT('<PASSWORD_HERE>', CONCAT('$6$', SUBSTRING(SHA(RAND()), -16))), 'user@example.com');
    INSERT INTO virtual_aliases (domain_id, source, destination) VALUES (1, 'alias@exampe.com', 'user@example.com');

Drop back to the Bash prompt using `CTRL-D` or with

.. code-block:: none

    EXIT

Postfix
=======

.. code-block:: none bash

    sudo apt-get install postfix postfix-mysql postfix-policyd-spf-python

When prompted for a Postfix configuration, just select `Internet Site`. You'll
also be prompted for a mail name, I'll be using `mail.example.com`.

Back up the original `main.cf` and `master.cf` for Postfix.

.. code-block:: none bash

    sudo mv /etc/postfix/main.cf{,.orig}
    sudo mv /etc/postfix/master.cf{,.org}

Create a new `/etc/postfix/main.cf` with the content below.

.. code-block:: none

    smtpd_banner = $myhostname ESMTP
    biff = no
    append_dot_mydomain = no
    readme_directory = no

    smtpd_use_tls = yes
    smtpd_tls_cert_file = /etc/ssl/certs/mail.crt
    smtpd_tls_key_file = /etc/ssl/private/mail.key
    smtpd_tls_auth_only = yes
    smtpd_tls_security_level = encrypt
    smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
    smtpd_tls_session_cache_timeout = 3600s
    smtpd_helo_required = yes
    smtpd_tls_received_header = yes
    smtpd_tls_security_level = may
    smtpd_tls_mandatory_ciphers = high
    smtpd_tls_mandatory_exclude_ciphers = aNULL, MD5, RC4
    smtpd_tls_mandatory_protocols = TLSv1
    smtpd_tls_loglevel = 1
    smtpd_sasl_type = dovecot
    smtpd_sasl_path = private/auth
    smtpd_sasl_auth_enable = yes
    smtpd_sasl_security_options = noanonymous
    smtpd_sasl_local_domain = $myhostname

    smtp_use_tls = yes
    smtp_tls_cert_file = /etc/ssl/certs/mail.crt
    smtp_tls_key_file = /etc/ssl/private/mail.key

    tls_random_source = dev:/dev/urandom
    broken_sasl_auth_clients = yes

    smtpd_recipient_restrictions =
        permit_mynetworks,
        permit_sasl_authenticated,
        reject_unauth_destination,
        reject_unknown_sender_domain,
        check_policy_service unix:private/policy-spf

    smtpd_sender_restrictions =
        permit_sasl_authenticated,
        permit_mynetworks

    policy-spf_time_limit = 3600s
    myhostname = mail.example.com
    myorigin = /etc/mailname
    mydestination = localhost
    relayhost =
    mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
    mailbox_size_limit = 0
    recipient_delimiter = +
    inet_interfaces = all

    virtual_transport = lmtp:unix:private/dovecot-lmtp
    virtual_mailbox_domains = mysql:/etc/postfix/mysql-virtual-mailbox-domains.cf
    virtual_mailbox_maps = mysql:/etc/postfix/mysql-virtual-mailbox-maps.cf
    virtual_alias_maps = mysql:/etc/postfix/mysql-virtual-alias-maps.cf

    smtpd_recipient_limit = 2000
    smtpd_milters =
        unix:clamav/clamav-milter.ctl,
        unix:spamass/spamass.sock
    milter_connect_macros = j {daemon_name} v {if_name} _
    milter_default_action = tempfail


Create a new `/etc/postfix/master.cf` and make it look like below.

.. code-block:: none

    smtp      inet  n       -       -       -       -       smtpd
        -o strict_rfc821_envelopes=yes
    submission inet n       -       -       -       -       smtpd
        -o syslog_name=postfix/submission
        -o smtpd_tls_security_level=encrypt
        -o smtpd_sasl_auth_enable=yes
        -o content_filter=dksign:[127.0.0.1]:10027
        -o smtpd_client_restrictions=permit_sasl_authenticated,reject
        -o milter_macro_daemon_name=ORIGINATING
    smtps     inet  n       -       -       -       -       smtpd
        -o syslog_name=postfix/smtps
        -o smtpd_tls_wrappermode=yes
        -o smtpd_sasl_auth_enable=yes
        -o content_filter=dksign:[127.0.0.1]:10027
        -o smtpd_client_restrictions=permit_sasl_authenticated,reject
        -o milter_macro_daemon_name=ORIGINATING
    pickup    fifo  n       -       -       60      1       pickup
    cleanup   unix  n       -       -       -       0       cleanup
    qmgr      fifo  n       -       n       300     1       qmgr
    tlsmgr    unix  -       -       -       1000?   1       tlsmgr
    rewrite   unix  -       -       -       -       -       trivial-rewrite
    bounce    unix  -       -       -       -       0       bounce
    defer     unix  -       -       -       -       0       bounce
    trace     unix  -       -       -       -       0       bounce
    verify    unix  -       -       -       -       1       verify
    flush     unix  n       -       -       1000?   0       flush
    proxymap  unix  -       -       n       -       -       proxymap
    proxywrite unix -       -       n       -       1       proxymap
    smtp      unix  -       -       -       -       -       smtp
    relay     unix  -       -       -       -       -       smtp
    showq     unix  n       -       -       -       -       showq
    error     unix  -       -       -       -       -       error
    retry     unix  -       -       -       -       -       error
    discard   unix  -       -       -       -       -       discard
    local     unix  -       n       n       -       -       local
    virtual   unix  -       n       n       -       -       virtual
    lmtp      unix  -       -       -       -       -       lmtp
    anvil     unix  -       -       -       -       1       anvil
    scache    unix  -       -       -       -       1       scache
    maildrop  unix  -       n       n       -       -       pipe
        flags=DRhu user=vmail argv=/usr/bin/maildrop -d ${recipient}
    uucp      unix  -       n       n       -       -       pipe
        flags=Fqhu user=uucp argv=uux -r -n -z -a$sender - $nexthop!rmail ($recipient)
    ifmail    unix  -       n       n       -       -       pipe
        flags=F user=ftn argv=/usr/lib/ifmail/ifmail -r $nexthop ($recipient)
    bsmtp     unix  -       n       n       -       -       pipe
        flags=Fq. user=bsmtp argv=/usr/lib/bsmtp/bsmtp -t$nexthop -f$sender $recipient
    scalemail-backend unix	-	n	n	-	2	pipe
        flags=R user=scalemail argv=/usr/lib/scalemail/bin/scalemail-store ${nexthop} ${user} ${extension}
    mailman   unix  -       n       n       -       -       pipe
        flags=FR user=list argv=/usr/lib/mailman/bin/postfix-to-mailman.py
        ${nexthop} ${user}
    policy-spf unix -       n       n       -       -       spawn
        user=nobody argv=/usr/bin/policyd-spf
    dksign    unix  -       -       n       -       4       smtp
        -o smtp_send_xforward_command=yes
        -o smtp_discard_ehlo_keywords=8bitmime,starttls
    127.0.0.1:10028 inet n  -        n      -       10      smtpd
        -o content_filter=
        -o receive_override_options=no_unknown_recipient_checks,no_header_body_checks
        -o smtpd_helo_restrictions=
        -o smtpd_client_restrictions=
        -o smtpd_sender_restrictions=
        -o smtpd_recipient_restrictions=permit_mynetworks,reject
        -o mynetworks=127.0.0.0/8
        -o smtpd_authorized_xforward_hosts=127.0.0.0/8

Next you'll create the config files to query MySQL.

Create `/etc/postfix/mysql-virtual-mailbox-domains.cf` with the content below.

.. code-block:: none

    user = mailuser
    password = <MYSQL_PASSWORD>
    hosts = 127.0.0.1
    dbname = mailserver
    query = SELECT 1 FROM virtual_domains WHERE name='%s'

Create `/etc/postfix/mysql-virtual-mailbox-maps.cf` with the content below.

.. code-block:: none

    user = mailuser
    password = <MYSQL_PASSWORD>
    hosts = 127.0.0.1
    dbname = mailserver
    query = SELECT 1 FROM virtual_users WHERE email='%s'

Create `/etc/postfix/mysql-virtual-alias-maps.cf` with the content below.

.. code-block:: none

    user = mailuser
    password = <MYSQL_PASSWORD>
    hosts = 127.0.0.1
    dbname = mailserver
    query = SELECT destination FROM virtual_aliases WHERE source='%s'

Reload Postfix and test that the domain and users work.

.. code-block:: none bash

    sudo /etc/init.d/postfix reload
    postmap -q example.com mysql:/etc/postfix/mysql-virtual-mailbox-domains.cf
    postmap -q user@example.com mysql:/etc/postfix/mysql-virtual-mailbox-maps.cf
    postmap -q alias@example.com mysql:/etc/postfix/mysql-virtual-alias-maps.cf

You should see output similar to below

.. code-block:: none

    1
    1
    user@example.com

Dovecot
=======

.. code-block:: none bash

    sudo apt-get install dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql

Backup the default Dovecot config files.

.. code-block:: none

    sudo cp /etc/dovecot/dovecot.conf{,.orig}
    sudo cp /etc/dovecot/conf.d/10-mail.conf{,.orig}
    sudo cp /etc/dovecot/conf.d/10-auth.conf{,.orig}
    sudo cp /etc/dovecot/dovecot-sql.conf.ext{,.orig}
    sudo cp /etc/dovecot/conf.d/10-master.conf{,.orig}
    sudo cp /etc/dovecot/conf.d/10-ssl.conf {,.orig}

For each domain you want to serve mail for, you will need to create a
directory for it to be stored in.

.. code-block:: none bash

    sudo mkdir -p /var/mail/vhosts/example.com

Add a user and group for the mail and give permissions on the mail directory.

.. code-block:: none bash

    sudo groupadd -g 5000 vmail
    sudo useradd -g vmail -u 5000 vmail -d /var/mail
    sudo chown -R vmail:vmail /var/mail

Modify the line in `/etc/dovecot/dovecot.conf` so it looks like below.

.. code-block:: none

    !include_try /usr/share/dovecot/protocols.d/*.protocol
    protocols = imap lmtp

Modify `/etc/dovecot/dovecot.conf` so it has the following lines.

.. code-block:: none

    mail_location = maildir:/var/mail/vhosts/%d/%n
    mail_privileged_group = mail

Edit `/etc/dovecot/conf.d/10-auth.conf`.

You'll need to uncomment the following line.

.. code-block:: none

    disable_plaintext_auth = yes

Set `auth_mechanisms` to look like below

.. code-block:: none

    auth_mechanisms = plain login

Next up, make sure the include lines look like below.

.. code-block:: none

    #!include auth-system.conf.ext
    !include auth-sql.conf.ext
    #!include auth-ldap.conf.ext
    #!include auth-passwdfile.conf.ext
    #!include auth-checkpassword.conf.ext
    #!include auth-vpopmail.conf.ext
    #!include auth-static.conf.ext

Create `/etc/dovecot/conf.d/auth-sql.conf.ext` and add the content below.

.. code-block:: none

    passdb {
        driver = sql
        args = /etc/dovecot/dovecot-sql.conf.ext
    }

    userdb {
        driver = static
        args = uid=vmail gid=vmail home=/var/mail/vhosts/%d/%n
    }

Edit `/etc/dovecot/dovecot-sql.conf.ext` and set the following values.

.. code-block:: none

    driver = mysql
    connect = host=127.0.0.1 dbname=mailserver user=mailuser password=<PASSWORD>
    default_pass_scheme = SHA512-CRYPT
    password_query = SELECT email as user, password FROM virtual_users WHERE email='%u'

Add the following content to `/etc/dovecot/conf.d/10-master.conf`

.. code-block:: none

    service imap-login {
        inet_listener imaps {
            port = 993
            ssl = yes
        }
    }

    service lmtp {
        unix_listener /var/spool/postfix/private/dovecot-lmtp {
            mode = 0600
            user = postfix
            group = postfix
        }
    }

    service auth {
        unix_listener /var/spool/postfix/private/auth {
            mode = 0666
            user = postfix
            group = postfix
        }
        unix_listener auth-userdb {
            mode = 0600
            user = vmail
        }
        user = dovecot
    }

    service auth-worker {
        user = vmail
    }

Modify `/etc/dovecot/conf.d/10-ssl.conf` to have the following lines.

.. code-block:: none

    ssl_cert = </etc/ssl/certs/mail.crt
    ssl_key = </etc/ssl/private/mail.key
    ssl = required

For fulltext searching, you'll want to enable wheezy-backports and install
`dovecot-solr` from there.

.. code-block:: none bash

    sudo echo "deb http://ftp.debian.org/debian wheezy-backports main contrib non-free" >> /etc/apt/sources.list
    sudo apt-get update
    sudo apt-get install dovecot-solr solr-tomcat

There is a bug in `dovecot-solr` where it doesn't set up the Solr schema for,
you'll have to do it by downloading `orig.tar.gz` from `the Debian website
<https://packages.debian.org/wheezy/dovecot-solr>`_.

Extract the archive and copy the included schema in to Solr.

.. code-block:: none bash

    sudo cp docs/solr-schema.xml /etc/solr/conf/schema.xml

For security reasons, modify `/etc/tomcat6/server.xml` to have the local address
in the Connectory.

.. code-block:: none xml

    <Connector address="127.0.0.1" port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               URIEncoding="UTF-8"
               redirectPort="8443" />

Modify `/etc/dovecot/conf.d/20-imap.conf` to have the following line.

.. code-block:: none

    mail_plugins = $mail_plugins fts fts_solr

Next up, add the following lines to `/etc/dovecot/conf.d/90-plugin.conf`

.. code-block:: none

    plugin {
        fts = solr
        fts_solr = break-imap-search url=http://localhost:8080/solr/
    }

Create `/etc/cron.daily/solr` with the following contents.

.. code-block:: none bash

    #!/bin/sh
    curl http://localhost:8080/solr/update?optimize=true

Create `/etc/cron.hourly/solr` with the following contents.

.. code-block:: none bash

    #!/bin/sh
    curl http://localhost:8080/solr/update?commit=true

Make both files executable.

.. code-block:: none bash

    sudo chmod +x /etc/cron.daily/solr /etc/cron.hourly/solr

Solr uses soft commits when it indexes new mail, this only commits to memory so
a cron task is good for committing every hour and a daily optimize for keeping
things fast.

That's all for Dovecot and Solr, so restart them.

.. code-block:: none bash

    sudo /etc/init.d/dovecot restart
    sudo /etc/init.d/tomcat6 restart

ClamAV and SpamAssassin milters
===============================

.. code-block:: none bash

    sudo apt-get install clamav-milter clamav-unofficial-sigs spamass-milter

You'll likely get an error when installing these, don't worry.

.. code-block:: none bash

    sudo freshclam
    sudo /etc/init.d/clamav-daemon start

Uncomment the last line in `/etc/default/clamav-milter`.

.. code-block:: none

    SOCKET_RWGROUP=postfix

Now create somewhere for the clamav-milter socket to reside.

.. code-block:: none bash

    sudo mkdir /var/spool/postfix/clamav
    sudo chown clamav /var/spool/postfix/clamav

Edit `/etc/clamav/clamav-milter.conf` to look like below.

.. code-block:: none

    MilterSocket /var/spool/postfix/clamav/clamav-milter.ctl
    FixStaleSocket true
    User clamav
    AllowSupplementaryGroups true
    ReadTimeout 120
    Foreground false
    PidFile /var/run/clamav/clamav-milter.pid
    ClamdSocket unix:/var/run/clamav/clamd.ctl
    OnClean Accept
    OnInfected Reject
    OnFail Defer
    AddHeader Replace
    LogSyslog false
    LogFacility LOG_LOCAL6
    LogVerbose false
    LogInfected Off
    LogClean Off
    LogRotate true
    MaxFileSize 100M
    SupportMultipleRecipients true
    RejectMsg Rejecting harmful e-mail: %v found.
    TemporaryDirectory /tmp
    LogFile /var/log/clamav/clamav-milter.log
    LogTime true
    LogFileUnlock false
    LogFileMaxSize 0
    MilterSocketGroup clamav
    MilterSocketMode 666

Edit `/etc/default/spamass-milter` and add the following line.

.. code-block:: none

    OPTIONS="-u spamass-milter -i 127.0.0.1 -m -r -1 -I"

Edit `/etc/default/spamassassin` to have the following values.

.. code-block:: none

    ENABLED=1
    CRON=1

Update SpamAssassin and start the service.

.. code-block:: none bash

    sudo sa-update
    sudo /etc/init.d/spamassassin start

DKIMProxy
=========

.. code-block:: none bash

    sudo apt-get install dkimproxy

Create a private and public keypair.

.. code-block:: none bash

    sudo openssl genrsa -out /etc/dkimproxy/private.key 1024
    sudo openssl rsa -in /etc/dkimproxy/private.key -out /etc/dkimproxy/public.key -pubout -outform PEM

Modify `/etc/dkimproxy/dkimproxy_in.conf` to look like below.

.. code-block:: none

    listen 127.0.0.1:10025
    relay 27.0.0.1:10026

Modify `/etc/dkimproxy/dkimproxy_out.conf` to look like below.

.. code-block:: none

    listen 127.0.0.1:10027
    relay 127.0.0.1:10028
    domain example.com
    keyfile /etc/dkimproxy/private.key
    selector mail

There seems to be a rather annoying bug where signatures are not modified
based on the config, I found the easiest way to cheat this is to just modify
the init.d file for dkimproxy.

.. code-block:: none bash

    DKIMPROXY_OUT_ARGS="${COMMON_ARGS} --pidfile=${PIDDKIMPROXY_OUT} --min_servers=${DKIMPROXY_OUT_MIN_SERVERS} --domain=example.com --method=simple --conf_file=${DKOUT_CONF} --keyfile=/etc/dkimproxy/private.key --selector=mail --signature=dkim(a=rsa-sha256) --signature=domainkeys(a=rsa-sha1)"

Finally, restart dkimproxy.

.. code-block:: none bash

    /etc/init.d/dkimproxy restart

DNS
===

All that needs to be done now is to create two three records.

.. code-block:: none

    example.com. IN TXT "v=spf1 a mx -all"

.. code-block:: none

    _domainkey.example.com. IN TXT "o=-;"

.. code-block:: none

    mail._domainkey.example.com. IN TXT "k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDGTLLBUsIH..."


The contents of the latter record are the public key from `/etc/dkimproxy/public.key`.
