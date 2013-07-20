Apache internal dummy connection
################################
:date: 2010-03-27 19:29
:author: kura
:category: tutorials
:tags: apache, load average
:slug: apache-internal-dummy-connection

Recently I found that one of the servers I look after that runs a high
profile site was generating semi-high load at traffic peaks. You could
generally say that this would be understandable but the server was
shooting up to a load of around 10 for a few seconds and with that load
jump I was able to graph an increase of Apache processes on top of it.
Again though, this would generally be considered normal, but knowing how
well the server performs and having nginx sitting on top handling all
static content I knew something wasn't quite right.

Looking through the logs I found quite a lot of requests from a badly
written spider which was generating a lot of server load when it hit the
server, but after IP banning the culprit I also found several instances
of Apache waking it's child processes.

::

    127.0.0.1 - - [23/Mar/2010:17:02:38 +0000] "OPTIONS * HTTP/1.0" 200 - "-" "Apache (internal dummy connection)"

This in itself is normal and nothing to worry about, generally, it is
known and also mentioned on the Apache wiki (`explanation here`_) that
servers running 2.2.6 or lower can suffer performance problems due to
how Apache wakes it's children because it used GET / to wake them, but I
run 2.2.8 which doesn't actually used that same method.

.. _explanation here: http://wiki.apache.org/httpd/InternalDummyConnection

I applied the well known "work around" for this to test it and see if it
made any difference.

.. code:: apache

    RewriteEngine on
    RewriteCond %{HTTP_USER_AGENT} ^.*internal dummy connection.*$ [NC]
    RewriteRule ^/$ /blank.html [L]

Adding the virtual hosts with dynamic content will simple rewrite
Apache's internal dummy connection requests to blank.html, thus stopping
it from trying to generate all dynamic page content just to wake the
child.

All seems normal but time will tell as to whether this makes a
difference with versions > 2.2.6.
