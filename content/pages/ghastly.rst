Ghastly - A theme for Pelican
#############################
:date: 2014-05-26 23:00
:author: kura
:slug: ghastly

.. figure:: /images/gastly.png
    :alt: Gastly, the Ghost Pokemon

    (Image by `Raiba-art <http://raiba-art.deviantart.com/art/Gastly-294533100>`__)

.. contents::
    :backlinks: none

Introduction
============

I'd like to introduce Ghastly, a clean and minimal, lightweight theme for the
`Pelican <http://getpelican.com>`__ blogging platform.

Ghastly is based heavily off of Casper, the default theme for
`Ghost <https://ghost.org>`__.


It's name is derived from the D&D monster, the Ghast and Gastly, the
Pokemon.


Features
========

- Disqus
- Pygments
- CSS & JS minifying using webassets
- Share buttons
- Custom 404 page

Missing Features
----------------

- Templates are free from all tracking engines like Google Analytics,
  although adding tracking is as simple as editing the HTML.

Design concessions
==================

The Casper theme is designed purely for blog posts and as such it is hard
to easily create any kind of menu for it without ruining the overall design.

I continued this with Ghastly because to me, the articles are more important
than a menu.

This does mean pages become quite pointless.

Typography
==========

.. figure:: /images/firasans.png
    :alt: FiraSans map of the World

    (Image by `the guys at Carrois, creators of FiraSans <http://dev.carrois.com/fira-3-1/>`__)

The guys at `Carrois <http://dev.carrois.com/fira-3-1/>`__ created FiraSans for
Mozilla and released it to the world for free.

The Ghastly theme uses both FiraSans for general typography and FiraMono for
`code`, `kbd`, `pre` and `samp` blocks.

    This is an example of the FiraSans font

::

    This is an example of FiraMono

Screenshots
===========

.. image:: /images/ghastly-homepage.png
    :alt: An example of the homepage

.. image:: /images/ghastly-article1.png
    :alt: An example of article content

.. image:: /images/ghastly-article2.png
    :alt: An example of article content

.. image:: /images/ghastly-article3.png
    :alt: An example of article content

Requirements
============

- pelican
- webassets
- cssmin
- pelican webassets from `pelican-plugins <https://github.com/getpelican/pelican-plugins/tree/master/assets>`__

.. code:: bash

    pip install pelican webassets cssmin

Installation
============

You can find Ghastly `on GitHub <https://github.com/kura/ghastly>`__ and you
can find installation instructions for themes in the `pelican documentation
<http://docs.getpelican.com/en/latest/pelican-themes.html>`__.

Configuration
=============

.. code:: python

    THEME = 'ghastly'
    DIRECT_TEMPLATES = (('index', 'archives', '404'))

License
=======

Ghastly is released under the `MIT license <https://github.com/kura/ghastly/blob/master/LICENSE>`__.
