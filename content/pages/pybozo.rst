PyBozo
######
:date: 2011-11-10 20:49
:author: kura
:slug: pybozo

.. contents::
    :backlinks: none

PyBozo is a Python implementation of `BozoCrack`_ which was originally
written by `Juuso Salonen`_ in Ruby.

.. _BozoCrack: https://github.com/juuso/BozoCrack
.. _Juuso Salonen: http://twitter.com/juusosalonen

How it works
------------

Quite simply it takes each hash and searches for it on Google, the first
page of results returned will have every word converted to an MD5 hash
of 32 hexidecimal characters which is then compared against the hash
passed in.

Downloads
---------

- `.tar.gz`_
- `.zip`_

.. _.tar.gz: https://github.com/kura/pybozo/tarball/master
.. _.zip: https://github.com/kura/pybozo/zipball/master

Requires
--------

- Python 2.6+

Usage
-----

.. code-block:: bash

    python bozo.py HASHES.TXT

The file of hashes must contain a 32 character MD5 hash separated by a
new line "\\n"

Source
------

`Here`_.

.. _Here: https://github.com/kura/pybozo
