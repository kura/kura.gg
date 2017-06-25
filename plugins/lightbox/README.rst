Lightbox -- A pure CSS lightbox for Pelican
###########################################

.. figure:: https://raw.githubusercontent.com/kura/lightbox/master/lightbox.png
    :alt: Lightbox
    :align: center

    Credit: `Kimberly Coles <http://www.kimberlycoles.com/>`_

.. contents::
    :backlinks: none

Introduction
============

With the release of my `Eevee <https://kura.io/eevee/>`_ theme for `Pelican
<http://getpelican.com>`_, I realised displaying a thumbnail image of the
theme that linked to a larger image wasn't the most appealing design choice.
I prefer to leave Javascript out of the equation where possible, being one of
those weird people that have it disabled by default.

As such I sought out a way to create a pure CSS equivalent of a Lightbox and
turn it in to an RST directive to plug directly in to Pelican.

Installation
============

.. code-block:: bash

    $ wget https://github.com/kura/lightbox/archive/master.tar.gz -O lightbox.tar.gz
    $ tar xvzf lightbox.tar.gz
    $ mv lightbox-master /your/pelican/plugins/folder/lightbox

Make sure to rename the ``lightbox-master`` directory to ``lightbox``.

If you do not have a plugins directory in your Pelican blog, in the root
directory of your blog, the directory your ``content`` directory is in.

Create one.

.. code-block:: bash

    $ mkdir plugins

And in your ``pelicanconf.py`` set the ``PLUGIN_PATHS`` variable.

.. code-block:: python

    PLUGIN_PATHS = ['plugins/', ]

Then add lightbox to your ``pelicanconf.py`` ``PLUGINS``.

.. code-block:: python

    PLUGINS = [
        # ...
        'lightbox',
        # ...
    ]

Usage
=====

In your article or page, you simply need add a directive.

.. code-block:: rst

    .. lightbox::
        :thumbnail: /images/eevee-thumbnail.png
        :large: /images/eevee-large.png

Will result in the following HTML.

.. code-block:: html

    <div class="align-left">
        <a href="#005da263-b70e-4a84-b8c3-e2c989527613" title="Click to view large image">
            <img src="/images/eevee-article-header-thumb.png" class="align-left" alt="Click to view large image" />
        </a>
        <a class="lightbox" href="#_" id="005da263-b70e-4a84-b8c3-e2c989527613" title="Click to close">
            <img src="/images/eevee-article-header.png" alt="Click to close" />
        </a>
    </div>
    <div class="lightbox-divider"></div>

Optional arguments
==================

Lightbox also supports the following optional arguments.

- `alt`_
- `caption`_
- `align`_

Alt
---

This optional argument defines ``alt=`` attribute for an image that is also
used the ``title=`` attribute for anchors.

.. code-block:: rst

    :alt: Eevee, the Pokémon

Caption
-------

This optional argument defines caption text for an image, it is displayed
under the thumbnail inside a paragraph ``<p></p>`` element.

.. code-block:: rst

    :caption: Eevee, the Pokémon

Align
-----

This optional argument defines the alignment of the thumbnail image and
caption.

.. code-block:: rst

    :align: center

Valid values for this option are;

- center
- left
- right

Alignment is added as a CSS class attribute, for example;

.. code-block:: html

    <img class="align-center" />
    <img class="align-left" />
    <img class="align-right" />

CSS attributes
==============

Each set of lightbox thumbnail, large image and caption are wrapped in a
``<div>`` element with the class attribute ``lightbox-block`` and a class
attribute based on the alignment i.e. ``align-left``.

For example;

.. code-block:: html

    <div class="lightbox-block align-left"> ... </div>

The thumbnail image will have an alignment class attribute too.

.. code-block:: html

    <img class="align-left" />

The large image and the anchor that closes it have the class attribute
``lightbox`` which initially sets their display as hidden.

.. code-block:: html

    <a href="#_" class="lightbox" title="Click to close">
        <img class="lightbox" alt="Click to close" />
    </a>

Finally, the parent ``div`` element is closed and a final ``div`` element with
the class attribute ``lightbox-divider`` is provided, allowing you to create a
defined separation between images.

.. code-block:: html

    <div class="lightbox-divider"></div>

Putting all elements together, this is how the final HTML will be returned.

.. code-block:: html

    <div class="lightbox-block align-center">
        <a href="#e17813e9-ba4c-4037-be9a-3b0bb81fa0e5" title="Homepage (click to view large image)">
            <img alt="Homepage (click to view large image)" class="align-center" src="/images/eevee-homepage-thumb.png" />
        </a>
        <a class="lightbox" href="#_" id="e17813e9-ba4c-4037-be9a-3b0bb81fa0e5" title="Click to close">
            <img alt="Click to close" src="/images/eevee-homepage.png" />
        </a>
        <p class="align-center">Homepage (click to view large image)</p>
    </div>
    <div class="lightbox-divider"></div>

Basic CSS for Lightbox
======================

.. code-block:: css

    .lightbox {
        display: none;
        position: fixed;
        z-index: 999;
        width: 100%;
        height: 100%;
        text-align: center;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.8);
    }

    .lightbox img {
        max-width: 98%;
        max-height: 90%;
        margin-top: 2%;
    }

    .lightbox:target {
        outline: none;
        display: block;
    }

    .lightbox-divider {
        background: #E0E0E0;
        width: 100%;
        height: 3px;
        -webkit-flex-shrink: 0;
        -ms-flex-negative: 0;
        flex-shrink: 0;
        margin: 30px 0;
    }

You can get a copy of this `basic CSS file from GitHub
<https://github.com/kura/lightbox/blob/master/lightbox.css>`_.


Source code
===========

The source code of Lightbox is `hosted on GitHub
<https://github.com/kura/lightbox/>`__.

License
=======

Lightbox is released under the `MIT license
<https://github.com/kura/lightbox/blob/master/LICENSE>`__.
