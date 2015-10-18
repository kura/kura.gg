SSHFP DNS records
#################
:date: 2015-10-18 03:30
:author: kura
:category: tutorials
:tags: dnssec, dns, sshfp, ssh
:slug: sshfp-dns-records

`SSHFP <http://tools.ietf.org/html/rfc4255>`_ records are a defense against
people blindly typing 'yes' when asked if they want to continue connecting to
an SSH host who's authenticity is unknown.

.. code:: bash

    $ ssh some.host.tld
    The authenticity of host 'some.host.tld (123.456.789.10)' can't be established.
    ED25519 key fingerprint is 69:76:51:39:a4:c6:de:15:7c:50:4b:4a:a7:98:40:5e.
    Are you sure you want to continue connecting (yes/no)?

This prompt is likely to be extremely familiar to you and, most people seem to
just type 'yes' to move on with their lives, which defeats the whole purpose of
this prompt.

If you use DNSSEC you can bypass this prompt entirely by publishing your
server's key fingerprints via DNS and having SSH authenticate them for you.

Generating your SSHFP record
============================

You can get SSH to generate the DNS records for you, log in to the server in
question and run the command below to get similar content.

.. code:: bash

    $ ssh-keygen -r some.host.tld
    some.host.tld IN SSHFP 1 1 c53bfb3d5d053280b17db76909f707f3ac9cbb47
    some.host.tld IN SSHFP 1 2 56310ad73fae7a3861f87c246f1fb7c0884706f9a65e94d75be4fb14ca973275
    some.host.tld IN SSHFP 4 1 fe3a67a65b71631c8c16c173c09ad9885b72bd4e
    some.host.tld IN SSHFP 4 2 7dd9225ef20b806e78fca60935c8b051565ab6077d7735e2c8d23fdfd26289d2

Each line in response contains the following information.

+---------------+----------+-----------+------------------+------------------------------------------+
| Hostname      | IN SSHFP | Algorithm | Fingerprint type | Hash                                     |
+===============+==========+===========+==================+==========================================+
| some.host.tld | IN SSHFP | 1         | 1                | c53bfb3d5d053280b17db76909f707f3ac9cbb47 |
+---------------+----------+-----------+------------------+------------------------------------------+

Algorithm
---------

1. RSA
2. DSA
3. ECDSA
4. ED25519

Fingerprint type
----------------

1. SHA-1
2. SHA-2

I would advise you do not use DSA or ECDSA algorithms and SHA-1 fingerprints.

Add the relevant records to your DNS.

~/.ssh/config
=============

Add the following to your ~/.ssh/config file.

.. code::

    Host *
        VerifyHostKeyDNS yes

This means SSH will always try to validate host keys from DNS.

Now, when you try to SSH to a host it should validate against SSHFP records
automatically.

.. code:: bash

    $ ssh -v some.host.tld
    ...
    debug1: found 2 secure fingerprints in DNS
    debug1: matching host key fingerprint found in DNS
    ...

If you're not using DNSSEC then automatic validation will not happen, instead
you will be told that records match but the fingerprints are insecure.
