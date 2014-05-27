HOWTO: Using SPF to validate outgoing mail
##########################################
:date: 2010-02-11 18:25
:author: kura
:category: tutorials
:tags: howto, mail
:slug: howto-using-spf-to-validate-outgoing-mail

.. contents::
    :backlinks: none

You can get a basic overview on what SPF is, what it's for and it's more
advanced usages here - `http://www.openspf.org/`_

.. _`http://www.openspf.org/`: http://www.openspf.org/

This article is to give only a basic insight in to how you can use an
SPF record to valid mail from your servers.

The DNS
-------

SPF records work from your DNS, it's really simple. Technically there is
a DNS type defined for SPF records as of `RFC 4408`_, but since not all
servers recognise this type it also works in the TXT type.

.. _RFC 4408: http://tools.ietf.org/html/rfc4408

A simple usage of SPF is

::

    v=spf1 a mx -all

Imagine this exists on this domain, **syslog.tv**. This spf record would
mean that ALL AN and MX servers listed in the DNS records of syslog.tv
would be valid senders.

The hypen (-) before *all* means that if the mail appears to be coming
from a server that isn't listen in syslog.tv's DNS records then the
check should fail.

Mechanisms
~~~~~~~~~~

+=============+=============================================================================================================+
| Mechanism   | Description                                                                                                 |
| +=============+===========================================================================================================+
| **ALL**     | Matches always                                                                                              |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **A**       | If the domain name has an A (or AAAA for IPv6) record corresponding to the sender's address, it will match. |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **IP4**     | If the sender is in a given IPv4 range, match.                                                              |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **IP6**     | If the sender is in a given IPv6 range, match.                                                              |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **MX**      | If the domain name has an MX record resolving to the sender's address, it will match.                       |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **PTR**     | If the RDNS domain of the sending IP ending in the domain name.                                             |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **EXISTS**  | If the given domain resolves, matches.                                                                      |
+-------------+-------------------------------------------------------------------------------------------------------------+
| **INCLUDE** | If the included policy passes the test this mechanism matches.                                              |
+-------------+-------------------------------------------------------------------------------------------------------------+

Qualifiers
~~~~~~~~~~
+===========+=====================================================+
| Qualifier | Description                                         |
+===========+=====================================================+
| **+**     | PASS result.                                        |
+-----------+-----------------------------------------------------+
| **?**     | NEUTRAL result interpreted like no policy.          |
+-----------+-----------------------------------------------------+
| **~**     | SOFTFAIL, a debugging aid between NEUTRAL and FAIL. |
+-----------+-----------------------------------------------------+
| **-**     | FAIL, the mail should be rejected.                  |
+-----------+-----------------------------------------------------+

More examples
-------------

::

    v=spf1 include:google.com -all

Include SPF records from the domain **google.com** and pass if record
matches any from the include, failing if it doesn't.

::

    v=spf1 exists:syslog.tv

If syslog.tv resolves, pass.

::

    v=spf mx ~all

If record matches against an MX record for the domain in the DNS, pass,
if not then neutrally fail but still be accepted.

Hopefully this basic guide is helpful, SPF records are very useful and
we use them a lot at work across our mail platform, going so far as to
get clients to include our SPF records in their DNS to ensure no
failures when they send email via our servers.
