Eevee -- A Material Design theme for Pelican
############################################
:slug: eevee

.. image:: /images/eeveelutions.png
    :alt: Eevee, the Pokémon
    :align: center

.. contents::
    :backlinks: none

.. role:: blue-grey
.. role:: pink

Introduction
============

Eevee is a theme for `Pelican <http://getpelican.com>`__, based on Google's
`Material Design <https://material.google.com/>`__ specification. It is named
after the Pokémon `Eevee <http://www.pokemon.com/uk/pokedex/eevee>`__ because
-- like the Pokémon -- it can evolve in to many 'elemental types.'

Features
========

- Built around `Google's Material Design <https://material.google.com/>`__
  specification on top of Goole's `Material Design Lite library
  <https://github.com/google/material-design-lite>`__,
- configurable colour scheme (see `Primary and accent colours`_),
- responsive layout with mobile friendly header and navigation scheme,
- inclusion of a ``custom.css`` file allowing easy overwriting of the theme
  without breaking the base CSS (see `Custom CSS`_),
- `DNS prefetch`_ (see `DNS prefetch`_),
- comments via `Disqus <https://disqus.com/>`__ or `Muut
  <https://muut.com/>`__ (see `Disqus or Muut for comments`_),
- share buttons for Twitter, Facebook, Google+, email and comments (see
  `Sharing options`_),
- Twitter and Open Graph meta tags (see `Sharing options`_),
- CSS and JS minifying via `webassets
  <https://webassets.readthedocs.io/en/latest/>`__, cssmin and jsmin (see
  `Plugin: Minimise CSS and JavaScript`_),
- analytics from `Google Analytics <https://analytics.google.com>`__,
  `Piwik <https://piwik.org/>`__, `GoSquared <https://www.gosquared.com/>`__
  and `Open Web Analytics <http://www.openwebanalytics.com/>`__ (see
  `Google Analytics, Piwik, Open Web Analytics and GoSquared`_),
- easy customisation, including menus and footer (see `Header and footer
  options`_),
- custom 404 error page,
- `Microdata <https://en.wikipedia.org/wiki/Microdata_(HTML)>`__,
- `Aria <https://en.wikipedia.org/wiki/WAI-ARIA>`__ accessibility,
- includes `Material Icons <https://design.google.com/icons/>`__, `Font Awesome
  <http://fontawesome.io/>`__ and Google's `Roboto font
  <https://typecast.com/preview/google/Roboto>`__ and,
- seamless feature upgrade with Material Design Lite's `Javascript library
  <https://getmdl.io/started/index.html#download>`__.

Plugins supported out-of-the-box
================================

Eevee ships with all the HTML, CSS and JavaScript required for the following
plugins but does not need any of them to function correctly. If a plugin is
supported but not used, the HTML, CSS and JavaScript simply won't be included.

- `assets
  <https://github.com/getpelican/pelican-plugins/tree/master/assets>`__ (see
  `Plugin: Minimise CSS and JavaScript`_ section for more information),
- `extract_toc
  <https://github.com/getpelican/pelican-plugins/tree/master/extract_toc>`__ (
  see `Table of contents for articles and pages`_ section for more
  information),
- `headerid
  <https://github.com/getpelican/pelican-plugins/tree/master/headerid>`__ (see
  `Plugin: Permalinks in headlines`_ section for more information),
- `lightbox
  <https://github.com/kura/lightbox>`__,
- `neighbors
  <https://github.com/getpelican/pelican-plugins/tree/master/neighbors>`__,
- `related_posts
  <https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`__
  (see `Plugin: Related articles`_ section for more information),
- `series
  <https://github.com/getpelican/pelican-plugins/tree/master/series>`__ (see
  `Plugin: Articles in a series`_ section for more information) and,
- `tipue_search
  <https://github.com/getpelican/pelican-plugins/tree/master/tipue_search>`__ (
  see `Plugin: Search functionality`_ section for more information.)

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

.. gallery:: content/images/eevee_page/
    :columns: 3

Installation
============

Download the latest Eevee release
`from GitHub <https://github.com/kura/eevee/releases>`__ and extract it in to
your Pelican website directory and rename the directory to ``eevee``.

Install the theme using ``pelican-themes``.

.. code-block:: bash

    pelican-themes -i eevee

All you need to do after that is set the ``THEME`` variable to ``eevee`` in
your ``pelicanconf.py``.

.. code-block:: python

    THEME = 'eevee'

Customising Eevee
=================

.. _colours:

