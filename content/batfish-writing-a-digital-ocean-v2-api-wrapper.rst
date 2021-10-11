batfish(1) - writing a Digital Ocean V2 API wrapper
###################################################
:date: 2014-09-15 22:20
:author: kura
:category: coding
:tags: python, digital ocean
:slug: batfish-writing-a-digital-ocean-v2-api-wrapper

.. contents::
    :backlinks: none

Batfish is a Python client and API wrapper for the `Digital Ocean V2 API
<https://developers.digitalocean.com/>`_. It can be used as a library module in
your own Python code but also provides a CLI interface and a shell-like command
interpreter.

Batfish is still under development and is considered in the Alpha stage. It is
not yet available via PyPI but can be tried out using the `code available on
GitHub <https://github.com/kura/batfish>`_.

There is a small amount of `documentation available on Read The Docs
<https://batfish.readthedocs.org>`_ and tests are still being written to get as
much coverage as possible and eaked out all of the bugs. You can find the
`latest test status on Travis CI <https://travis-ci.org/kura/batfish>`_.

Module interface
----------------

.. code-block:: python

    >>> from batfish import Client
    >>> client = Client()
    >>> client.authorize("abcde12345")
    >>> client.droplets
    [<Droplet ego.kura.gg>, <Droplet fax.kura.gg>, <Droplet jet.kura.gg>, <Droplet ski.kura.gg>]
    >>> client.droplet_reboot(1234)

CLI interface
-------------

.. code-block:: bash

    $ batfish authorize
    abcde12345
    $ batfish droplets
    ego.kura.gg [id: 12345] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    fax.kura.gg [id: 12346] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    jet.kura.gg [id: 12347] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    ski.kura.gg [id: 12348] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    $ batfish droplet_reboot 12345

Console interface
-----------------

.. code-block:: bash

    batfish> authorize
    abcde12345
    batfish> droplets
    ego.kura.gg [id: 12345] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    fax.kura.gg [id: 12346] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    jet.kura.gg [id: 12347] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    ski.kura.gg [id: 12348] (cpu(s): 1, mem: 512MB, disk: 20GB, ip: 123.123.123.123 status: active, region: Amsterdam 3)
    batfish> droplet_reboot 12345
