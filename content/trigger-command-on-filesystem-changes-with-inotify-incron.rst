Trigger command on filesystem changes with inotify + incron
###########################################################
:date: 2010-07-03 15:26
:author: kura
:category: tutorials
:tags: incron, infobright, inotify, mysql
:slug: trigger-command-on-filesystem-changes-with-inotify-incron

.. contents::
    :backlinks: none

During a seemingly normal work day a colleague pointed out a problem to
me and asked if I had any solution.

The problem was that they were trying to use InfoBright
(`http://www.infobright.com/`_) for some data crunching, export the data
to CSV and then import in to MySQL. My first idea was to output the data
from InfoBright as SQL and pipe it directly in to MySQL, this turned out
to not be possible as the version of IB they were using only supported
output as CSV.

.. _`http://www.infobright.com/`: http://www.infobright.com/

This in itself wasn't a problem, the problem lay with the fact that IB
would only output the file with 0660 permissions, and although both IB
and MySQL ran as user mysql and group mysql, MySQL itself flat out
refused to import the CSV file unless it was world readable (0664),
which was slightly annoying.

If the CSV didn't need to be instantly imported in to MySQL as soon as
it was generated then we could've just used CRON to change the file
permissions, but also this would've meant remembering which files needed
to be imported.

So the answer lay in **inotify**.

I could've written some C or Python to interface with inotify but I am
lazy, so I decided to just use incron.

Installation
------------

.. code-block:: bash

    sudo apt-get install inotify incron

Configuration
-------------

Once installed we need to modify /etc/incron.allow to set which users
can actually use incron.

I just choose the root user.

    /etc/incron.allow

Put the following in:

    root

Using incron
------------

Now that root can actually set up incron tasks, as root you can use
incrontab just like you do crontab

Listing incron tasks
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    incrontab -l

Adding/editing tasks
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    incrontab -e

Delete all tasks
~~~~~~~~~~~~~~~~

.. code-block:: bash

    incrontab -r

All incron tasks must be in the following format

::

    <path> <mask> <command>

Masks
~~~~~

    **IN_ACCESS** - File was accessed (read) (*)
    **IN_ATTRIB** - Metadata changed (permissions, timestamps, extended attributes, etc.) (*)
    **IN_CLOSE_WRITE** - File opened for writing was closed (*)
    **IN_CLOSE_NOWRITE** - File not opened for writing was closed (*)
    **IN_CLOSE** - Covers IN_CLOSE_WRITE and IN_CLOSE_NOWRITE
    **IN_CREATE** - File/directory created in watched directory (*)
    **IN_DELETE** - File/directory deleted from watched directory (*)
    **IN_DELETE_SELF** - Watched file/directory was itself deleted
    **IN_MODIFY** - File was modified (*)
    **IN_MOVE_SELF** - Watched file/directory was itself moved
    **IN_MOVED_FROM** - File moved out of watched directory (*)
    **IN_MOVED_TO** - File moved into watched directory (*)
    **IN_MOVE** - Covers IN_MOVED_FROM and IN_MOVED_TO
    **IN_OPEN** - File was opened (*)
    **IN_ALL_EVENTS** - All of the above

    **IN_DONT_FOLLOW** - Don't dereference pathname if it is a symbolic link
    **IN_ONESHOT** - Monitor pathname for only one event
    **IN_ONLYDIR** - Only watch pathname if it is a directory

*When monitoring a directory, the masks marked with an asterisk (*)
above can occur for files in the directory, in which case the name field
in the returned event data identifies the name of the file within the
directory.*

Command
~~~~~~~

Commands can be any system commands that the user has permissions to
use, but incron also has some symbols that can be accessed to use within
the commands.

    **$$** - Dollar sign
    **$@** - Watched filesystem path
    **$#** - Event-related file name
    **$%** - Event flags (textually)
    **$&** - Event flags (numerically)

A simple way of testing incron would be to add a basic task on the root
users home directory.

::

    /root/ IN_CREATE echo "$@$# $% $&"

Open up a second root shell on the system and tail syslog

.. code-block:: bash

    sudo tail -f /var/log/syslog

And simply create a random file on the system in /root/

.. code-block:: bash

    >test-incron

You should see the following appear within syslog:

::

    Jul 03 15:19:26 eurus incrond[5049]: (root) CMD (echo "/tmp/test-incron IN_CREATE 256")

Success, you now have incron working.

How I used it
-------------

For me it meant I could set up one simple task to modify file access

::

    /tmp/mysql-ib-exports/ IN_CREATE /bin/chmod 0664 $@$#

This will instantly change permissions on created files to 0664,
allowing the CSV to be loaded directly in to MySQL.
