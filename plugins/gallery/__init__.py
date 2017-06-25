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

import os
from uuid import uuid4

from docutils import nodes
from docutils.parsers.rst import directives, Directive


START = '<div class="eevee-card-container mdl-grid">\n'
END = '</div>\n'
IMAGE = ('<div class="eevee-cell eevee-cell--{2}-col mdl-card">\n'
         '<div class="mdl-card__media">\n'
         '<a href="#{0}" title="Click to view large image">\n'
         '<img src="{1}" alt="Click to view large image"/>\n'
         '</a>\n'
         '</div></div>\n'
         '<a class="lightbox" href="#_" id="{0}" title="Click to close">\n'
         '<img alt="Click to close" src="{1}"/>\n'
         '</a>\n')


class Gallery(Directive):
    required_arguments = 1
    optional_arguments = 1
    option_spec = {'columns': directives.positive_int}

    final_argument_whitespace = False
    has_content = False

    def run(self):
        _nodes = []
        gallery_dir = self.arguments[0].strip()
        columns = self.options['columns'] if 'columns' in self.options else 4
        if columns == 0 or columns > 5:
            raise self.error('Minimum number of columns is 1 and maximum is 5')
        webroot = gallery_dir.replace('content/', '/')
        if not os.access(gallery_dir, os.R_OK):
            err = ('Gallery directory {} does not exist or is not '
                   'readable'.format(gallery_dir))
            raise self.error()
        images = os.listdir(gallery_dir)
        if len(images) == 0:
            err = ('Gallery directory {} does not contain any '
                   'images'.format(gallery_dir))
            raise self.error(err)
        i = 0
        for image in sorted(images):
            path = os.path.join(webroot, image)
            uuid = str(uuid4())
            if i == 0:
                _nodes.append(nodes.raw('', START, format='html'))
            image_html = IMAGE.format(uuid, path, columns)
            _nodes.append(nodes.raw('', image_html, format='html'))
            i = i + 1
            if i == columns:
                _nodes.append(nodes.raw('', END, format='html'))
                i = 0
        return _nodes


def register():
    """Register the directive."""
    directives.register_directive('gallery', Gallery)
