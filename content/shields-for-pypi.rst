Shields for PyPI packages
#########################
:date: 2013-12-24 14:07
:author: kura
:category: coding
:tags: python, pypi, shields
:slug: shields-for-pypi-packages

.. contents::

.. image:: https://pypip.in/d/blackhole/badge.png

.. image:: https://pypip.in/v/blackhole/badge.png

.. image:: https://pypip.in/egg/blackhole/badge.png

.. image:: https://pypip.in/wheel/blackhole/badge.png

.. image:: https://pypip.in/license/blackhole/badge.png


Some time back in April 2013 I was bored and looking for a new project to keep
my attention, if only for a short period of time.

My colleague `@codeinthehole <https://twitter.com/codeinthehole>`_ had an idea
but no time to implement it, this idea was to have shields like those of
`travis-ci <https://travis-ci.org>`_ (shown below) but displaying package
download counts.

.. image:: https://api.travis-ci.org/kura/blackhole.png?branch=master

Tech stack
==========

From the very start I decided to use
`Tornado framework <http://www.tornadoweb.org/en/stable/>`_, although this may
change in the future.

The original plan was to generate the images using Pillow (PIL) and then simply
cache them to disk. I decided it would make far more sense to do this using
`Varnish <https://www.varnish-cache.org/>`_ and not have to worry about it
working as expected.

Manually generating the images
==============================

The images were originally generated from a base template using Pillow, but
sadly Python's image manipulation is not very good, especially it's text
manipulation and the shields could have really used a bit of work.

I reached out to the `shields project <https://github.com/gittip/shields.io>`_
but sadly got no response so the images remained as they were.

crate.io shuts down
===================

Sadly `crate.io <http://crate.io>`_ stopped being a custom PyPI mirror in mid
December which meant I had to rewrite the codebase to use the official PyPI
JSON API. In doing so I lost the ability to get download counts for all
versions or a specific version and instead, could only get a count by day,
week or month.

It was while changing this functionality that I stumbled upon a `ticket from
the shields project <https://github.com/gittip/shields.io/issues/83>`_
mentioning my shields and their poor artistic styling. The ticked mentioned an
`public API <http://shields.io/>`_ for generating these images.

After switching to this API I quickly found from PyPI Pin users on Twitter that
there was an issue in their API, specifically with version number formats.
Version numbers with a format of X.X.X worked fine but X.XX did not. I can only
assume that many other formats didn't work either.

b.repl.ca
=========

While trying to find the source code for shields.io on GitHub I found what they
consider `a newer, better version <http://b.repl.ca/>`_.

I promptly switched to PyPI Pins to use this and queried the authors on GitHub
to make sure the API was meant to be public and usable, thankfully it was.

Eggs, wheels and licenses
=========================

With this new found image API and the wealth of data in the PyPI JSON API I
quickly decided to leverage it as much as I could and thus the egg, wheel and
license shields were created.

The tech stack remains the same, I still cache all successful image requests
using Varnish to limit the impact on my Tornado servers and on the shields.io
service. I look forward to adding more shields and functionality in the future.

You can access this set of services `on PyPI Pins <https://pypip.in>`_.