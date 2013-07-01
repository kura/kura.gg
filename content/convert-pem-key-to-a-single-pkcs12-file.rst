Convert PEM & Key to a single PKCS#12 file
##########################################
:date: 2010-04-13 19:19
:author: kura
:category: howto
:tags: crt, openssl, pem, pkcs12, ssl
:slug: convert-pem-key-to-a-single-pkcs12-file

Sometimes keeping multiple copies of keys, certificates and root
certificates can be a real annoyance, thankfully it's quite simple to
convert them in to a single PKCS#12 file with the following command.

    openssl pkcs12 -export -out certificate.pkcs -in certificate.crt -inkey private.key -certfile rootcert.crt -name "PKCS#12 Certificate Bundle"

This will create a file called **certificate.pkcs** which will contain
the contents of the **certificate.crt**, **private.key** and your root
certificate **rootcert.crt**, it will also have an internal reference to
it's name **PKCS#12 Certificate Bundle** to make it easier to inspect
the certificate to find what it should contain, usually you'd set this
to something more useful.
