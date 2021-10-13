Pelican Vimeo
##############
:date: 2011-10-20 11:38
:author: kura
:slug: pelican-vimeo

.. contents::
    :backlinks: none

Pelican Vimeo is a plugin to enabled you to embed Vimeo videos in your pages
and articles.

Installation
============

To install pelican-vimeo, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-vimeo

Then enabled it in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_vimeo',
        # ...
    ]

Usage
=====

In your article or page, you simply need to add a line to embed you video.

.. code-block:: rst

    .. vimeo:: VIDEO_ID

Which will result in:

.. code-block:: html

    <div class="vimeo" align="left">
        <iframe width="420" height="315" src="https://player.vimeo.com/video/VIDEO_ID" frameborder="0"></iframe>
    </div>

Additional arguments
--------------------

You can also specify a `width`, `height` and `alignment`

.. code-block:: rst

	.. vimeo:: 37818131
        :width: 800
        :height: 500
        :align: center

Which will result in:

.. code-block:: html

    <div class="vimeo" align="center">
        <iframe width="800" height="500" src="https://player.vimeo.com/video/37818131" frameborder="0"></iframe>
    </div>

License
=======

`MIT`_ license.

.. _MIT: https://opensource.org/licenses/MIT
