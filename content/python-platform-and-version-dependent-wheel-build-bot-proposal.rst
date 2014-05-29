Python platform and version dependent wheel build bot proposal
##############################################################
:date: 2014-05-26 23:00
:author: kura
:category: coding
:tags: python, wheel
:slug: python-platform-and-version-dependent-wheel-build-bot-proposal

Abstract
========

This proposal describes a build system for generating "wheel" archives and is
very, very informal. This plan was drawn up after a random dicussion with
Jannis Liedel on Twitter and IRC.

Wheel files can be platform and Python-version dependent, a way of generating
these files automatically needs to be created and linked to the Packaging
Index (PyPI.)

Design
======

After discussions with Jannis, I believe the simplest
solution would likely be the best solution for this problem. As such, I feel
that using a custom-build, lightweight solution makes more sense than using
something like buildbot.

Technology
----------

I feel the platform should leverage existing Python packages that are tried,
tested and well used in the community. Therefore I feel we should use a
combination of the following;

- RabbitMQ for queueing builds
- Celery for building wheels and
- pyenv for managing multiple Python versions

Operating systems
-----------------

I lack any understanding of Windows or Mac OS but, I believe the initial plan
should cover OS X and Linux, using a distro such as Ubuntu for building Linux
packages.

This way we can at least have wheels being built for OS X and Linux and work
on a plan to implement a Windows solution.

PyPI
====

My knowledge of PyPI internals are rather lacking, therefore I have no decided
how packages are passed to the build system to have their wheels built and
added to the PyPI warehouse.

To begin with, we could simply provide a web form that allows a developer to
upload an sdist archive and be provided links to download their generated
wheel files.

While this is not a good long term solution, it would at least allow for
testing of the build platform and for integration in to PyPI itself to be
fully discussed and implemented.

Notes
=====

This document is just a set of thoughts and ideas for how to do this, I'd
really like to get any feedback about this so we can action it and get
something going.
