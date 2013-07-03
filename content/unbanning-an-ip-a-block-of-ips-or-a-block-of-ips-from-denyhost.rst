Unbanning an IP, multiple IPs or a block of IPs from DenyHost
#############################################################
:date: 2012-11-13 17:45
:author: kura
:category: tutorials
:tags: denyhosts, unban
:slug: unbanning-an-ip-a-block-of-ips-or-a-block-of-ips-from-denyhost

I wrote this little Python program a while ago and now people are
starting to email me about it, asking for it to be part of the DenyHosts
Debian packages so I figured I'd write a quick article on it.

If you're like my developers, you'll find yourself getting banned from
servers all the time and have to come speak to someone like me (your sys
engineer/admin), or maybe you are an admin and are sick of people
banning themselves and want and easy way to unban them.

So give this a try:

`https://github.com/kura/denyhosts-unban`_

.. _`https://github.com/kura/denyhosts-unban`: https://github.com/kura/denyhosts-unban

From the GitHub page you can download either the tarballs, zipballs or a
Debian .deb package. Install it using the instructions in the README and
you're good to go.

Unban
-----

Unbanning is simple, you can either unban a single IP using:

    sudo denyhosts-unban 10.0.0.1

Or multiples using:

    sudo denyhosts-unban 10.0.0.1 10.0.0.2

Or, you can use a bashism to unban an entire range:

    sudo denyhosts-unban 10.0.0.{0..255}
