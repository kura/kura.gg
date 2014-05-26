Bye bye Google Analytics, hello self-hosted Open Web Analytics & DuckDuckGo search
##################################################################################
:date: 2013-09-17 18:00
:author: kura
:category: misc
:tags: google analytics, duckduckgo, open web analytics, owa
:slug: bye-bye-google-analytics-hello-self-hosted-open-web-analytics-duckduckgo-search

.. contents::

Today I can happily announce that `the Google Analytics tracking code has been
removed from this website
<https://github.com/kura/kura.io/commit/5e82c14bab3922d81b430549dd258a2047d1367f>`_.

Goodybye Google Analytics & hello Open Web Analytics
====================================================

I've been planning on doing it from a while because I do not like Google Analytics,
I don't like being tracked and I actively stopped trying to use Google services
for my own reasons.

The company I work for uses `Piwik <http://piwik.org/>`_
for some of our clients, I am not a fan
of Piwik or how it works and does things. I did some research and found some
service providers but their free options were limited or I felt they weren't a
good fit, eventually I stumbled upon `Open Web Analytics
<http://www.openwebanalytics.com>`_ and decided that it
not only suited my purposes, but it meant servers I control would hold the
analytical data, rather than some third party.

Hello DuckDuckGo
================

After launching the new version of my site, I got upset at the fact I had lost
my search functionality. Sadly `Pelican <http://docs.getpelican.com/>`_
does not have any working search
functionality and I undertook the task of building `Sphinx <http://sphinx-doc.org/>`_
-style searches
in to Pelican, making it entirely static.

The task of building this functionality is still under way, but I decided that
I would like a more immediate option.

I've been using DuckDuckGo as my primary and only search provider for quite a
long time now and learned that you can embed it on your site easily, just like
with Google site searches.

So there it is, embded happily and with adverts enabled on their end to make
sure they make some revenue from it.
