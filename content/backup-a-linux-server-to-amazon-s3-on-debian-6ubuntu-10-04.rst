Backup a Linux server to Amazon S3 on Debian 6/Ubuntu 10.04
###########################################################
:date: 2012-02-29 20:55
:author: kura
:category: tutorials
:tags: amazon, aws, backup, debian, s3, ubuntu
:slug: backup-a-linux-server-to-amazon-s3-on-debian-6ubuntu-10-04

.. contents::

I have several servers powering syslog including it's `Raspberry Pi`_
mirror, load balancer and email servers. All of my servers are hosted
using `Linode`_ in their London data centre and have Linode's back-up
system doing both daily and weekly snapshots.

.. _Raspberry Pi: http://rpi.syslog.tv/
.. _Linode: http://www.linode.com/?r=8d58820f89940a1a68832c0cdd53109727cfa622

For the app and database servers I do server-side backups storing each
website and it's database in it's own folder within /backup in case I
require a quick back-up to fix something, rather than the server has
died.

This is all well and good but I like having an off-site backup too and
for that I use `S3`_...

.. _S3: http://aws.amazon.com/s3/

About S3
--------

Amazon's S3 is pretty cheap and very easy to use. Because only data is
going in you don't pay a transfer fee and the cost of storage is very
affordable, you can see a `pricing list here <http://aws.amazon.com/s3/#pricing>`_.

To do the backup I use a daily cron job which then uploads the data to
S3 using `s3cmd`_.

.. _s3cmd: http://s3tools.org/s3cmd

Installation
------------

Download the S3 tools package list in to apt

.. code:: bash

    sudo wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | sudo apt-key add -
    sudo wget http://s3tools.org/repo/deb-all/stable/s3tools.list -O /etc/apt/sources.list.d/s3tools.list

Update your package list and install s3cmd

.. code:: bash

    sudo apt-get update && apt-get install s3cmd

Configuration
-------------

You'll need to configure the tool to work with your AWS account, so run

.. code:: bash

    sudo s3cmd --configure

When prompted, fill in your access and secret key which you can find
`on the Amazone website <https://aws-portal.amazon.com/gp/aws/securityCredentials>`_.

When asked to provide an encryption password, I choose yes but you can
say no.

When asking if you want to use HTTPS, I choose yes but again, you can
say no, it really depends on how secure you want the data transfer.

I would suggest using an encryption password and enabling HTTPS.

Using s3cmd
-----------

Now that s3cmd is installed and configured you can use it.

You can create a bucket using the s3cmd command below, but as far as I
know you can't select a location so I create my buckets manually
`on the web interface <https://console.aws.amazon.com/s3/home>`_.

.. code:: bash

    s3cmd mb s3://your-bucket-name

Once done you can see a list of available buckets with

.. code:: bash

    s3cmd ls

As shown below

.. code:: bash

    s3cmd ls

    2012-02-29 20:28 s3://kura-linode-test

Now that this is done we can put some data in there, create a test file

.. code:: bash

    echo "this is a test" > test.file

And put it in S3

.. code:: bash

    s3cmd put test.file s3://your-bucket-name/

You can see it using

.. code:: bash

    s3cmd ls s3://your-bucket-name

Download it with

.. code:: bash

    s3cmd get s3://your-bucket-name/test.file

And delete it with

.. code:: bash

    s3cmd del s3://your-bucket-name/test.file

Once satisfied with this you can create a shell script to automate some
backups for you, I'll provide a simple one below that uploads my home
directory.

Example
-------

.. code:: bash

    #!/bin/sh
    s3cmd sync --recursive --skip-existing /home/kura
    s3://kura-linode-test/
