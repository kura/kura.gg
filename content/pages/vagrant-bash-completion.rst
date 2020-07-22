vagrant-bash-completion
#######################
:date: 2013-07-20 11:07
:author: kura
:slug: vagrant-bash-completion

.. contents::
    :backlinks: none

vagrant-bash-completion is as it sounds - bash completion
script for `Vagrant <http://www.vagrantup.com/>`_.

They were originally written by `Nikita Fedyashev
<https://github.com/nfedyashev/>`_, I just modified his
work and made some changes. Eventually he ended up deleting
his version and forking mine.

Originally the completion scripts were meant to be used by
myself and developers from my company, but they started to
gain traction and now are quite widely used.

OS X support was added by `Conor McDermottroe
<https://github.com/conormcd>`_ and `Nils Caspar
<https://github.com/pencil>`_ added it to Homebrew with
additional OS X/Homebrew documentation from `Dean Malmgren
<https://github.com/deanmalmgren>`_

Downloads
=========

- `.tar.gz <https://github.com/kura/vagrant-bash-completion/tarball/master>`_
- `.zip <https://github.com/kura/vagrant-bash-completion/zipball/master>`_

Installation
============

Debian/Ubuntu
-------------

apt.kura.gg
~~~~~~~~~~~

Follow instructions on enabling `apt.kura.gg </apt.kura.gg/>`__
repository and then run the following command to install the package.

.. code-block:: bash

    sudo apt-get install vagrant-bash-completion

Install manually
~~~~~~~~~~~~~~~~

Download the source file from above and run the commands below.

.. code-block:: bash

    sudo make install
    . ~/bashrc

Or you can do it the lazy way

.. code-block:: bash

    sudo wget https://raw.github.com/kura/vagrant-bash-completion/master/etc/bash_completion.d/vagrant -O /etc/bash_completion.d/vagrant
    . ~/bashrc

OS X
----

With `homebrew <http://brew.sh/>`_ you can install the
 `vagrant-completion` recipe to use this plugin

.. code-block:: bash

    brew tap homebrew/completions
    brew install vagrant-completion

then add the following lines to your ~/.bashrc

.. code-block:: bash

    if [ -f `brew --prefix`/etc/bash_completion.d/vagrant ]; then
        source `brew --prefix`/etc/bash_completion.d/vagrant
    fi

Source
======

The source can be found on `GitHub
<https://github.com/kura/vagrant-bash-completion>`_.

Issues
======

Issues can be tracked using `GitHub Issues
<https://github.com/kura/vagrant-bash-completion/issues>`_.

License
=======

This software is licensed using the MIT License.
The license is provided in the `source code repository
<https://github.com/kura/vagrant-bash-completion/blob/master/LICENSE>`_.
