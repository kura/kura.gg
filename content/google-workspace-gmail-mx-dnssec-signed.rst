Google Workspace Gmail MX records signed with DNSSEC
####################################################
:date: 2021-10-14 16:50
:author: kura
:category: email
:tags: gmail email smtp dnssec
:slug: google-workspace-gmail-mx-dnssec-signed

.. contents::
    :backlinks: none

Gmail provided by the paid Google Workspace service (formerly
known as G Suite and Google Apps) has unofficial DNSSEC-signed
MX records available for use. The officially supported ones
that you're told to configure do not offer DNSSEC signing.

These MX records have both IPv4 and IPv6 addresses, although
the records are not officially supported or documented and
may be unreliable or removed at any point. (I've been using them
for a while now and they seem perfectly fine to me but use at
your own risk.)

.. code::

    mx1.smtp.goog
    mx2.smtp.goog
    mx3.smtp.goog
    mx4.smtp.goog

