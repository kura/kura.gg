Hauntr - A theme for Pelican
############################
:slug: hauntr

.. figure:: /images/haunter.png
    :alt: Haunter, the evolved Pokemon form of Gastly
    :align: center

    (Image by `Kawiku <https://kawiku.deviantart.com/art/Haunter-350580512>`__)

.. contents::
    :backlinks: none

Introduction
============

Hauntr is a minimal, lightweight and clean theme for the
`Pelican <https://getpelican.com>`__ blogging platform.

It is named after the Pokémon 'Haunter' because it is a modified version
(you might say evolved) of my previous theme, `Ghastly
</ghastly/>`__.

Features
========

- Disqus
- Pygments
- CSS minifying using webassets
- Share buttons
- Custom 404 page

Typography
==========

.. figure:: /images/firasans.png
    :alt: FiraSans map of the World
    :align: center

    (Image by `the guys at Carrois, creators of FiraSans <https://dev.carrois.com/fira-3-1/>`__)

The guys at `Carrois <https://dev.carrois.com/fira-3-1/>`__ created FiraSans for
Mozilla and released it to the world for free.

The Hauntr theme uses both FiraSans for general typography and FiraMono for
`code`, `kbd`, `pre` and `samp` blocks.

Screenshots
===========

.. figure:: /images/hauntr-homepage-thumb.png
    :alt: An example of the homepage
    :align: center
    :target: /images/hauntr-homepage.png

    An example of the homepage

.. figure:: /images/hauntr-article1-thumb.png
    :alt: An example of article content
    :align: center
    :target: /images/hauntr-article1.png

    An example of article content

.. figure:: /images/hauntr-article2-thumb.png
    :alt: An example of article content
    :align: center
    :target: /images/hauntr-article2.png

    An example of article content

.. figure:: /images/hauntr-article3-thumb.png
    :alt: An example of article content
    :align: center
    :target: /images/hauntr-article3.png

    An example of article content

Requirements
============

- pelican
- webassets
- cssmin
- pelican webassets from `pelican-plugins <https://github.com/getpelican/pelican-plugins/tree/master/assets>`__

.. code-block:: bash

    pip install pelican webassets cssmin

Installation
============

You can find Hauntr `on GitHub <https://github.com/kura/hauntr>`__ and you
can find installation instructions for themes in the `pelican documentation
<https://docs.getpelican.com/en/latest/pelican-themes.html>`__.

Configuration
=============

.. code-block:: python

    THEME = 'hauntr'
    DIRECT_TEMPLATES = (('index', 'archives', '404'))

License
=======

Hauntr is released under the `MIT license <https://github.com/kura/hauntr/blob/master/LICENSE>`__.
