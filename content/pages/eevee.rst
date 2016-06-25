Eevee -- A Material Design theme for Pelican
############################################
:slug: eevee

.. image:: /images/eeveelutions.png
    :alt: Eevee, the Pokémon
    :align: center

.. contents::
    :backlinks: none

Introduction
============

Eevee is a theme for `Pelican <http://getpelican.com>`_, based on Google's
`Material Design <https://material.google.com/>`_ specification.

It is named after the Pokémon `Eevee
<http://www.pokemon.com/uk/pokedex/eevee>`_ because -- like the Pokémon Eevee
-- it can evolve in to many 'elemental types.'

.. role:: blue-grey
.. role:: pink

By default the colour scheme is :blue-grey:`blue grey` for the primary and
:pink:`pink` for the accent, both of these colours are configurable.

Features
========

- Built around Google's Material Design specification,
- configurable colour scheme,
- DNS prefetching,
- comments from Disqus or Muut,
- share buttons for Twitter, Facebook and Google+,
- Twitter and Open Graph meta tags,
- CSS minifying via webassets and cssmin,
- analytics from Google Analytics and Piwik,
- easy menu and footer customisation,
- custom 404 error page,
- includes Material Icons, Font Awesome and Roboto font,
- no additional javascript loading, except if you enable Google Analytics
  or Piwik,
- and allows upgrading of with `getmdl.io's Material
  Javascript <https://getmdl.io/started/index.html#download>`__.

Typography
==========

.. image:: /images/eevee-typography.png
    :alt: Eevee Typography
    :align: center

Google's `Roboto <https://material.google.com/style/typography.html>`_ font is
used for typography, `Material Icons <https://design.google.com/icons/>`_ and
`Font Awesome <http://fontawesome.io/icons/>`_ are included too.

Screenshots
===========

.. lightbox::
    :thumb: /images/eevee-homepage-thumb.png
    :large: /images/eevee-homepage.png
    :alt: Homepage
    :caption: Homepage
    :align: center

.. lightbox::
    :thumb: /images/eevee-footer-thumb.png
    :large: /images/eevee-footer.png
    :alt: Footer
    :caption: Footer
    :align: center

.. lightbox::
    :thumb: /images/eevee-pagination-thumb.png
    :large: /images/eevee-pagination.png
    :alt: Pagination
    :caption: Pagination
    :align: center

.. lightbox::
    :thumb: /images/eevee-article-header-thumb.png
    :large: /images/eevee-article-header.png
    :alt: Article header
    :caption: Article header
    :align: center

.. lightbox::
    :thumb: /images/eevee-article-header-thumb.png
    :large: /images/eevee-article-header.png
    :alt: Article header
    :caption: Article header
    :align: center

.. lightbox::
    :thumb: /images/eevee-disqus-thumb.png
    :large: /images/eevee-disqus.png
    :alt: Disqus
    :caption: Disqus
    :align: center

.. lightbox::
    :thumb: /images/eevee-pygments-thumb.png
    :large: /images/eevee-pygments.png
    :alt: Pygments
    :caption: Pygments
    :align: center

Requirements
============

- pelican
- webassets
- cssmin
- pelican webassets from `pelican-plugins
  <https://github.com/getpelican/pelican-plugins/tree/master/assets>`_

.. code-block:: bash

    pip install pelican webassets cssmin

Installation
============

You can find Eevee `on GitHub <https://github.com/kura/eevee>`__ and you can
find installation instructions for themes in the `pelican documentation
<http://docs.getpelican.com/en/latest/pelican-themes.html>`_.

Configuring the primary and accent colours
==========================================

The primary and accent colours are configured using the ``THEME_PRIMARY`` and
``THEME_ACCENT`` options respectively.

You can find available primary and accent colours on `Material Design Lite
<https://getmdl.io/customize/index.html>`_. This website also shows you accents
that won't work well with the primary colour you choose.

.. code-block:: python

    THEME_PRIMARY = 'blue'

.. code-block:: python

    THEME_ACCENT = 'amber'

By default the colour scheme is :blue-grey:`blue grey` for the primary and
:pink:`pink` for the accent.

.. code-block:: python

    THEME_PRIMARY = 'blue_grey'
    THEME_ACCENT = 'pink'

Header and footer options
=========================

Header
------

To configure links in the header, use the ``MENUITEMS`` option.

.. code-block:: python

    MENUITEMS = (('Contact', '/contact/'), ('Software', '/software/'),
                 ('Donate', '/donate/'),
                 ('.onion', 'http://omgkuraio276g5wo.onion/'))

Using ``DISPLAY_PAGES_ON_MENU`` will automatically add pages to the menu.

.. code-block:: python

    DISPLAY_PAGES_ON_MENU = True

Footer
------

You can display links in the footer, by default this option is enabled but
can be turned off using the ``MEGA_FOOTER`` option. See the `Screenshots`_
section for an example of the mega footer.

