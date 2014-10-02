Tor all the things!
###################
:date: 2014-10-02 03:45
:author: kura
:category: tor
:tags: tor
:slug: tor-all-the-things

Privacy is key
--------------

I am a big fan of keeping my browsing habits and other personal information
private. As such, I use a VPN service provided by `proxy.sh (affiliate link)
<https://proxy.sh/panel/aff.php?aff=079>`_, I also use their proxies, Tor and
various other proxies, usually from online lists, should I feel the need.

Anonymous nodes
---------------

I've run some Tor nodes for quite a while now, two Exits and five relays to be
precise. They are all listed as being part of the same family and have never
had any reference to me being their operator.

Sadly, these seven nodes will always remain a secret due to the hassle that
inherently comes with running Tor Exit nodes. These issues include some mean
emails and IP addresses and CIDR blocks being blacklisted by services like
Netflix.

New nodes!
----------

The good news is, I have recently launched three more nodes! These nodes
belong to a different family and share my PGP identity, an email address I can
be contacted at with regards to the nodes and my lovely bitcoin address for
anyone interested in firing off a donation.

At time of writing, the servers are part of the Tor network but they are
currently in their initial phase of being rarely used by the network itself.
A `post on the Tor blog
<https://blog.torproject.org/blog/lifecycle-of-a-new-relay>`_ gives some
anecdotal information as to each phase, why it happens and what it means. I
suggest giving it a read since it's quite interesting.

In my experience, within about two weeks, all three new nodes will be available
as fast relays and be acceptable is guard relays too.

Bandwidth
---------

Each of the three nodes has a 1Gbps network interface, two of the nodes have
truly infinite bandwidth while the third only has 1TB of outbound transfer but
infinite inbound.

Hopefully all three servers will add some much needed bandwidth and speed
capacity to the Tor network.

The US
------

Another piece of good news is one of these servers is actually running in the
U.S., which is something I tend to stay away from in general. This will be my
second U.S. Tor node, hopefully it will push me to run more nodes in that
region in the future.

The nodes
---------

These new nodes having a nickname scheme akin to the Ubuntu convention, but
slightly more disgusting, as befits my warped personality.

* `SpunkWeasel 865A408E2B1EA3E18C9A12E80A8D458F9C985C16 <https://globe.torproject.org/#/relay/865A408E2B1EA3E18C9A12E80A8D458F9C985C16>`_,
* `AnorexicSquirrel B8E6FFEB6F91FA3D26BC572836FB0ABBD142DC87 <https://globe.torproject.org/#/relay/B8E6FFEB6F91FA3D26BC572836FB0ABBD142DC87>`_ and,
* `EjactulatingWhale E803339621BD78503AC333F0FDA35DB705B18071 <https://globe.torproject.org/#/relay/E803339621BD78503AC333F0FDA35DB705B18071>`_.

Feel free to contact the address listed on the nodes if you have any queries or
questions regarding the nodes or running your own. Bitcoin donations are always
welcome and will help keep these nodes running and allow more to be onlined.

Relay, relay, relay
-------------------

As a final note, running a relay is pretty damn safe. You can do it pretty
cheaply too on AWS, with DigitalOcean or any other VPS provide. Relays are
generally allowed to be run on those environments too, although dropping an
email or support ticket to say you're doing it is always a good idea.

The Tor network needs nodes, especially Guards and Exits. Exits are a
difficult thing for most people to run but relays and Guards are easy. A Guard
relay is simply just a standard relay that has currently been chosen to have
the Guard flag, which is in a time period-based rotation, so it really is
simple.
