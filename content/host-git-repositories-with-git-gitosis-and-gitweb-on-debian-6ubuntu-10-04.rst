Host git repositories with git, gitosis and gitweb on Debian 6/Ubuntu 10.04
###########################################################################
:date: 2011-12-17 15:40
:author: kura
:category: apache, howto, ubuntu
:tags: debian, git, gitosis, gitweb, ubuntu
:slug: host-git-repositories-with-git-gitosis-and-gitweb-on-debian-6ubuntu-10-04

Installation
------------

First up we'll need to install git and some Python tools to get Gitosis
installed.

Where # is used it means you need to either run the command as a
superuser with sudo or as root.

    # apt-get install -y git-core gitweb python-setuptools

Next we have to clone gitosis from it's git repository and install it.

    cd /tmp

    git clone git://eagain.net/gitosis.git

    cd gitosis

    # python setup.py install

Adding your git user
--------------------

    # adduser --system --shell /bin/sh --gecos 'git version control'
    --group --disabled-password --home /home/git git

The above command creates a new system user with **/bin/sh** as it's
shell with **no password** and a homedir of **/home/git/** and also
creates a group with the same name.

Initialising gitosis
--------------------

You'll need an SSH key for this, if you have one simply copy the
contents of it to your new git server, if you do not have one then you
can generate one on your machine using

    ssh-keygen

And then copy the contents to your server.

My file was copied to **/tmp/kura.pub** so to initialise I used

    sudo -H -u git gitosis-init < /tmp/kura.pub

***This command MUST be run as sudo.***

You need to do the same but replacing **kura.pub** with your own key, it
has to end in .pub

A note on key format
~~~~~~~~~~~~~~~~~~~~

One of my users (`@gump`_) had an issue where Gitosis would complain
about his username having invalid characters

.. _@gump: https://syslog.tv/2011/12/17/host-git-repositories-with-git-gitosis-and-gitweb-on-debian-6ubuntu-10-04/#comment-374

    gitosis.init.InsecureSSHKeyUsername: Username contains not allowed
    characters

This is because Gitosis expects your key to have a username and host at
the end of the base64 string like below

    ssh-rsa AAAAB3NzaC1yc2EA ... NOHgpPwEBzpnw== kura@odin

Configuring and controlling gitosis
-----------------------------------

Now that git and gitosis are working on your server, from your local
machine you now need to clone your gitosis admin and do all your changes
locally, pushing them back to the git server where gitosis will
automatically pick them up.

So you need to run

    git clone git@YOUR\_SERVER:gitosis-admin.git

If everything worked correctly you should have a copy on your local
machine now, if you run **ls** you'll see 1 file and a directory.

#. gitosis.conf
#. keydir

Unsurprisingly gitosis.conf is where gitosis is configured and keydir
contains public keys for your users. Each user needs their own public
key and it must end in *.pub*.

So open up **gitosis.conf** in your favourite editor and add the
following:

    [gitosis]
    gitweb = yes

    [group admins]
    writable = gitosis-admin test1
    members = kura

    [repo gitosis-admin]
    description = Gitosis admin repository
    gitweb = yes

So lets separate that in to parts.

**Part 1** - we simply tell gitosis to enable gitweb support.

**Part 2** - we configure a group called ***admins***, the admins group
has write permissions to 2 repositories; ***gitosis-admin*** and
***test***. The test repository will automatically become available once
we push this configuration back to gitosis later. We also define a user
called **kura** which you should replace with your own username, **each
user must have a public key in the keydir with the same name as the user
with .pub suffix. E.g. the kura user has a key called kura.pub**

**Part 3** - We create a repository section which is only really used
for gitweb to tell it to display that repository publicly via a browser.

**If you do not want your repositories to be public then I advice you
skip the parts with gitweb = yes above and also uninstall gitweb and
skip the gitweb section below. Or you could lock your gitweb via
HTAUTH.**

Now the changes have been made you need to commit them to git.

    git add \*
    git commit -m "Initial configuration"

And push them back to the server

    git push origin master

Now that is done you can test your access to the test repository created
earlier.

    git clone git@YOUR\_SERVER:test.git
    cd test
    echo "Hello world" > hello
    git add hello
    git commit -m "Test"
    git push origin master

If the above works then congratulations, everything is good.

Adding users and repositories
-----------------------------

Users
~~~~~

To add a user to gitosis you need to add them to a group and put a
public key with username.pub as the naming format in to keydir.

Repositories
~~~~~~~~~~~~

You simply need to name it in a writable section of a group and it'll
instantly be accessible. If you want to make it public in gitweb then
you'll need to a [repo] section as shown above.

Configure gitweb
----------------

Open up **/etc/gitweb.conf** in your favourite editor and change
***$projectroot*** to

    $projectroot = "/home/git/repositories/"

You will also need to add the Apache user to the git group

    usermod -G www-data,git www-data

By default Debian and Ubuntu will symlink in an Apache2 config to
**/etc/apache2/conf.d/gitweb** which is accessible from a browser on
`http://YOUR\_SERVER/gitweb`_

.. _`http://YOUR\_SERVER/gitweb`: http://YOUR_SERVER/gitweb
