yarg(1) -- A semi hard Cornish cheese, also queries PyPI
########################################################
:slug: yarg

.. contents::
    :backlinks: none

Yarg is a PyPI client, it was written for `pypip.in
<https://pypip.in>`_ and can search packages as well as read the RSS feeds
from PyPI for new packages and new package version releases.

Search interface
----------------

.. code-block:: python

    >>> import yarg
    >>> package = yarg.get("yarg")
    >>> package.name
    u'yarg'
    >>> package.author
    Author(name=u'Kura', email=u'kura@kura.io')

Newest packages interface
-------------------------

.. code-block:: python

    >>> import yarg
    >>> packages = yarg.newest_packages()
    >>> packages
    [<Package yarg>, <Package gray>, <Package ragy>]
    >>> packages[0].name
    u'yarg'
    >>> packages.url
    u'http://pypi.python.org/pypi/yarg

Updated packages interface
--------------------------

.. code-block:: python

    >>> import yarg
    >>> packages = yarg.latest_updated_packages()
    >>> packages
    [<Package yarg>, <Package gray>, <Package ragy>]
    >>> packages[0].name
    u'yarg'
    >>> packages[0].version
    u'0.1.2'
    >>> packages[0].url
    u'http://pypi.python.org/pypi/yarg/0.1.2

Documentation
-------------

Full documentation is at <https://yarg.readthedocs.org>.
