Running a Tor exit node is not as scary as it sounds
####################################################
:date: 2015-02-02 09:59
:author: kura
:category: misc
:tags: tor
:slug: running-a-tor-exit-node-is-not-as-scary-as-it-sounds

.. contents::
    :backlinks: none

There is a variety of information out there about being a Tor exit node
operator. Articles like `this one
<https://testbit.eu/tor-exit-node-less-week/>`_
make the thought of running a Tor exit as scary prospect, it's understandable,
some countries have laws that make running an exit scary too.

I run `a variety of relays </tor/>`_ in various countries in this crazy World
and thought I'd share my experiences.

Choosing a hosting partner
==========================

I personally choose to use a third party hosting provider for my relays,
rather than using colocation. I just find this is easier and I don't have to
think about the hardware much at all.

Finding a provider can be a pain, there is a decent list on the `Tor wiki
<https://trac.torproject.org/projects/tor/wiki/doc/GoodBadISPs>`_. I use
some of the providers on this list but I've also found it can be a really
good idea to just contact a provider and talk to them. There is a company I
spoke to recently that is quite small and were really happy about the idea of
having an exit operator using them. When we have figured things out, I'll
add them to the wiki.

You'll really want to find a provider with 1Gbps link and lots of bandwidth, I
like to find or pay for unmetered 1Gbps connectivity, but 10TB/month should be
a good amount.

A good exit policy
===================

The exit policy is everything, it can mean the difference between lots of abuse
complaints or very few. There is a `good reduced exit policy on the Tor Wiki
<https://trac.torproject.org/projects/tor/wiki/doc/ReducedExitPolicy>`_, I use
this on all of my nodes.

Abuse complaints
================

With the reduced exit policy from the Tor wiki, I find abuse complaints are
actually very rare.

The complaints I get are usually automatic emails from some hosting companies
that have HTTP brute force attempts logged. Not many companies use these
things but there are a few. There's not much you can do, they are automated
and you should reply to them like you should reply to all abuse complaints but,
the response will never be read.

The majority of complaints I get are related to `stopforumspam.com
<https://stopforumspam.com/>`_. Again, there's not really anything you can do
about this except reply.

Generally though, I will receive maybe one complaint per month on each node,
sometimes two, but that's about it and it's always one of the two abuse reports
I mentioned above.

Use the exit notice
===================

I can't really give any evidence as to whether or not this helps but, use the
`Tor exit notice <https://svn.torproject.org/svn/tor/branches/hidserv-perf/contrib/tor-exit-notice.html>`_
on port 80. This means any admins that look up your IP may browse to it and see
it's a Tor exit node and also has your email address in case they want to get
in touch about blocking their servers from your node.

Incorporate
===========

I haven't had any reason to result to this myself but, I started my own
company (easy to do in the UK) and my servers are paid for through this company.

It's really not much hassle to set-up a company and a company bank account.

Any of the donations I receive that aren't Bitcoin are paid in to this company
too to continue paying for my nodes and put new ones online.
