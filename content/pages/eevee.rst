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

Eevee is a theme for `Pelican <http://getpelican.com>`__, based on Google's
`Material Design <https://material.google.com/>`__ specification.

It is named after the Pokémon `Eevee
<http://www.pokemon.com/uk/pokedex/eevee>`__ because -- like the Pokémon -- it
can evolve in to many 'elemental types.'

.. role:: blue-grey
.. role:: pink

By default the colour scheme is :blue-grey:`blue grey` for the primary and
:pink:`pink` for the accent, both of these colours are configurable.

Features
========

- Built around `Google's Material Design <https://material.google.com/>`__
  specification,
- configurable colour scheme,
- responsive layout with mobile friendly header and navigation scheme,
- inclusion of a ``custom.css`` file allowing easy overwriting of the theme
  without breaking the base CSS,
- `DNS prefetch`_,
- comments via `Disqus <https://disqus.com/>`__ or `Muut
  <https://muut.com/>`__,
- share buttons for Twitter, Facebook, Google+, email and comments,
- Twitter and Open Graph meta tags,
- CSS and JS minifying via `webassets
  <https://webassets.readthedocs.io/en/latest/>`__, cssmin and jsmin,
- analytics from `Google Analytics <https://analytics.google.com>`__,
  `Piwik <https://piwik.org/>`__, `GoSquared <https://www.gosquared.com/>`__
  and `Open Web Analytics <http://www.openwebanalytics.com/>`__,
- easy customisation, including menus and footer,
- custom 404 error page,
- `Microdata <https://en.wikipedia.org/wiki/Microdata_(HTML)>`__,
- `Aria <https://en.wikipedia.org/wiki/WAI-ARIA>`__ accessibility,
- includes `Material Icons <https://design.google.com/icons/>`__, `Font Awesome
  <http://fontawesome.io/>`__ and `Roboto font
  <https://typecast.com/preview/google/Roboto>`__ and,
- seamless upgrading with `getmdl.io's Material Javascript
  <https://getmdl.io/started/index.html#download>`__.

Plugins supported out-of-the-box
================================

Eevee ships with all the HTML and CSS required for the following plugins but
does not need any of them to function. If a plugin is supported but not used,
the HTML, CSS and JavaScript simply won't be included.

- `assets
  <https://github.com/getpelican/pelican-plugins/tree/master/assets>`__,
- `extract_toc
  <https://github.com/getpelican/pelican-plugins/tree/master/extract_toc>`__,
- `headerid
  <https://github.com/getpelican/pelican-plugins/tree/master/headerid>`__,
- `lightbox
  <https://github.com/getpelican/kura/lightbox>`__,
- `neighbors
  <https://github.com/getpelican/pelican-plugins/tree/master/neighbors>`__,
- `related_posts
  <https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`__,
- `series
  <https://github.com/getpelican/pelican-plugins/tree/master/series>`__ and,
- `tipue_search
  <https://github.com/getpelican/pelican-plugins/tree/master/tipue_search>`__.

Typography
==========

.. image:: /images/eevee-typography.png
    :alt: Eevee Typography
    :align: center

Google's `Roboto <https://material.google.com/style/typography.html>`__ font is
used for typography, `Material Icons <https://design.google.com/icons/>`__ and
`Font Awesome <http://fontawesome.io/icons/>`__ are included too.

Screenshots
===========

.. lightbox::
    :thumb: /images/eevee-homepage-thumb.png
    :large: /images/eevee-homepage.png
    :alt: Homepage
    :caption: Homepage
    :align: center

.. lightbox::
    :thumb: /images/eevee-homepage-separator-thumb.png
    :large: /images/eevee-homepage-separator.png
    :alt: Homepage separator
    :caption: Homepage separator
    :align: center

.. lightbox::
    :thumb: /images/eevee-homepage-pagination-thumb.png
    :large: /images/eevee-homepage-pagination.png
    :alt: Homepage pagination
    :caption: Homepage pagination
    :align: center

