Writing a Vimeo and YouTube plugin for Pelican
##############################################
:date: 2013-08-09 17:38
:author: kura
:category: coding
:tags: python, pelican, youtube, vimeo
:slug: writing-a-vimeo-and-youtube-plugin-for-pelican

.. contents::
    :backlinks: none

`Pelican <https://getpelican.com/>`_ is a Python-powered static blog generator
that processes `ReStructuredText <https://docutils.sourceforge.net/rst.html>`_
and `Markdown <https://daringfireball.net/projects/markdown/>`_ articles and
pages and converts them to HTML. I use Pelican to power this blog.

There is a YouTube RST directive built in to Pelican core but it really
shouldn't exist there.

I submitted a pull request for Pelican core to enable Vimeo videos in articles
but that request was declined because it didn't belong in the core. So I
decided I would write it as a plugin instead and while I was doing it, also
wrote a plugin for YouTube so that it could be removed from the core.

`There is a decent amount of detail in the Pelican documentation on how to
write plugins
<https://docs.getpelican.com/en/3.2/plugins.html#how-to-create-plugins>`_, I'm
not going to cover the whole process but I thought I would cover a little of
what I did.

Adding an RST directive
=======================

Really all we're doing is modifying docutils on-the-fly to tell it how to
understand new directives, so we need to import directives from docutils

.. code-block:: python

    from docutils.parsers.rst import directives, Directive

With this in place, we can dynamically register a new directive to docutils

.. code-block:: python

    directives.register_directive('vimeo', Vimeo)

The first argument we pass in is the name of our directive, the second
argument is the name of the class we wish to be invoked.

Writing the Directive
=====================

I'll now break down the Vimeo class and explain what it does, piece by piece.

We will need to import an extra method from docutils

.. code-block:: python

    from docutils import nodes

This is used to append segments of data together, in our case HTML.

class Vimeo
-----------

.. code-block:: python

    class Vimeo(Directive):

This is pretty self explanatory, we define a new class that inherits from
`docutils.parsers.rst.Directive`.

Next we define a method for handling our alignment choices

.. code-block:: python

    def align(argument):
        return directives.choice(argument, ('left', 'center', 'right'))

Now we need to set some base values against our class for docutils to know how
many arguments are required and so on, it's pretty easy to understand. For the
alignment option we pass it the callable method declared above, but without
calling it.

.. code-block:: python

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'width': directives.positive_int,
        'height': directives.positive_int,
        'align': align
    }

    final_argument_whitespace = False
    has_content = False

And finally we move on to the meat of the plugin, the method that actually does
the processing.

The method name is called run because that is required by docutils.

.. code-block:: python

    def run(self):

First I get the videoID from the first argument in the RST, I tend set default
values for width, height and alignment. Those three arguments are optional, but
if they have been defined then I override the defaults.

.. code-block:: python

        videoID = self.arguments[0].strip()
        width = 420
        height = 315
        align = 'left'

        if 'width' in self.options:
            width = self.options['width']

        if 'height' in self.options:
            height = self.options['height']

        if 'align' in self.options:
            align = self.options['align']

Next I define the Vimeo URL and the two blocks of HTML that create the
surrounding div element and the video iframe. Here I also replace the videoID
in to the URL and also the optional arguments specified above.

.. code-block:: python

        url = 'https://player.vimeo.com/video/{}'.format(videoID)
        div_block = '<div class="vimeo" align="{}">'.format(align)
        embed_block = '<iframe width="{}" height="{}" src="{}" '\
                      'frameborder="0"></iframe>'.format(width, height, url)

And finally I create a list of docutils nodes with the HTML we created above.

.. code-block:: python

        return [
            nodes.raw('', div_block, format='html'),
            nodes.raw('', embed_block, format='html'),
            nodes.raw('', '</div>', format='html')]

And that's really it, it's a simple as that. `You can view full source on
GitHub <https://github.com/kura/pelican_vimeo>`_ and also `read the manual for
pelican-vimeo on it's software page on this website
</pelican-vimeo>`_.