Primary and accent colours
--------------------------

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

Custom CSS
----------

`Inside the Eevee static folder is a custom.css file
<https://github.com/kura/eevee/tree/master/static/css>`__. Anything added to
this file will overwrite any of the core CSS. You can use this file to
modify any part of the interface you wish, including changing the Pygments
CSS.

This allows you to tinker with the design as much as you like without breaking
the core theme.

Header and footer options
-------------------------

Header
~~~~~~

.. lightbox::
    :thumb: /images/eevee-menu.png
    :large: /images/eevee-menu.png
    :alt: Header menu
    :caption: Header menu
    :align: center

To configure links in the header, use the ``MENUITEMS`` option.

.. code-block:: python

    MENUITEMS = (('Contact', '/contact/'), ('Software', '/software/'),
                 ('Donate', '/donate/'),
                 ('.onion', 'http://omgkuraio276g5wo.onion/'))

Using ``DISPLAY_PAGES_ON_MENU`` will automatically add pages to the menu.

.. code-block:: python

    DISPLAY_PAGES_ON_MENU = True

Footer
~~~~~~

.. lightbox::
    :thumb: /images/eevee-footer-menu-thumb.png
    :large: /images/eevee-footer-menu.png
    :alt: Footer menu
    :caption: Footer menu
    :align: center

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

Setting your own copyright notice and disclaimer
------------------------------------------------

.. lightbox::
    :thumb: /images/eevee-copyright-disclaimer-thumb.png
    :large: /images/eevee-copyright-disclaimer.png
    :alt: Copyright and disclaimer
    :caption: Copyright and disclaimer
    :align: center

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

Table of contents for articles and pages
----------------------------------------

.. lightbox::
    :thumb: /images/eevee-toc.png
    :large: /images/eevee-toc.png
    :alt: Table of contents
    :caption: Table of contents
    :align: center

A table of contents section is added to an article or page if it exists
as a variable called ``toc`` in the article or page object.

The `extract_toc
<https://github.com/getpelican/pelican-plugins/tree/master/extract_toc>`__
adds a ``toc`` option for RST and Markdown content.

The extract_toc plugin adds an ugly header element by default, I have a
modified version `on GitHub
<https://github.com/kura/kura.io/tree/master/plugins/extract_toc>`__ that
returns nicer HTML.

Author card
-----------

.. lightbox::
    :thumb: /images/eevee-author-card.png
    :large: /images/eevee-author-card.png
    :alt: Author card
    :caption: Author card
    :align: center

The author card is disabled by default, below are instructions on enabling it
and customising it.

Enabling the author card
~~~~~~~~~~~~~~~~~~~~~~~~

Enabling the author card is as simple as setting an option in
``pelicanconf.py``.

.. code-block:: python

    USE_AUTHOR_CARD = True

You can disable it by setting to ``False`` or removing the setting entirely.

.. code-block:: python

    USE_AUTHOR_CARD = False

Using your own avatar
~~~~~~~~~~~~~~~~~~~~~

A default avatar placeholder is provided with the theme, you can easily use
your own avatar by setting an option in ``pelicanconf.py``.

.. code-block:: python

    AUTHOR_CARD_AVATAR = '/images/kura.png'

The maximum size that you should use are 250x250 pixels.

Setting a description
~~~~~~~~~~~~~~~~~~~~~

Like all the other options above, setting a description for your author card
requires a single config option.

.. code-block:: python

    AUTHOR_CARD_DESCRIPTION = 'My name is Kura and I break things.'

You can add HTML and other various things to this description.

Social buttons
~~~~~~~~~~~~~~

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

Some default styling rules are included with Eevee, they are as follow:

.. role:: ac-twitter
.. role:: ac-twitter-hover
.. role:: ac-facebook
.. role:: ac-facebook-hover
.. role:: ac-google-plus
.. role:: ac-google-plus-hover
.. role:: ac-github
.. role:: ac-github-hover
.. role:: ac-instagram
.. role:: ac-instagram-hover

+-----------+---------------------------+---------------------------------+
| Site      | Link colour               | Hover colour                    |
+===========+===========================+=================================+
| Twitter   | :ac-twitter:`#039BE5`     | :ac-twitter-hover:`#0277BD`     |
+-----------+---------------------------+---------------------------------+
| Facebook  | :ac-facebook:`#1565C0`    | :ac-facebook-hover:`#0D47A1`    |
+-----------+---------------------------+---------------------------------+
| Google+   | :ac-google-plus:`#F44336` | :ac-google-plus-hover:`#D32F2F` |
+-----------+---------------------------+---------------------------------+
| GitHub    | :ac-github:`#212121`      | :ac-github-hover:`#616161`      |
+-----------+---------------------------+---------------------------------+
| Instagram | :ac-instagram:`#8BC34A`   | :ac-instagram-hover:`#689F38`   |
+-----------+---------------------------+---------------------------------+


