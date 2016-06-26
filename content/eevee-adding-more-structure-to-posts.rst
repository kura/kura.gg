Eevee -- Adding more structure to posts
#######################################
:date: 2016-06-25 21:00
:author: kura
:category: eevee
:tags: pelican
:slug: eevee-adding-more-structure-to-posts

.. image:: /images/eeveelutions.png
    :alt: Eevee the Pokémon
    :align: center

.. contents::
    :backlinks: none

Introduction
============

`Eevee </eevee/>`__ is a theme for `Pelican <http://getpelican.com>`_, based on
Google's `Material Design <https://material.google.com/>`_ specification that I
released in June 2016.

`Schema.org <https://schema.org/>`__ is a collaborative effort, including
private companies like Google and the open source community to promoter adding
additional structure to data that indentifies what parts of HTML are being used
for, for example it can help a search engine understand what content is more
important to index or, it can help a user with a screen reader get to the
important content more easily. These structures are more commonly known as
microformats or microdata.

Structure is a beautiful thing
==============================

HTML -- by it's very design is structured -- the difference is that the content
defines or modifies that structure.

By using microformat data structures from schema.org you can define what
elements are more prominent or important through a large set of additional
vocabulary, improving the experience for everyone that uses your website.

.. code-block:: html

    <article itemscope itemtype="http://schema.org/BlogPosting">
        <meta itemprop="accessibilityControl" content="fullKeyboardControl" />
        <meta itemprop="accessibilityControl" content="fullMouseControl" />
        <meta itemprop="accessibilityControl" content="bookmarks" />
        <meta itemprop="accessibilityAPI" content="ARIA" />
        <div itemprop="author" itemscope
             itemtype="https://schema.org/Person" role="presentation">
            <meta itemprop="name" content="Kura" />
            <meta itemprop="name"
                  content="https://kura.io/authors/kura/" />
        </div>
        <meta itemprop="keywords" content="eevee,html,pelican" />
        <div class="eevee-article eevee-article-padding">
            <div class="eevee-meta mdl-color-text--grey-500">
                <time datetime="2016-06-25T21:00:00+01:00"
                      itemprop="datePublished">
                     25 Jun 2016
                </time>
            </div>
            <h2 itemprop="name">
                <a href="https://kura.io/eevee" rel="bookmark"
                   title="Permalink to 'Eevee -- A Material Design theme for Pelican'"
                   itemprop="url">
                    Eevee -- A Material Design theme for Pelican
                </a>
            </h2>
            <section itemprop="articleBody">
                Some random content here
            </section>
        </div>
        <div class="eevee-comment" id="article-comments">
            <section itemscope itemtype='http://schema.org/UserComments'>
                <h2>Discuss</h2>
                Disqus/Muut stuff here.
            </section>
        </div>
    </article>

Above is an example of a blog post with the additional vocabulary, below I'll
outline each important section and explain what it does.

.. code-block:: html

    <article itemscope itemtype="http://schema.org/BlogPosting">

This simply tells the client which schema is being used for the content within
it. The client uses that data to determine what elements should be provided
based on that schema. Here I'm using the `BlogPosting
<http://schema.org/BlogPosting>`__ schema.

.. code-block:: html

    <meta itemprop="accessibilityControl" content="fullKeyboardControl" />
    <meta itemprop="accessibilityControl" content="fullMouseControl" />
    <meta itemprop="accessibilityControl" content="bookmarks" />
    <meta itemprop="accessibilityAPI" content="ARIA" />

These elements -- as you may have guess from their names -- are used to improve
accessibility. More information on available options is provided on the
`W3C wiki <https://www.w3.org/wiki/WebSchemas/Accessibility>`__.

.. code-block:: html

    <div itemprop="author" itemscope
         itemtype="https://schema.org/Person" role="presentation">
        <meta itemprop="name" content="Kura" />
        <meta itemprop="name"
              content="https://kura.io/authors/kura/" />
    </div>

This set of markup simply defines who the author is and where more of their
content is located. Note that it uses a different schema named `Person
<https://schema.org/Person>`__.

Because the div element has no style and consists of only meta data, a role
is defined that tells screen readers this data is only for presentation
purposes and can be ignored.

.. code-block:: html

    <meta itemprop="keywords" content="eevee,html,pelican" />

This a pretty simple element, it is generated from the blog articles category
and any tags it may have.

.. code-block:: html

    <time datetime="2016-06-25T21:00:00+01:00"
          itemprop="datePublished">
         25 Jun 2016
    </time>

This element is a date provided as a universally understood value and in a
more user-friendly format that is displayed to the user.

.. code-block:: html

    <h2 itemprop="name">
        <a href="https://kura.io/eevee" rel="bookmark"
           title="Permalink to 'Eevee -- A Material Design theme for Pelican'"
           itemprop="url">
            Eevee -- A Material Design theme for Pelican
        </a>
    </h2>

Here the name of the article is defined, as is the URL to that article.

.. code-block:: html

    <section itemprop="articleBody">
        Some random content here
    </section>

This section informs the client that this is the main content of the post.

.. code-block:: html

    <section itemscope itemtype='http://schema.org/UserComments'>
        <h2>Discuss</h2>
        Disqus/Muut stuff here.
    </section>

Finally we add another schema `UserComments <http://schema.org/UserComments>`__
that defines user comment content.
