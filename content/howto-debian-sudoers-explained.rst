HOWTO: Debian - Sudo(ers) explained
###################################
:date: 2010-01-13 03:56
:author: kura
:category: tutorials
:tags: debian, howto, sudo, sudoers
:slug: howto-debian-sudoers-explained



Ah sudo, one of my favourites, funnily enough I've noticed a lot of
Linux users use sudo (mainly because Ubuntu installs and configures your
first user by default,) but very few seem to know that much about it.
This can include not even knowing how to add a user to sudoers.

This article will give you some useful information on what sudo actually
is, how to configure it and how to restrict it.

What is sudo?
-------------

So, quickly running **man sudo** gives us some information what sudo
actually is and does.

    sudo allows a permitted user to execute a command as the superuser
    or another user, as specified in the sudoers file. The real and
    effective uid and gid are set to match those of the target user as
    specified in the passwd file and the group vector is initialized
    based on the group file (unless the -P option was specified). If the
    invoking user is root or if the target user is the same as the
    invoking user, no password is required. Otherwise, sudo requires
    that users authenticate themselves with a password by default (NOTE:
    in the default configuration this is the user's password, not the
    root password). Once a user has been authenticated, a timestamp is
    updated and the user may then use sudo without a password for a
    short period of time (15 minutes unless overridden in sudoers).

Why use sudo?
-------------

So now that we know what sudo is, why use it? Well, one of the main (and
probably biggest reasons) for using sudo is giving users and groups
access to commands that as a normal user they wouldn't normally be able
to use.

If configured correctly you can have all commands run through sudo
logged, which you can then do wonderous things with like have emailed to
you as I do, using Logwatch.

sudo uses the users password, this means no revealing root passwords to
random users in order to allow them to run a few extra commands that
they need to use. "But I can just change access permissions on programs
if I want them accessible" I hear you cry, of course you can, but there
are some things you simply don't want to expose and yes, you can argue
that you just add a user to a group that has permissions but sudo is
just a better way of controlling access.

Installing sudo
---------------

So first things first, lets install sudo.

.. code:: bash

    apt-get install sudo

Chances are you've probably already got sudo installed but depending on
how you installed Debian (or whichever flavour you're using) you may not
have chosen to install it.

So how do I use sudo?
---------------------

Well, this is what **man sudo** is for, but basically it's simple:

.. code:: bash

    sudo cat /etc/issue

Yes, this command would work without the need for sudo, but I wanted a
simple example usage.

Adding users to sudo
--------------------

There are a couple of ways of doing this, you can either edit
**/etc/sudoers** with your favourite editor or use **visudo**. visudo
will use which ever editor you have set using export. I've seen some
distributions that do not allow direct access to /etc/sudoers and force
you to use visudo, I've also read and seen that visudo does some
checking before saving. I personally know enough and feel comfortable
enough with the sudoers file to edit it directly, but that's just my
choice.

So, open your sudoers list using your chosen method, you should see
something similar to this:

.. code:: bash

    root ALL=(ALL) ALL

So, what does this mean? Well, it's actually surprisingly simple. The
first part **"root"** is the name of the user, the second **"ALL"** is
the host that this definition belongs to, chances are you don't need to
change this, the third **"ALL"** is the user(s) to allow the user to run
commands as and the final **"ALL"** is a list of commands that the user
can run.

So, this might be a bit daunting from that explanation, so lets take a
look at a user I'll create for myself

.. code:: bash

    kura ALL=(root) /usr/bin/apt-get, /usr/bin/vi

So lets break that down; the user **kura** can run the commands
**/usr/bin/apt-get** and **/usr/bin/vi** as the user **root** on all
hosts.

Hopefully that makes it simple to understand. For the user that the
commands are run as you can user any user or daemon on the server, for
example root could be another user, in the following example I will use
a different user called admin.

.. code:: bash

    kura ALL=(admin) /usr/bin/apt-get, /usr/bin/vi

Adding groups to sudoers
------------------------

The approach for this is exactly the same as for users except you use %
to define a group.

.. code:: bash

    %sudoers ALL=(root) /usr/bin/apt-get, /usr/bin/vi

And now to wrap this article up...

How I personally use sudoers
----------------------------

I use sudoers on all of my servers and my approach to locking them down
is simple; I have a user that has access to ALL users and ALL commands,
I then have a group called sudoers that users can be added to that have
access to some commands that they may need from time to time, giving
them the ability to do things like tailing system logs. I also have
Logwatch installed which will email me with my daily log report which
includes a list of all users that ran commands via sudo and tells me
which commands they ran. This way I can keep an eye on them.
