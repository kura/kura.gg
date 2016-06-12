tugboat-bash-completion
#######################
:date: 2014-05-28 9:00
:author: kura
:category: coding
:tags: digital ocean, tugboat, bash, completion
:slug: tugboat-bash-completion

.. contents::
    :backlinks: none

tugboat-bash-completion is a bash completion script the `tugboat
<https://github.com/pearkes/tugboat>`__ CLI interface for the `Digital Ocean
<https://www.digitalocean.com/>`__ API.

Downloads
=========

- `.tar.gz <https://github.com/kura/tugboat-bash-completion/tarball/master>`_
- `.zip <https://github.com/kura/tugboat-bash-completion/zipball/master>`_

Installation
============

Debian/Ubuntu
-------------

Install manually
~~~~~~~~~~~~~~~~

Download the source file from above and run the commands below.

.. code-block:: bash

    sudo make install
    . ~/bashrc

Or you can do it the lazy way

.. code-block:: bash

    sudo wget https://github.com/kura/tugboat-bash-completion/blob/master/tugboat -O /etc/bash_completion.d/tugboat
    . ~/bashrc

Notes
=====

It's worth noting that any command that supports a FUZZY_MATCH will take a
small amount of time to respond, due to querying the API for a list of either
droplets or images.

Commands that do a droplet lookup;

- destroy
- halt
- info
- password-reset
- rebuild
- resize
- restart
- snapshot
- ssh
- start
- wait

An image lookup;

- destroy_image
- info_image
- rebuild


Source
======

The source can be found on `GitHub
<https://github.com/kura/tugboat-bash-completion>`_.

Issues
======

Issues can be tracked using `GitHub Issues
<https://github.com/kura/tugboat-bash-completion/issues>`_.

License
=======

This software is licensed using the MIT License.
The license is provided in the `source code repository
<https://github.com/kura/tugboat-bash-completion/blob/master/LICENSE>`_.
