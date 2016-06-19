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

This week I pushed the `0.0.3 update
<https://github.com/kura/eevee/tree/0.0.3>`__ for my Pelican theme `Eevee
</eevee/>`__ containing new and improved styling for share buttons and adding
the ability to use `Muut <https://muut.com/>`__ instead of Disqus for comments.

Share button changes
====================

The original styling of the share buttons wasn't particularly pretty.

.. image:: /images/eevee-original-share-buttons.png
    :alt: Eevee's original share button styling
    :align: center

They badly needed a make over, and so they were restyled to be more prominent,
look less out of place and randomly pasted in to the page and to have a colour
scheme that matches the social media site they share to.

.. image:: /images/eevee-0.0.3-share-buttons.png
    :alt: Eevee's new 0.0.3 share button styling
    :align: center

These buttons appear on articles and pages, but when viewing an article with
``DISQUS_SITENAME`` or ``MUUT_SITENAME`` enabled a fourth button is shown that
links to the comments section of the current article.

.. image:: /images/eevee-0.0.3-article-share-buttons.png
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

Please be aware that if ``DISQUS_SITENAME`` and ``MUUT_SITENAME`` are
configured, Disqus will be prioritized over Muut and therefore only the Disqus
template will be loaded.

.. lightbox::
    :thumb: /images/eevee-0.0.3-muut-thumb.png
    :large: /images/eevee-0.0.3-muut.png
    :alt: Eevee using Muut for comments
    :caption: Eevee using Muut for comments
    :align: center

Back to the top of the page links
=================================

A small addition are the `back to the top of the page` links that will now
appear under each article on index pages.

.. image:: /images/eevee-0.0.3-back-to-top-links.png
    :alt: Eevee's new 0.0.3 back to top of the page links
    :align: center

A link has also been added to the footer to take users back to the top of the
page.

.. image:: /images/eevee-0.0.3-back-to-top-footer.png
    :alt: Eevee's new 0.0.3 back to top of the page footer link
    :align: center
