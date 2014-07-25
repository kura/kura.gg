New pypip.in shields and styling
################################
:date: 2014-07-25 01:00
:author: kura
:category: coding
:tags: python, pypi, shields
:slug: new-pypip.in-shields-and-styling

.. contents::
    :backlinks: none

.. image:: https://pypip.in/d/blackhole/badge.svg?style=flat
   :alt: Downloads for blackhole
   :class: shield

.. image:: https://pypip.in/v/blackhole/badge.svg?style=flat
   :alt: Latest version of blackhole
   :class: shield

.. image:: https://pypip.in/egg/blackhole/badge.svg?style=flat
   :alt: blackhole's egg status
   :class: shield

.. image:: https://pypip.in/wheel/blackhole/badge.svg?style=flat
   :alt: blackhole's wheel status
   :class: shield

.. image:: https://pypip.in/license/blackhole/badge.svg?style=flat
   :alt: blackhole's license
   :class: shield

Supported Python versions
=========================

This one is generated from the list of classifiers you provide to PyPI.

.. image:: https://pypip.in/py_versions/blackhole/badge.svg?style=flat
   :alt: Supported Python versions
   :class: shield

If no Python version classifiers exist, it defaults to Python 2.7. This is
because really, Python 3 is not widely used in production or supported by
libraries.

Python implementation(s)
========================

I think this one is really cool. Chances are you're unlikely to get more than
two supported implementations, like CPython and PyPy or CPython and Stackless.

The shield uses the Python implementation classifiers to generate this shield.
It supports all classifiers that PyPI supports (CPython, Jython, Iron Python,
PyPy and Stackless) and defaults to CPython is none are set.

.. image:: https://pypip.in/implementation/blackhole/badge.svg?style=flat
   :alt: Supported Python implementations
   :class: shield

Styling changes
===============

This change is simply because of the upgrade of the shields library. This
allows us to use the default rounded badges like below.

.. image:: https://pypip.in/py_versions/blackhole/badge.svg
   :alt: Supported Python versions
   :class: shield

But also allow you to use a much nicer, cleaner, flat styling like the ones
used on this page.

SVG > PNG
=========

The final change is that by default pypip.in now returns SVG images by default,
rather than PNG. You can of course get the badge in whatever format you wish.

.. code::

    https://pypip.in/download/<PACKAGE>/badge.<MIMETYPE>
