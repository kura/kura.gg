Postfix spam protection with blacklists
#######################################
:date: 2011-09-24 21:05
:author: kura
:category: tutorials
:tags: blackhole, blacklist, email, mail, postfix, spam
:slug: postfix-spam-protection-with-blacklists

This really should be quite a quick and simple post.

I use several tools to protect my mail servers from spam, the most
effective of these I've found is using external lists in conjunction
with **reject_rbl_client** and **reject_rhsbl_client**.

+======================+
| Service              | Description
+======================+======================================================================================================+
| zen.spamhaus.org     | A single lookup for querying the SBL, XBL and PBL databases.                                         |
|                      |  - SBL - Verified sources of spam, including spammers and their support services                     |
|                      |  - XBL - Illegal third-party exploits (e.g. open proxies and Trojan Horses)                          |
|                      |  - PBL - Static, dial-up & DHCP IP address space that is not meant to be initiating SMTP connections |
+----------------------+------------------------------------------------------------------------------------------------------+
| dnsbl.sorbs.net      | Unsolicited bulk/commercial email senders                                                            |
+----------------------+------------------------------------------------------------------------------------------------------+
| spam.dnsbl.sorbs.net | Hosts that have allegedly sent spam to the admins of SORBS at any time                               |
+----------------------+------------------------------------------------------------------------------------------------------+
| b1.spamcop.net       | IP addresses which have been used to transmit reported email to SpamCop users                        |
+----------------------+------------------------------------------------------------------------------------------------------+
| rhsbl.ahbl.org       | Domains sending spam, domains owned by spammers, comment spam domains, spammed URLs                  |
+----------------------+------------------------------------------------------------------------------------------------------+

The description for each of these services was shamelessly taken from
Wikipedia, I have listed the services that I actually use but you can
find a much larger list on the `page that I took the descriptions
from`_.

.. _page that I took the descriptions from: http://en.wikipedia.org/wiki/Comparison_of_DNS_blacklists

***Please note that the SORBS lists are generally classed as being
aggressive and a lot of people advise not to use them due to this. They
have been known to block emails from senders like Facebook.***

You can pick and choose which ones you use and you configure them as
below within **smtp_recipient_restrictions** in **/etc/postfix/main.cf**

::

    smtpd_recipient_restrictions =
      reject_rbl_client zen.spamhaus.org,
      reject_rbl_client dnsbl.sorbs.net,
      reject_rbl_client spam.dnsbl.sorbs.net,
      reject_rbl_client bl.spamcop.net,
      reject_rhsbl_client rhsbl.ahbl.org
