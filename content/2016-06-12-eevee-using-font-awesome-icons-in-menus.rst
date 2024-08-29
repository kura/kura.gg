Eevee -- Using Font Awesome icons in menus
##########################################
:date: 2016-06-12 23:40
:author: kura
:category: eevee
:tags: pelican
:slug: eevee-using-font-awesome-icons-in-menus
:series: Eevee

.. image:: /images/eeveelutions.png
    :alt: Eevee the Pokémon
    :align: center

.. contents::
    :backlinks: none

Introduction
============

`Eevee </eevee/>`__ is a theme for `Pelican <https://getpelican.com>`_, based on
Google's `Material Design <https://material.google.com/>`_ specification that I
released in June 2016.

Eevee allows configuring menu links in the header and footer of a template --
including social links.

Eevee also includes `Font Awesome <https://fontawesome.com/>`_ by default, at
time of release and writing of this article it provides Font Awesome version
4.6.3.

Because the links are totally customisable, it means you can inject HTML
directly in to a link name and -- because Font Awesome is included by default
-- you can inject Font Awesome icons in to link names using HTML.

.. image:: /images/eevee-social-icons.png
    :alt: Social icons in Eevee menu

Using icons in links
====================

Menu's in Eevee are controlled by Pelican's configuration, for information on
how to modify menu's please see `the Eevee documentation
</eevee/#header-and-footer-options>`_.

Imagine you have a list of links to social websites in your menu, similar to
the list below.

.. code-block:: python

    SOCIAL = (('Github', 'https://github.com/'),
              ('Twitter', 'https://twitter.com/'),
              ('Facebook', 'https://facebook.com/'),
              ('Instagram', 'https://instagram.com/'),
              ('LinkedIn', 'https://linkedin.com/'))

Adding the relevant icons to these links is very simple.

.. code-block:: python

    SOCIAL = (('<i class="fa fa-github aria-hidden="true"></i> Github',
               'https://github.com/'),
              ('<i class="fa fa-twitter aria-hidden="true"></i> Twitter',
               'https://twitter.com/'),
              ('<i class="fa fa-facebook aria-hidden="true"></i> Facebook',
               'https://facebook.com/'),
              ('<i class="fa fa-instagram aria-hidden="true"></i> Instagram',
               'https://instagram.com/'),
              ('<i class="fa fa-linkedin aria-hidden="true"></i> LinkedIn',
               'https://linkedin.com/'))

Turning a rather dull menu, in to a more pleasing menu.

.. image:: /images/eevee-social-icons--no-icons.png
    :alt: Eevee menu with no icons

.. image:: /images/eevee-social-icons.png
    :alt: Social icons in Eevee menu
