haproxy OCSP stapling
#####################
:date: 2014-07-02 23:45
:author: kura
:category: tutorials
:tags: haproxy, ssl, ocsp, ocsp stapling
:slug: haproxy-ocsp-stapling

.. contents::
    :backlinks: none

With haproxy 1.5 finally being released we are lucky enough to get a basic
interface around OCSP stapling.

Sadly this interface really is quite basic and it's not the simplest thing to
figure out without some trial and error.

According to the official documentation, you should be able to pipe your
OCSP response to haproxy via it's stats socket. Sadly I could not get this to
work properly at all, so I decided to swap the piping for a file and reload
solution.

You'll need to get a copy of your certification authorities root certificate
to proceed with this.

Looking for your OCSP URI
=========================

If you don't know the URI you need to do an OCSP lookup against, you can find
it in your certificate data.

.. code:: bash

    openssl x509 -in /path/to/your/certificate -text

Inside the output, look for the following section.

::

    Authority Information Access:
        CA Issuers - URI:http://secure.globalsign.com/cacert/gsdomainvalsha2g2r1.crt
        OCSP - URI:http://ocsp2.globalsign.com/gsdomainvalsha2g2

Testing OCSP response
=====================

.. code:: bash

    openssl ocsp -noverify -issuer /path/to/your/ca/root/certificate \
                 -cert /path/to/your/certificate -url "OCSP_URI"

You should see a response like the one below.

::

    /path/to/your/certificate: good
    This Update: Jul  2 23:01:54 2014 GMT

If you get any errors from this, you may need to try these additional arguments;

Disable nonces
--------------

::

    -no_nonce

This will disable nonces, some servers are not able to handle nonces so you may
need to disable them.

Send a "Host" header
--------------------

If you get an HTTP error like a 403 or 404 error then you may need to specify
a host header.

::

    -header Host OCSP_URI_DOMAIN

For my certificate the OCSP URI is *http://ocsp2.globalsign.com/gsdomainvalsha2g2*
so the Host header would be like below.

::

    -header Host ocsp2.globalsign.com

Proving OCSP data to haproxy
============================

If the above testing was all OK, we can now actually use the data.

.. code:: bash

    openssl ocsp -noverify -issuer /path/to/your/ca/root/certificate \
                 -cert /path/to/your/certificate \
                 -url "OCSP_URI" -respout /path/to/your/certificate.ocsp

One thing to note is, if your certificate file is */etc/ssl/certs/kura.io.crt*
then you must set -respout to */etc/ssl/certs/kura.io.crt.ocsp*

You can now simply reload haproxy and check your OCSP staping is working.

Testing OCSP from haproxy
=========================

.. code:: bash

    openssl s_client -connect domain.tld:443 -tls1 -tlsextdebug -status

Near the top of the response you'll see your OCSP information.

::

    OCSP response:
    ======================================
    OCSP Response Data:
        OCSP Response Status: successful (0x0)
        Response Type: Basic OCSP Response
        Version: 1 (0x0)
        Responder Id: DFDE6C7C4B6C4098FA6992156D2B082875FD6443
        Produced At: Jul  2 22:58:27 2014 GMT
        Responses:
        Certificate ID:
            Hash Algorithm: sha1
            Issuer Name Hash: D1F1B576F9EEC0C10F7AFC7C3124A9C3625D7C61
            Issuer Key Hash: EA4E7CD4802DE5158186268C826DC098A4CF970F
            Serial Number: 1121C92209F7127584AAFEB2B08ECDD30A9D
        Cert Status: good
        This Update: Jul  2 22:58:27 2014 GMT

Updating OCSP
=============

The simplest way of doing this is by using cron.daily or something similar
to update your certificate.ocsp file.
