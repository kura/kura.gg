Trigger command on filesystem changes with inotify + incron
###########################################################
:date: 2010-07-03 15:26
:author: kura
:category: debian, howto, ubuntu
:tags: incron, infobright, inotify, mysql
:slug: trigger-command-on-filesystem-changes-with-inotify-incron

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

    incrontab -l

Adding/editing tasks
~~~~~~~~~~~~~~~~~~~~

    incrontab -e

Delete all tasks
~~~~~~~~~~~~~~~~

    incrontab -r

All incron tasks must be in the following format

    <path> <mask> <command>

Masks
~~~~~

    **IN\_ACCESS** - File was accessed (read) (\*)
    **IN\_ATTRIB** - Metadata changed (permissions, timestamps, extended attributes, etc.) (\*)
    **IN\_CLOSE\_WRITE** - File opened for writing was closed (\*)
    **IN\_CLOSE\_NOWRITE** - File not opened for writing was closed (\*)
    **IN\_CLOSE** - Covers IN\_CLOSE\_WRITE and IN\_CLOSE\_NOWRITE
    **IN\_CREATE** - File/directory created in watched directory (\*)
    **IN\_DELETE** - File/directory deleted from watched directory (\*)
    **IN\_DELETE\_SELF** - Watched file/directory was itself deleted
    **IN\_MODIFY** - File was modified (\*)
    **IN\_MOVE\_SELF** - Watched file/directory was itself moved
    **IN\_MOVED\_FROM** - File moved out of watched directory (\*)
    **IN\_MOVED\_TO** - File moved into watched directory (\*)
    **IN\_MOVE** - Covers IN\_MOVED\_FROM and IN\_MOVED\_TO
    **IN\_OPEN** - File was opened (\*)
    **IN\_ALL\_EVENTS** - All of the above

    **IN\_DONT\_FOLLOW** - Don't dereference pathname if it is a symbolic link
    **IN\_ONESHOT** - Monitor pathname for only one event
    **IN\_ONLYDIR** - Only watch pathname if it is a directory

*When monitoring a directory, the masks marked with an asterisk (\*)
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

    /root/ IN\_CREATE echo "$@$# $% $&"

Open up a second root shell on the system and tail syslog

    tail -f /var/log/syslog

And simply create a random file on the system in /root/

    >test-incron

You should see the following appear within syslog:

    Jul 03 15:19:26 eurus incrond[5049]: (root) CMD (echo "/tmp/test-incron IN\_CREATE 256")

Success, you now have incron working.

How I used it
-------------

For me it meant I could set up one simple task to modify file access

    /tmp/mysql-ib-exports/ IN\_CREATE /bin/chmod 0664 $@$#

This will instantly change permissions on created files to 0664,
allowing the CSV to be loaded directly in to MySQL.
