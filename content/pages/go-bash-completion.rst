go-bash-completion
##################
:date: 2013-07-20 11:07
:author: kura
:slug: go-bash-completion

.. contents::
    :backlinks: none

go-bash-completion is as it sounds - bash completion
script for the `Go programming language <http://golang.org/>`_.

Downloads
=========

- `.tar.gz <https://github.com/kura/go-bash-completion/tarball/master>`_
- `.zip <https://github.com/kura/go-bash-completion/zipball/master>`_

Installation
============

Debian/Ubuntu
-------------

apt.kura.io
~~~~~~~~~~~

Follow instructions on enabling `apt.kura.io </apt.kura.io/>`__
repository and then run the following command to install the package.

.. code-block:: bash

    sudo apt-get install go-bash-completion

Install manually
~~~~~~~~~~~~~~~~

Download the source file from above and run the commands below.

.. code-block:: bash

    sudo make install
    . ~/bashrc

Or you can do it the lazy way

.. code-block:: bash

    sudo wget https://raw.github.com/kura/go-bash-completion/master/etc/bash_completion.d/go -O /etc/bash_completion.d/go
    . ~/bashrc

OS X
----

With `homebrew <http://brew.sh/>`_ you can install the
 `go-completion` recipe to use this plugin

.. code-block:: bash

    brew tap homebrew/completions
    brew install go-completion

then add the following lines to your ~/.bashrc

.. code-block:: bash

    if [ -f `brew --prefix`/etc/bash_completion.d/go ]; then
        source `brew --prefix`/etc/bash_completion.d/go
    fi

Source
======

The source can be found on `GitHub
<https://github.com/kura/go-bash-completion>`_.

Issues
======

Issues can be tracked using `GitHub Issues
<https://github.com/kura/go-bash-completion/issues>`_.

License
=======

This software is licensed using the MIT License.
The license is provided in the `source code repository
<https://github.com/kura/go-bash-completion/blob/master/LICENSE>`_.