.. code-block:: python

    MEGA_FOOTER = True  # default
    MEGA_FOOTER = False  # disable the footer

Up to four columns can be displayed in the footer.

The first column displays the links from ``MENUITEMS``.

.. code-block:: python

    MENUITEMS = (('Contact', '/contact/'), ('Software', '/software/'),
                 ('Donate', '/donate/'),
                 ('.onion', 'http://omgkuraio276g5wo.onion/'))

Using ``DISPLAY_PAGES_ON_MENU`` will automatically add pages to the menu.

.. code-block:: python

    DISPLAY_PAGES_ON_MENU = True

The second column displays categories, this is enabled using
``DISPLAY_CATEGORIES_ON_MENU``.

.. code-block:: python

    DISPLAY_CATEGORIES_ON_MENU = True

The third column displays social links from ``SOCIAL``.

.. code-block:: python

    SOCIAL = (('Github', 'https://github.com/kura'),
              ('Twitter', 'https://twitter.com/kuramanga'))

And finally, the fourth column displays links from ``LINKS``.

.. code-block:: python

    LINKS = (('blackhole.io', 'https://blackhole.io'), )

The footer will scale based on options you configure, so if you set
``MENUITEMS`` and ``LINKS`` but not ``SOCIAL``, there will be no gap.

Adding table of contents to articles and pages
==============================================

A table of contents section is added to an article or page if it exists
as a variable called ``toc`` in the article or page object.

The `extract_toc
<https://github.com/getpelican/pelican-plugins/tree/master/extract_toc>`_ adds
a ``toc`` option for RST and Markdown content.

The extract_toc plugin adds an ugly header element by default, I have a
modified version `on GitHub
<https://github.com/kura/kura.io/tree/master/plugins/extract_toc>`__ that
returns nicer HTML.

Using Disqus or Muut for comments
=================================

You can only enable `Disqus <https://disqus.com/home/>`__ or `Muut
<https://muut.com/>`__, not both. Disqus takes priority over Muut
in terms of how the configuration variables are handled.

Disqus
------

.. code-block:: python

    DISQUS_SITENAME = 'somethinghere'

Setting this option will enable Disqus for articles.

Muut
----

.. code-block:: python

    MUUT_SITENAME = 'somethinghere'

Setting this option will enable Muut for articles.

Sharing options
===============

Share buttons
-------------

By default three share buttons are configured;

- Twitter,
- Facebook
- and Google+

These buttons will appear on all articles and pages.

If you have comments enabled either using Disqus or Muut, on articles a fourth
button will be shown which shows the user comments for the current article.

Configuration options
---------------------

.. code-block:: python

    USE_OPEN_GRAPH = True

If set, Open Graph meta tags will be added.

.. code-block:: python

    USE_TWITTER_CARDS = True

If set, Twitter meta tags will be added.

.. code-block:: python

    TWITTER_USERNAME = 'kuramanga'

Used in conjunction with ``USE_TWITTER_CARDS``, adds the "via" meta tag.

Adding an image to Open Graph and Twitter meta tags
---------------------------------------------------

There are two ways of adding an image to Twitter and Open Graph so that when
someone shares your content, an image will be added too.

You can add ``og_image`` to the file metadata of an article or page, allowing
you to configure and image to use per item.

.. code-block:: rst

    Title
    =====
    :slug: example
    :og_image: /images/example.png

    Example content

Or you can set ``OPEN_GRAPH_IMAGE`` to an image location.

.. code-block:: python

    OPEN_GRAPH_IMAGE = '/images/example.png'

Using Google Analytics or Piwik
===============================

Setting the ``GOOGLE_ANALYTICS`` option will enable Google Analytics,
alternatively you can set ``PIWIK_SITE_ID``, ``PIWIK_URL`` and
``PIWIK_SSL_URL`` to use Piwik for analytics instead.

.. code-block:: python

    GOOGLE_ANALYTICS = 'abc1234'

.. code-block:: python

    PIWIK_SITE_ID = '123456'
    PIWIK_URL = 'example.com'
    # PIWIK_SSL_URL = ''  # Defaults to https://PIWIK_URL

Enabling feeds
==============

You can use the ``FEED_RSS`` and ``FEED_ATOM`` options to enable RSS and Atom
feeds respectively.

.. code-block:: python

    FEED_RSS = 'feeds/rss.xml'

.. code-block:: python

    FEED_ATOM = 'feeds/atom.xml'

Additional tweaks and modifications
===================================

Additional things you can tweak and modify are available on `kura.io
</c/eevee/>`__.

License
=======

Eevee is released under the `MIT license
<https://github.com/kura/eevee/blob/master/LICENSE>`_ which is also outlined
below.

::

    (The MIT License)

    Copyright (c) 2016 Kura

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the 'Software'), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
