How to generate an  /etc/shadow compatible password
###################################################
:date: 2012-10-11 09:56
:author: kura
:category: tutorials
:tags: /etc/shadow, mkpasswd, password, sha-512, sha512
:slug: how-to-generate-an-etcshadow-compatible-password

You'll need mkpasswd, on Debian 6 and Ubuntu 12.04 you can install this
using:

.. code-block:: bash

    sudo apt-get install whois

It is pretty weird that it comes with the whois package though...

And then run

.. code-block:: bash

    mkpasswd -m sha-512
