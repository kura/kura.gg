# -*- coding: utf-8 -*-
"""
Gist embedding plugin for Pelican
=================================

This plugin allows you to embed `Gists`_ into your posts.

.. _Gists: https://gist.github.com/

"""
from __future__ import unicode_literals
import hashlib
import logging
import os
import re


logger = logging.getLogger(__name__)
gist_regex = re.compile(
    r'(<p>\[gist:id\=([0-9a-fA-F]+)(,file\=([^\]]+))?\]</p>)')
gist_template = """<div class="gist">
    <script src='{{script_url}}'></script>
</div>"""


def gist_url(gist_id, filename=None):
    url = "https://gist.github.com/raw/{}".format(gist_id)
    if filename is not None:
        url += "/{}".format(filename)
    return url


def script_url(gist_id, filename=None):
    url = "https://gist.github.com/{}.js".format(gist_id)
    if filename is not None:
        url += "?file={}".format(filename)
    return url


def setup_gist(pelican):
    """Setup the default settings."""

    pelican.settings.setdefault('GIST_CACHE_ENABLED', True)
    pelican.settings.setdefault('GIST_CACHE_LOCATION',
                                '/tmp/gist-cache')

    # Make sure the gist cache directory exists
    cache_base = pelican.settings.get('GIST_CACHE_LOCATION')
    if not os.path.exists(cache_base):
        os.makedirs(cache_base)


def replace_gist_tags(generator):
    """Replace gist tags in the article content."""
    from jinja2 import Template
    template = Template(gist_template)

    for article in generator.articles:
        for match in gist_regex.findall(article._content):
            gist_id = match[1]
            filename = None
            if match[3]:
                filename = match[3]
            logger.info('[gist]: Found gist id {} and filename {}'.format(
                gist_id,
                filename
            ))

            # Create a context to render with
            context = generator.context.copy()
            context.update({
                'script_url': script_url(gist_id, filename),
            })

            # Render the template
            replacement = template.render(context)

            article._content = article._content.replace(match[0], replacement)


def register():
    """Plugin registration."""
    from pelican import signals

    signals.initialized.connect(setup_gist)

    signals.article_generator_finalized.connect(replace_gist_tags)
