Convert DER certificate to PEM
##############################
:date: 2010-03-03 17:26
:author: kura
:category: tutorials
:tags: apache, certificate, crt, der, pem, ssl
:slug: convert-der-certificate-to-pem

Some times as an administrator you will be given a certificate from a
third party that will be in the DER format, which cannot be loaded in to
Apache.

Converting it is a simple process:

.. code-block:: bash

    openssl x509 -in certificate.crt -inform DER -out certificate.pem -outform PEM