You can add your own new styles or overwrite an existing style using the
``href`` selector.

For example, adding a selector style for ``https://kura.io`` would be done
like the example below.

.. code-block:: css

    nav.eevee-ac-author__social a[href^="https://kura.io"] {
      color: #039BE5 !important;
    }

    nav.eevee-ac-author__social a[href^="https://kura.io"]:hover {
      color: #0277BD !important;
    }

Dynamically disabling author card on an article or page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of Eevee version 0.0.12, it is now possible to disable the author card
feature on a per-article or per-page basis using metadata.

Using reStructuredText:

.. code-block:: rst

    Example title
    #############
    :slug: example
    :author_card: False

Using Markdown:

.. code-block:: md

    Title: Example title
    Slug: example
    Author_card: False

Disqus or Muut for comments
---------------------------

You can only enable `Disqus <https://disqus.com/home/>`__ or `Muut
<https://muut.com/>`__, not both. Disqus takes priority over Muut
in terms of how the configuration variables are handled.

Disqus
~~~~~~

.. code-block:: python

    DISQUS_SITENAME = 'somethinghere'

Setting this option will enable Disqus for articles.

Muut
~~~~

.. code-block:: python

    MUUT_SITENAME = 'somethinghere'

Setting this option will enable Muut for articles.

Comments on pages
~~~~~~~~~~~~~~~~~

You can display comments on pages as well as articles with the following
option. By default this is disabled.

.. code-block:: python

    COMMENTS_ON_PAGES = True

Dynamically disabling comments on an article or page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of Eevee version 0.0.12, it is now possible to disable comments on a
per-article or per-page basis using metadata.

Using reStructuredText:

.. code-block:: rst

    Example title
    #############
    :slug: example
    :comments: False

    Example content

Using Markdown:

.. code-block:: markdown

    Title: Example title
    Slug: example
    Comments: False

    Example content

Sharing options
---------------

.. lightbox::
    :thumb: /images/eevee-share-buttons.png
    :large: /images/eevee-share-buttons.png
    :alt: Share buttons
    :caption: Share buttons
    :align: center

Share buttons
~~~~~~~~~~~~~

By default four share buttons are configured;

- Twitter,
- Facebook,
- Google+,
- and Email.

These buttons will appear on all articles and pages.

If you have comments enabled either using Disqus or Muut, on articles a fifth
button will be shown which shows the user comments for the current article.

Options
~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways of adding an image to Twitter and Open Graph so that when
someone shares your content, an image will be added too.

You can add ``og_image`` to the file metadata of an article or page, allowing
you to configure and image to use per item.

Using reStructuredText:

.. code-block:: rst

    Example title
    #############
    :slug: example
    :og_image: /images/example.png

    Example content

Using Markdown:

.. code-block:: markdown

    Title: Example title
    Slug: example
    Og_image: /images/example.png

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

Archives
--------

.. lightbox::
    :thumb: /images/eevee-menu.png
    :large: /images/eevee-menu.png
    :alt: Header menu
    :caption: Header menu
    :align: center

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

Google Analytics, Piwik, Open Web Analytics and GoSquared
---------------------------------------------------------

All four of these options can be enabled at the same time, should you wish to
do so.

Google Analytics
~~~~~~~~~~~~~~~~

.. code-block:: python

    GOOGLE_ANALYTICS = 'abc1234'

Piwik
~~~~~

.. code-block:: python

    PIWIK_SITE_ID = '123456'
    PIWIK_URL = 'example.com'
    # PIWIK_SSL_URL = ''  # Defaults to https://PIWIK_URL

Open Web Analytics
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    OWA_SITE_ID = '123456'
    OWA_URL = 'https://example.com/owa/'

GoSquared
~~~~~~~~~

.. code-block:: python

    GOSQUARED_SITENAME = '123456'

Feeds
-----

You can use the ``FEED_RSS`` and ``FEED_ATOM`` options to enable RSS and Atom
feeds respectively.

.. code-block:: python

    FEED_RSS = 'feeds/rss.xml'

.. code-block:: python

    FEED_ATOM = 'feeds/atom.xml'

