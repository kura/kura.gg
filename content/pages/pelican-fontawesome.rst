Pelican FontAwesome
###################
:author: kura
:slug: pelican-fontawesome

.. contents::
    :backlinks: none

Pelican FontAwesome allows you to embed FontAwesome icons in your RST documents.

Installation
============

To install pelican-fontawesome, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-fontawesome

Then enable it in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_fontawesome',
        # ...
    ]

Include the FontAwesome CSS in your base template.

.. code-block:: html

    <link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

Usage
=====

In your article or page, you simply need to add a reference to FontAwesome and
then the icon name.

.. code-block:: rst

    :fa:`fa-github`

Which will result in:

.. code-block:: html

    <span class="fa fa-github"></span>

And the user will see: :fa:`fa-github`

You can also increase the size, just like the `FontAwesome documentation
<https://fortawesome.github.io/Font-Awesome/examples/>`__ shows.

.. code-block:: rst

    :fa:`fa-github fa-4x`

Will result in: :fa:`fa-github fa-4x`



License
=======

`MIT`_ license.

.. _MIT: http://opensource.org/licenses/MIT