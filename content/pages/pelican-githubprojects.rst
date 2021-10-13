Pelican GitHub Projects
#######################
:author: kura
:slug: pelican-githubprojects

.. contents::
    :backlinks: none

Pelican GitHub Projects allows you to embed a list of your public GitHub
projects in your pages.

Installation
============

To install pelican-githubprojects, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-githubprojects

Configuration
=============

Enable the plugin in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_githubprojects',
        # ...
    ]

Add a setting with your GitHub username.

.. code-block:: python

    GITHUB_USER = 'kura'

Available data
==============

:name:
    The name of your project.
:language:
    The language your project is written in, information on how GitHub detects
    languages is `available here
    <https://help.github.com/articles/my-repository-is-marked-as-the-wrong-language>`_.
    It is GitHub that detects the language, not this plugin. So please, no
    issues about that.
:description:
    The description of your project (as set on GitHub.)
:homepage:
    The homepage of your project (as set on GitHub.)
:github_url:
    The web page URL of your project on GitHub (not the GIT or API URL.)

Usage
=====

In your templates you will be able to iterate over the `github_projects`
variable, as below.

.. code-block:: html

    {% if GITHUB_USER %}
        <h1>Projects</h1>
        {% for project in github_projects %}
            <h2>{{ project.name }} <sup>({{ project.language }})</sup></h2>
            <p>{{ project.description }}</p>
            <p>
                <a href="{{ project.homepage }}">Homepage</a>
                <a href="{{ project.github_url }}">GitHub</a>
            </p>
        {% endfor %}
    {% endif %}


License
=======

`MIT`_ license.

.. _MIT: https://opensource.org/licenses/MIT