Feed menu item
~~~~~~~~~~~~~~

.. lightbox::
    :thumb: /images/eevee-menu.png
    :large: /images/eevee-menu.png
    :alt: Feed menu item
    :caption: Feed menu item
    :align: center

Enabling either ``FEED_RSS`` or ``FEED_ATOM`` will automatically add a menu
item for that feed. If ``MEGA_FOOTER`` is also enabled a link to the feed will
be added there too.

Eevee prefers RSS over ATOM, if you enable both feed types a menu item will
only be created for RSS, although both feeds will be added as alternate link
tags.

Category and tag pages
----------------------

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

.. _search:

Plugin: Search functionality
----------------------------

.. lightbox::
    :thumb: /images/eevee-search-menu-item.png
    :large: /images/eevee-search-menu-item.png
    :alt: Search menu item
    :caption: Search menu item
    :align: center

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

Plugin: Permalinks in headlines
-------------------------------

.. lightbox::
    :thumb: /images/eevee-headerid.png
    :large: /images/eevee-headerid.png
    :alt: Header permalink
    :caption: Header permalink
    :align: center

reStructuredText does not add anchors to headings by default, adding reference
links on headings means you can send the link to someone and have the browser
automatically display the relevant section.

Eevee is configured out-of-the-box to support adding these references using the
`headerid
<https://github.com/getpelican/pelican-plugins/tree/master/headerid>`__
plugin.

Plugin: Related articles
------------------------

.. lightbox::
    :thumb: /images/eevee-related.png
    :large: /images/eevee-related.png
    :alt: Related articles
    :caption: Related articles
    :align: center

Related articles functionality is provided by the `related_posts
<https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`__
plugin.

Installing it will automatically enabled the functionality within Eevee.

.. code-block:: python

    PLUGINS = [
        # ...
        'related_posts',
        # ...
    ]

Plugin: Articles in a series
----------------------------

.. lightbox::
    :thumb: /images/eevee-series.png
    :large: /images/eevee-series.png
    :alt: Articles in a series
    :caption: Articles in a series
    :align: center

Series article functionality is provided by the `series
<https://github.com/getpelican/pelican-plugins/tree/master/series>`__
plugin.

Installing it will automatically enabled the functionality within Eevee.

.. code-block:: python

    PLUGINS = [
        # ...
        'series',
        # ...
    ]

Plugin: Minimise CSS and JavaScript
-----------------------------------

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

Advanced pagination
-------------------

By default, Eevee will display pagination links on the index page of articles.
Enabling the `neighbors
<https://github.com/getpelican/pelican-plugins/tree/master/neighbors>`__ will
automatically add a previous and next button to the article page, allowing
pagination without going back to the index page.

The default Pelican pagination settings are not very pleasing, for more
information on how to customise them to better and be more intuitive please
look at the `Pelican documentation
<http://docs.getpelican.com/en/3.6.3/settings.html#using-pagination-patterns>`__.

DNS prefetch
------------

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

For example, the following would be applied if you had Disqus and Google
Analytics enabled.

.. code-block:: html

    <link rel="dns-prefetch" href="EXAMPLE.COM">
    <link rel="dns-prefetch" href="//code.getmdl.io">
    <link rel="dns-prefetch" href="//disqus.com">
    <link rel="dns-prefetch" href="//a.disquscdn.com">
    <link rel="dns-prefetch" href="//EXAMPLE.disqus.com">
    <link rel="dns-prefetch" href="//glitter-services.disqus.com">
    <link rel="dns-prefetch" href="//google-analytics.com">
    <link rel="dns-prefetch" href="//www.google-analytics.com">

All configuration settings
==========================