.. lightbox::
    :thumb: /images/eevee-mega-footer-thumb.png
    :large: /images/eevee-mega-footer.png
    :alt: Mega footer
    :caption: Mega footer
    :align: center

.. lightbox::
    :thumb: /images/eevee-article-top-thumb.png
    :large: /images/eevee-article-top.png
    :alt: Article header
    :caption: Article header
    :align: center

.. lightbox::
    :thumb: /images/eevee-article-bottom-thumb.png
    :large: /images/eevee-article-bottom.png
    :alt: Article footer
    :caption: Article footer
    :align: center

.. lightbox::
    :thumb: /images/eevee-headerlinks-thumb.png
    :large: /images/eevee-headerlinks.png
    :alt: Article header links
    :caption: Article header links
    :align: center

.. lightbox::
    :thumb: /images/eevee-related-author-card-thumb.png
    :large: /images/eevee-related-author-card.png
    :alt: Related articles and author card
    :caption:
    :align: center

.. lightbox::
    :thumb: /images/eevee-toc-series-thumb.png
    :large: /images/eevee-toc-series.png
    :alt: Table of contents
    :caption: Table of contents
    :align: center

.. lightbox::
    :thumb: /images/eevee-archives-thumb.png
    :large: /images/eevee-archives.png
    :alt: Archives
    :caption: Archives
    :align: center

.. lightbox::
    :thumb: /images/eevee-search-thumb.png
    :large: /images/eevee-search.png
    :alt: Search
    :caption: Search
    :align: center

Requirements
============

.. code-block:: bash

    pip install pelican

Installation
============

You can find Eevee `on GitHub <https://github.com/kura/eevee>`__ and you can
find installation instructions for themes in the `pelican documentation
<http://docs.getpelican.com/en/latest/pelican-themes.html>`__.

.. _colours:

Configuring the primary and accent colours
==========================================

The primary and accent colours are configured using the ``THEME_PRIMARY`` and
``THEME_ACCENT`` options respectively.

You can find available primary and accent colours on `Material Design Lite
<https://getmdl.io/customize/index.html>`__. This website also shows you
accents that won't work well with the primary colour you choose.

.. code-block:: python

    THEME_PRIMARY = 'blue'

.. code-block:: python

    THEME_ACCENT = 'amber'

By default the colour scheme is :blue-grey:`blue grey` for the primary and
:pink:`pink` for the accent.

.. code-block:: python

    THEME_PRIMARY = 'blue_grey'
    THEME_ACCENT = 'pink'

Responsive mobile design
========================

By default Eevee will modify it's design -- specifically the logo and menu --
on smaller screened devices, like cell phones or tablets. A ``Home`` link is
automatically added to the navigation list.

Customising the CSS
===================

`Inside the Eevee static folder is a custom.css file
<https://github.com/kura/eevee/tree/master/static/css>`__. Anything added to
this file will overwrite any of the core CSS. You can use this file to
modify any part of the interface you wish, including changing the Pygments
CSS.

This allows you to tinker with the design as much as you like without breaking
the core theme.

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

Customising the copyright notice and disclaimer
===============================================

You can change the disclaimer and copyright notice displayed in the footer with
the following variables.

.. code-block:: python

    DISCLAIMER = 'Powered by love &amp; rainbow sparkles.'
    COPYRIGHT = 'Source code and content are released under the <a href="/license/">MIT license</a>.'

You can see either or both to ``False`` to disable these notices being
displayed.

.. code-block:: python

    DISCLAIMER = False
    COPYRIGHT = False

The default values for these are as below, although you are under no
obligation to keep either of them.

.. code-block:: python

    DISCLAIMER = 'Powered by love &amp; rainbow sparkles.'
    COPYRIGHT = '<a href="https://kura.io/eevee/" title="Eevee">Eevee</a> theme by <a href="https://kura.io/" title="kura.io">kura.io</a>'

Archives
========

Eevee supports full archives and archives broken down by year and month.

To enable the full archive section, you need to enable the relevant setting in
your ``pelicanconf.py`` file.

