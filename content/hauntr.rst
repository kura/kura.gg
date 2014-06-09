Hauntr - A theme for Pelican
############################
:date: 2014-06-09 18:00
:author: kura
:tags: pelican
:slug: hauntr

.. contents::

.. figure:: /images/haunter.png
    :alt: Haunter, the evolved Pokemon form of Gastly

    (Image by `Kawiku <http://kawiku.deviantart.com/art/Haunter-350580512>`__)

Introduction
============

Hauntr is a minimal, lightweight and clean theme for the
`Pelican <http://getpelican.com>`__ blogging platform.

It is named after the Pokemon 'Haunter' because it is a modified version
(you might say evolved) of my previous theme, `Ghastly
<https://kura.io/ghastly/>`__.

Features
========

- Disqus
- Pygments
- CSS minifying using webassets
- Share buttons
- Custom 404 page

Typography
==========

.. figure:: https://raw.githubusercontent.com/kura/hauntr/master/firasans.png
    :alt: FiraSans map of the World

    (Image by `the guys at Carrois, creators of FiraSans <http://dev.carrois.com/fira-3-1/>`__)

The guys at `Carrois <http://dev.carrois.com/fira-3-1/>`__ created FiraSans for
Mozilla and released it to the world for free.

The Hauntr theme uses both FiraSans for general typography and FiraMono for
`code`, `kbd`, `pre` and `samp` blocks.

Screenshots
===========

.. image:: /images/hauntr-homepage.png
    :alt: An example of the homepage

.. image:: /images/hauntr-article1.png
    :alt: An example of article content

.. image:: /images/hauntr-article2.png
    :alt: An example of article content

.. image:: /images/hauntr-article3.png
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

You can find Ghastly `on GitHub <https://github.com/kura/hauntr>`__ and you
can find installation instructions for themes in the `pelican documentation
<http://docs.getpelican.com/en/latest/pelican-themes.html>`__.

Configuration
=============

.. code:: python

    THEME = 'hauntr'
    DIRECT_TEMPLATES = (('index', 'archives', '404'))

License
=======

Hauntr is released under the `MIT license <https://github.com/kura/hauntr/blob/master/LICENSE>`__.