+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| Setting name                   | Default                              | Description                                                        |
+================================+======================================+====================================================================+
| ``SITENAME``                   |                                      | The title of your website                                          |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``AUTHOR``                     |                                      | Your name                                                          |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``THEME_PRIMARY``              | :blue-grey:`blue_grey`               | Primary colour scheme                                              |
|                                |                                      |                                                                    |
|                                |                                      | `Primary and accent colours`_                                      |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``THEME_ACCENT``               | :pink:`pink`                         | Accent colour scheme                                               |
|                                |                                      |                                                                    |
|                                |                                      | `Primary and accent colours`_                                      |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``MEGA_FOOTER``                | ``True``                             | Display the mega footer                                            |
|                                |                                      |                                                                    |
|                                |                                      | `Header and footer options`_                                       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``DISCLAIMER``                 |                                      | Disclaimer displayed on the footer                                 |
|                                |                                      |                                                                    |
|                                |                                      | `Primary and accent colours`_                                      |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``COPYRIGHT``                  |                                      | Copyright notice displayed on the footer                           |
|                                |                                      |                                                                    |
|                                |                                      | `Primary and accent colours`_                                      |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``USE_AUTHOR_CARD``            | ``False``                            | Display about author card on articles                              |
|                                |                                      |                                                                    |
|                                |                                      | `Author card`_                                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``AUTHOR_CARD_ON_PAGES``       | ``False``                            | Display about author card on pages                                 |
|                                |                                      |                                                                    |
|                                |                                      | `Author card`_                                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``AUTHOR_CARD_AVATAR``         | ``/theme/images/default_avatar.png`` | Avatar to display on the author card                               |
|                                |                                      |                                                                    |
|                                |                                      | `Author card`_                                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``AUTHOR_CARD_DESCRIPTION``    |                                      | Description to display on the author card                          |
|                                |                                      |                                                                    |
|                                |                                      | `Author card`_                                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``AUTHOR_CARD_SOCIAL``         | ``SOCIAL``                           | Social media links to display on the author card                   |
|                                |                                      |                                                                    |
|                                |                                      | `Author card`_                                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``MENUITEMS``                  | ``[]``                               | Displayed on header and mega footer                                |
|                                |                                      |                                                                    |
|                                |                                      | `Header and footer options`_                                       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``LINKS``                      | ``[]``                               | Blogroll to display on the mega footer                             |
|                                |                                      |                                                                    |
|                                |                                      | `Header and footer options`_                                       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``SOCIAL``                     | ``[]``                               | Social links to display on the menu and mega footer                |
|                                |                                      |                                                                    |
|                                |                                      | `Header and footer options`_                                       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``DISPLAY_PAGES_ON_MENU``      | ``False``                            | Display pages on the menu and mega footer                          |
|                                |                                      |                                                                    |
|                                |                                      | `Header and footer options`_                                       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``DISPLAY_CATEGORIES_ON_MENU`` | ``False``                            | Display categories on the menu and mega footer                     |
|                                |                                      |                                                                    |
|                                |                                      | `Header and footer options`_                                       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``COMMENTS_ON_PAGES``          | ``False``                            | Add Diqus or Muut comments on pages                                |
|                                |                                      |                                                                    |
|                                |                                      | `Disqus or Muut for comments`_                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``MUUT_SITENAME``              |                                      | Muut unique identifier for the website                             |
|                                |                                      |                                                                    |
|                                |                                      | `Disqus or Muut for comments`_                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``DISQUS_SITENAME``            |                                      | Disqus unique identifier for the website                           |
|                                |                                      |                                                                    |
|                                |                                      | `Disqus or Muut for comments`_                                     |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``USE_OPEN_GRAPH``             | ``False``                            | Add Open Graph meta tags                                           |
|                                |                                      |                                                                    |
|                                |                                      | `Sharing options`_                                                 |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``USE_TWITTER_CARDS``          | ``False``                            | Add Twitter meta tags                                              |
|                                |                                      |                                                                    |
|                                |                                      | `Sharing options`_                                                 |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``TWITTER_USERNAME``           |                                      | Add your Twitter username to mega tags                             |
|                                |                                      |                                                                    |
|                                |                                      | `Sharing options`_                                                 |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``OPEN_GRAPH_IMAGE``           |                                      | Add an image to Twitter and Open Graph                             |
|                                |                                      |                                                                    |
|                                |                                      | `Sharing options`_                                                 |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``OWA_SITE_ID``                |                                      | OWA unique identifier for the website                              |
|                                |                                      |                                                                    |
|                                |                                      | `Google Analytics, Piwik, Open Web Analytics and GoSquared`_       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``OWA_URL``                    |                                      | URL to the OWA installation                                        |
|                                |                                      |                                                                    |
|                                |                                      | `Google Analytics, Piwik, Open Web Analytics and GoSquared`_       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``PIWIK_SITE_ID``              |                                      | Piwik unique identifier for the website                            |
|                                |                                      |                                                                    |
|                                |                                      | `Google Analytics, Piwik, Open Web Analytics and GoSquared`_       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``PIWIK_URL``                  |                                      | URL to the Piwik installation                                      |
|                                |                                      |                                                                    |
|                                |                                      | `Google Analytics, Piwik, Open Web Analytics and GoSquared`_       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``PIWIK_SSL_URL``              | ``PIWIK_URL``                        | Secure URL to the Piwik installation                               |
|                                |                                      |                                                                    |
|                                |                                      | `Google Analytics, Piwik, Open Web Analytics and GoSquared`_       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``GOOGLE_ANALYTICS``           |                                      | Google Analytics unique identifier for the website                 |
|                                |                                      |                                                                    |
|                                |                                      | `Google Analytics, Piwik, Open Web Analytics and GoSquared`_       |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``ARCHIVES_URL``               |                                      | URL for archives and add a menu item for it                        |
|                                |                                      |                                                                    |
|                                |                                      | `Archives`_                                                        |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``ARCHIVES_SAVE_AS``           |                                      | Location to save archives                                          |
|                                |                                      |                                                                    |
|                                |                                      | `Archives`_                                                        |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``MONTH_ARCHIVE_SAVE_AS``      |                                      | Location to save monthly archives                                  |
|                                |                                      |                                                                    |
|                                |                                      | `Archives`_                                                        |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``YEAR_ARCHIVE_SAVE_AS``       |                                      | Location to save yearly archives                                   |
|                                |                                      |                                                                    |
|                                |                                      | `Archives`_                                                        |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``FEED_RSS``                   |                                      | Enable the RSS feed and add a menu item for it                     |
|                                |                                      |                                                                    |
|                                |                                      | `Feeds`_                                                           |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+
| ``FEED_ATOM``                  |                                      | Enable the Atom feed and add a menu item for it                    |
|                                |                                      |                                                                    |
|                                |                                      | `Feeds`_                                                           |
+--------------------------------+--------------------------------------+--------------------------------------------------------------------+

