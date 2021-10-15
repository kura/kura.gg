Google Workspace Gmail MX records signed with DNSSEC
####################################################
:date: 2021-10-14 16:50
:author: kura
:category: email
:tags: gmail, email, smtp, dnssec
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

The table below has the MX record and the A and AAAA record values.

.. code::

    mx1.smtp.goog
        216.239.32.151
        2001:4860:4802:32::97

    mx2.smtp.goog
        216.239.34.151
        2001:4860:4802:34::97

    mx3.smtp.goog
        216.239.36.151
        2001:4860:4802:36::97
        216.239.32.151

    mx4.smtp.goog
        216.239.38.151
        2001:4860:4802:38::97


I am using them myself but I am also willing to take the risk of
them possibly vanishing without any warning.

.. code::

    kura.gg.	300	IN	MX	10	mx1.smtp.goog.
    kura.gg.	300	IN	MX	20	mx2.smtp.goog.
    kura.gg.	300	IN	MX	30	mx3.smtp.goog.
    kura.gg.	300	IN	MX	40	mx4.smtp.goog.