.. code-block:: python

    ARCHIVES_URL = 'archives.html'
    ARCHIVES_SAVE_AS = 'archives.html'

Enabling the periodic archives for year and/or month is as simple as enabling
their respective options in ``pelicanconf.py``

.. code-block:: python

    YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
    MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

More information on archive settings can be found in the
`Pelican documentation
<http://docs.getpelican.com/en/3.6.3/settings.html#url-settings>`__.

Adding table of contents to articles and pages
==============================================

A table of contents section is added to an article or page if it exists
as a variable called ``toc`` in the article or page object.

The `extract_toc
<https://github.com/getpelican/pelican-plugins/tree/master/extract_toc>`__
adds a ``toc`` option for RST and Markdown content.

The extract_toc plugin adds an ugly header element by default, I have a
modified version `on GitHub
<https://github.com/kura/kura.io/tree/master/plugins/extract_toc>`__ that
returns nicer HTML.

Adding author card to articles
==============================

The author card is disabled by default, below are instructions on enabling it
and customising it.

Enabling the author card
------------------------

Enabling the author card is as simple as setting an option in
``pelicanconf.py``.

.. code-block:: python

    USE_AUTHOR_CARD = True

You can disable it by setting to ``False`` or removing the setting entirely.

.. code-block:: python

    USE_AUTHOR_CARD = False

Using your own avatar
---------------------

A default avatar placeholder is provided with the theme, you can easily use
your own avatar by setting an option in ``pelicanconf.py``.

.. code-block:: python

    AUTHOR_CARD_AVATAR = '/images/kura.png'

The maximum size that you should use are 250x250 pixels.

Setting a description
---------------------

Like all the other options above, setting a description for your author card
requires a single config option.

.. code-block:: python

    AUTHOR_CARD_DESCRIPTION = 'My name is Kura and I break things.'

You can add HTML and other various things to this description.

Social buttons
--------------

By default, the author card section will display links from your ``SOCIAL``
list.

This isn't always what you want though.

The ``SOCIAL`` list is used in other parts of the theme and the format may not
look good added to your author card.

To make things more flexible, the author card section can have it's own social
links.

.. code-block:: python

    AUTHOR_CARD_SOCIAL = (('<i class="fa fa-github aria-hidden="true"></i>',
                   'https://github.com/kura'),
                  ('<i class="fa fa-twitter aria-hidden="true"></i>',
                   'https://twitter.com/kuramanga'), )

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

Comments on pages
-----------------

You can display comments on pages as well as articles with the following
option. By default this is disabled.

.. code-block:: python

    COMMENTS_ON_PAGES = True

Sharing options
===============

Share buttons
-------------

By default four share buttons are configured;

- Twitter,
- Facebook,
- Google+,
- and Email.

These buttons will appear on all articles and pages.

If you have comments enabled either using Disqus or Muut, on articles a fifth
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

Or you can set ``OPEN_GRAPH_IMAGE`` to an image location in the
``pelicanconf.py`` settings file and adding the relevant directory to the
``STATIC_PATHS`` and ``EXTRA_PATH_METADATA`` settings.

.. code-block:: python

    OPEN_GRAPH_IMAGE = '/images/example.png'
    STATIC_PATHS = [
        # ...
        'images',
        # ...
    ]
    EXTRA_PATH_METADATA = {
        # ...
        'images': {'path': 'images'},
        # ...
    }

Using Google Analytics, Piwik, Open Web Analytics and GoSquared
===============================================================

All four of these options can be enabled at the same time, should you wish to
do so.

Google Analytics
----------------

.. code-block:: python

    GOOGLE_ANALYTICS = 'abc1234'

Piwik
-----

.. code-block:: python

    PIWIK_SITE_ID = '123456'
    PIWIK_URL = 'example.com'
    # PIWIK_SSL_URL = ''  # Defaults to https://PIWIK_URL

Open Web Analytics
------------------

.. code-block:: python

    OWA_SITE_ID = '123456'
    OWA_URL = 'https://example.com/owa/'

