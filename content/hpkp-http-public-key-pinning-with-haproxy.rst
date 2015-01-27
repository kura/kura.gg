HPKP: HTTP Public Key Pinning with HAProxy
##########################################
:date: 2015-01-27 07:04
:author: kura
:category: tutorials
:tags: haproxy, http, tls, ssl, hpkp, public key pinning
:slug: hpkp-http-public-key-pinning-with-haproxy

.. contents::

Public Key Pinning is a security feature that tells a web browser to associate
a public cryptographic key with a server or servers. When a web browser visits
a website for the first time, it will read the HPKP header and store the hashes
for the certificates that are provided. Each time the browser then revisits
that website, the hash from the provided public key is compared against the
stored keys, if the hashes do not match, the web browser should display a
warning.

The HPKP header adds protection against man-in-the-middle (MITM) attacks but,
if incorrectly configured can make your website display a TLS error for a long
period of time.

Here's a look at what this website publishes as it's HKPK header.

::

    Public-Key-Pins: pin-sha256="cYf9T3Il8DaCnaMaM0LatIAru1vqmcu2JSwS7uvyEB0="; pin-sha256="u2q8QZ8Hjp3o/efZjsch9NKjnZmrISJQjwoi/rmsKLU="; max-age=15768000; includeSubDomains

To explain it, the first `pin-sha265` key is the hash of the public key that
was used to generate the certificate this website uses, the second `pin-sha256`
key is the hash of the public key that I have as a backup for when I either need
to generate a new certificate when the old one expires or if something happens
and I need to revoke the old key. `max-age` tells the browser how long to store
the pin-sha256 details, for me that is 182 days and finally `includeSubDomains`
tells the browser that these hashes are valid for this domain and all sub
domains.

Extracting the public key information
=====================================

These commands will extract the public key information and encode it in base64.

.. code:: bash

    openssl rsa -in KEYFILE -outform der -pubout | openssl dgst -sha256 -binary | base64

The above command will extract the public key from a private key generated with
`openssl genrsa`, you can replace rsa with dsa for DSA keys.

.. code:: bash

    openssl req -in CSRFILE -pubkey -noout | openssl rsa -pubin -outform der | openssl dgst -sha256 -binary | base64

The above command will extract the public key from a CSR.

.. code:: bash

    openssl x509 -in PEMFILE -pubkey -noout | openssl rsa -pubin -outform der | openssl dgst -sha256 -binary | base64

And the above command here will extract the public key from an existing x509
certificate.

All three of the above commands will generate something similar to below.

::

    writing RSA key
    cYf9T3Il8DaCnaMaM0LatIAru1vqmcu2JSwS7uvyEB0=

Backup key(s)
=============

The backup key is actually really simple, you make any number of backups and
store them for future use in case of problems or emergencies with the primary
key file.

.. code:: bash

    openssl genrsa -out backup1.key 4096

You can then use the command in the previous section to get the base64 encoded
public key of this backup key.

The HPKP header
===============

::

    Public-Key-Pins: pin-sha256="PUBLIC_KEY"; max-age=EXPIRE_TIME [; includeSubdomains][; report-uri="REPORT_URI"]

As you can see the header is relatively simple, a definition of each option is
below.

pin-sha256
    The quoted string is the Base64 encoded fingerprint. You can specify this
    option multiple times.

max-age
    The time, in seconds, that the browser should remember that this site is only to be accessed using one of the pinned keys.

includeSubdomains *optional*
    If this optional parameter is specified, this rule applies to all of
    the website's subdomains.

report-uri *optional*
    If this optional parameter is specified, pin validation failures are
    reported to this URL. This won't be covered here though.

HAProxy
=======

In HAproxy you simply using the `rspadd` config option inside the `frontend`
declaration.

::

    rspadd Public-Key-Pins:\ pin-sha256="KEY=";\ pin-sha256="BACKUP_KEY";\ max-age=15768000;\ includeSubDomains
