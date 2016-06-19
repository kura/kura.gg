Eevee -- Updating share buttons and adding Muut
###############################################
:date: 2016-06-19 01:45
:author: kura
:category: eevee
:tags: pelican, eevee, muut
:slug: eevee-updating-share-buttons-and-adding-muut

.. image:: /images/eeveelutions.png
    :alt: Eevee the Pokémon
    :align: center

.. contents::
    :backlinks: none

This week I pushed the `Eevee 0.0.3 update
<https://github.com/kura/eevee/tree/0.0.3>`__ containing new and improved
styling for share buttons and adding the ability to use `Muut
<https://muut.com/>`__ instead of Disqus for comments for users that wish to do
that.

Share button changes
====================

The original styling of the share buttons wasn't particularly pretty.

.. figure:: /images/eevee-original-share-buttons.png
    :alt: Eevee's original share button styling
    :align: center

They badly needed a make over, and so they were restyled to be more prominent,
look less out of place and randomly pasted in to the page and to have a colour
scheme that matches the social media site they share to.

.. figure:: /images/eevee-0.0.3-share-buttons.png
    :alt: Eevee's new 0.0.3 share button styling
    :align: center

These buttons appear on articles and pages, but when viewing an article with
``DISQUS_SITENAME`` or ``MUUT_SITENAME`` enabled a fourth button is shown that
links to the comments section of the current article.

.. figure:: /images/eevee-0.0.3-article-share-buttons.png
    :alt: Eevee's new 0.0.3 article share button styling
    :align: center

Comments powered by Muut
========================

To enable commenting with Muut, simply modify ``pelicanconf.py`` and set the
Muut site name.

.. code-block:: python

    MUUT_SITENAME = 'somethinghere'

This will automatically cause Eevee to enable the Muut comment template which
will styled similarly to how the Disqus comments section is styled.

.. lightbox::
    :thumb: /images/eevee-0.0.3-muut-thumb.png
    :large: /images/eevee-0.0.3-muut.png
    :alt: Eevee using Muut for comments
    :caption: Eevee using Muut for comments
    :align: center