GoSquared
---------

.. code-block:: python

    GOSQUARED_SITENAME = '123456'

Enabling feeds
==============

You can use the ``FEED_RSS`` and ``FEED_ATOM`` options to enable RSS and Atom
feeds respectively.

.. code-block:: python

    FEED_RSS = 'feeds/rss.xml'

.. code-block:: python

    FEED_ATOM = 'feeds/atom.xml'

Feed menu item
--------------

Enabling either ``FEED_RSS`` or ``FEED_ATOM`` will automatically add a menu
item for that feed. If ``MEGA_FOOTER`` is also enabled a link to the feed will
be added there too.

Eevee prefers RSS over ATOM, if you enable both feed types a menu item will
only be created for RSS, although both feeds will be added as alternate link
tags.

Minimising/compressing CSS and JavaScript
=========================================

To minimise/compress all CSS or JavaScript, simply install the `assets <https://github.com/getpelican/pelican-plugins/tree/master/assets>`__ plugin.

Eevee is configured to automatically compress all CSS and JavaScript files it
uses if the assets plugin is enabled, including files related to the search_
functionality.

.. code-block:: python

    PLUGINS = [
        # ...
        'assets',
        # ...
    ]

.. _search:

Enabling search functionality
=============================

Eevee is configured to work with `tipue_search
<https://github.com/getpelican/pelican-plugins/tree/master/tipue_search>`__
out-of-the-box, all you need to do is enable the plugin and add the search
template setting.

.. code-block:: python

    PLUGINS = [
        # ...
        'tipue_search',
        # ...
    ]

    DIRECT_TEMPLATES = [
        # ...
        'search',
        # ...
    ]

Category and tag pages
======================

To display all articles in specific categories or tags, you need to add the
relevant settings.

An example for categories is below.

.. code-block:: python

    CATEGORY_URL = 'category/{slug}/'
    CATEGORY_SAVE_AS = 'category/{slug}/index.html'
    CATEGORIES_URL = 'categories/'
    CATEGORIES_SAVE_AS = 'categories/index.html'
    DIRECT_TEMPLATES = [
        # ...
        'categories',
        # ...
    ]

And below is an example for tags.

.. code-block:: python

    TAG_URL = 'tag/{slug}/'
    TAG_SAVE_AS = 'tag/{slug}/index.html'
    TAGS_URL = 'tags/'
    TAGS_SAVE_AS = 'tags/index.html'
    DIRECT_TEMPLATES = [
        # ...
        'tags',
        # ...
    ]

Adding permalinks to headlines
==============================

reStructuredText does not add anchors to headings by default, adding reference
links on headings means you can send the link to someone and have the browser
automatically display the relevant section.

Eevee is configured out-of-the-box to support adding these references using the
`headerid
<https://github.com/getpelican/pelican-plugins/tree/master/headerid>`__
plugin.

Advanced pagination of articles
===============================

By default, Eevee will display pagination links on the index page of articles.
Enabling the `neighbors
<https://github.com/getpelican/pelican-plugins/tree/master/neighbors>`__ will
automatically add a previous and next button to the article page, allowing
pagination without going back to the index page.

The default Pelican pagination settings are not very pleasing, for more
information on how to customise them to better and be more intuitive please
look at the `Pelican documentation
<http://docs.getpelican.com/en/3.6.3/settings.html#using-pagination-patterns>`__.-

DNS prefetch
============

`DNS prefetching
<https://developer.mozilla.org/en-US/docs/Web/HTTP/Controlling_DNS_prefetching>`__
is enabled by default and managed automatically.

The following features will have respective DNS prefetch settings that will
be applied if the feature is enabled;

- Disqus,
- Piwik,
- GoSquared,
- Google Analytics and,
- Open Web Analytics.

Additional tweaks and modifications
===================================

Additional things you can tweak and modify are available on `kura.io
</category/eevee/>`__.

License
=======

Eevee is released under the `MIT license
<https://github.com/kura/eevee/blob/master/LICENSE>`__ which is also outlined
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