Additional tweaks and modifications
===================================

Additional things you can tweak and modify are available on `kura.io
</category/eevee/>`__.

Changelog
=========

0.0.12
------

`Compare changes
<https://github.com/kura/eevee/compare/0.0.11...0.0.12>`__

- Updated share colours to be from the Material Design palette.
- Added some automatic colouring of links/icons for AUTHOR_CARD
- Added ability to disable comments and author_card for a specific page or
  article using metadata.

  Using reStructuredText:

  .. code-block:: rst

      Example title
      #############
      :slug: example
      :author_card: False
      :comments: False

  Using Markdown:

  .. code-block:: md

      Title: Example title
      Slug: example
      Author_card: False
      Comments: False

0.0.11
------

`Compare changes
<https://github.com/kura/eevee/compare/0.0.10...0.0.11>`__

- Stop using base64 fonts, dumb idea to begin with.
- Tidy up font sizes in headers.

0.0.10
------

`Compare changes
<https://github.com/kura/eevee/compare/0.0.9...0.0.10>`__

- Bug fixes in template styles.

0.0.9
-----

`Compare changes
<https://github.com/kura/eevee/compare/0.0.8...0.0.9>`__

- Huge overhaul of theme... Too much to list, check out the documentation.

0.0.8
-----

`Compare changes
<https://github.com/kura/eevee/compare/0.0.7...0.0.8>`__

- Added better templates for `tags` and `categories`.

0.0.7
-----

`Compare changes
<https://github.com/kura/eevee/compare/0.0.6...0.0.7>`__

- Fixed RSS and Atom having the wrong types.

0.0.6
-----

`Compare changes
<https://github.com/kura/eevee/compare/0.0.5...0.0.6>`__

- Updated archive templates so they aren't terrible.
- archive will automatically links to year and month archives if
  ``YEAR_ARCHIVE_SAVE_AS`` or ``MONTH_ARCHIVE_SAVE_AS`` are set.
- partial_archives template now works as expected instead of showing every
  article.
- Added archive to header and footer menus.

0.0.5
-----

`Compare changes
<https://github.com/kura/eevee/compare/0.0.4...0.0.5>`__

- Template clean up, mostly making the HTML itself look prettier to edit.
- Added aria labels to elements to improve accessibility.
- Added structures to articles and pages, using `schema.org
  <https://schema.org/>`__ additional markup.

0.0.4
-----

- Accidentally messed up Disqus and variable names where not used, so comments
  didn't actually work properly...
- Load fonts from base64 in the CSS file.

0.0.3
-----

- Add ability to use muut instead of Disqus using ``MUUT_SITENAME`` variable.
- Make the share buttons nicer.
- Added "back to top" links.

0.0.2
-----

- Replace ``vh`` definitions with ``em`` for ribbon.
- Replace truetype fonts with woff2 and woff.

0.0.1
-----

- Eevee released

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
