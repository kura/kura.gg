# -*- coding: utf-8 -*-

# Copyright (c) 2016 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals
from uuid import uuid4

from docutils import nodes
from docutils.parsers.rst import directives, Directive


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class Lightbox(Directive):
    """
    Create a pure CSS lightbox for images.

    Usage:

        .. lightbox::
            :thumb: /images/test-thumb.png
            :large: /images/test.png
            :alt: This is a test image
            :caption: A test caption
            :align: center
    """

    required_arguments = 0
    optional_arguments = 3
    option_spec = {
        'thumb': str,
        'large': str,
        'alt': str,
        'caption': str,
        'align': align
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        """Run the directive."""
        if 'thumb' not in self.options:
            raise self.error('Thumb argument is required.')
        thumb = self.options['thumb']
        if 'large' not in self.options:
            raise self.error('Large argument is required.')
        large = self.options['large']

        uuid = str(uuid4())
        caption = None
        alt = None

        if 'alt' in self.options:
            alt = self.options['alt']

        if 'caption' in self.options:
            caption = self.options['caption']

        if 'align' in self.options:
            align = self.options['align']
        else:
            align = 'left'

        if alt is not None:
            alt_text = '{} (click to view large image)'.format(alt)
        else:
            alt_text = 'Click to view large image'

        if caption is not None:
            caption_block = ('''<p class="align-{}">{} (click to view large '''
                             '''image)</p>''').format(align, caption)
        else:
            caption_block = ('''<p class="align-{}">Click to view large '''
                             '''image</p>''').format(align)

        block = ('''<div class="lightbox-block align-{4}">'''
                 '''<a href="#{0}" title="{3}">'''
                 '''<img src="{1}" alt="{3}" class="align-{4}" /></a>'''
                 '''<a href="#_" class="lightbox" id="{0}" title="Click to '''
                 '''close">'''
                 '''<img alt="Click to close" src="{2}" /></a>{5}</div>'''
                 '''<div class="lightbox-divider">'''
                 '''</div>''').format(uuid, thumb, large, alt_text, align,
                                      caption_block)
        return [nodes.raw('', block, format='html'), ]


def register():
    """Register the directive."""
    directives.register_directive('lightbox', Lightbox)
