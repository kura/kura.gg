Building nginx on Red Hat and Debian to RPM/DEB-style locations
###############################################################
:date: 2010-04-02 16:54
:author: kura
:category: tutorials
:tags: debian, fedora, install, nginx, redhat, ubuntu
:slug: building-nginx-on-red-hat-and-debian-to-rpmdeb-style-locations

The title of this post is a bit stupid, but I honestly couldn't think of
any other way to write it...

When compiling nginx by hand, by default make install will push the
binaries out to /usr/local/nginx and it doesn't come with a start/stop
script, understandably because it doesn't know which OS it is going to
be installed on etc etc.

Recently I was tasked with building nginx to an old Red Hat Enterprise
Live 4 server with no yum installation, no nginx package in up2date and
not being able to find an RPM that's link wasn't dead.

I've always felt that, being a Debian user, people think of me as only
being able to use apt-get and if I'm feeling especially adventurous dpkg
- to install applications. Some people know that I build .deb files in
my spare time, but most don't and for some weird reason I still feel
they think that about me. Paranoia?

Anyway, I decided to do it the old fashioned way and build nginx from
source on the RHEL4 box, simple tasks if you know how to do it
correctly.

Brief introduction of what's to come
------------------------------------

In this article I will explain the build process, options I pass to
configure and also provide a start/stop script for RHEL4, 5 and Debian.

The build process can be found on the nginx wiki and is a very simple
thing, but I passed some different arguments to do the follow;

-  Install all modules that I wanted
-  Build to /usr/bin, store config files in /etc/nginx, add
   sites-available, sites-enabled folders and logs to /var/log/nginx

I'm going to assume you have the latest 0.7.X or even 0.8.X source
already downloaded, untarred and also have gcc and all other required
build modules installed.

You'll need to be in your source directory to execute the following
commands.

Installation
------------

First we will add a www-data user and group to run as. You may already
have this set up for you if you've already installed Apache or nginx
from yum or apt in the past.

To check to see if you already have a www-data user run the following
command as root.

.. code:: bash

    grep www-data /etc/passwd

You should see the following output, the at signs (@) represent a
number.

::

    www-data:x:@@:@@:www-data:/var/www:/bin/sh

If you don't see this user then we will need to create it.

.. code:: bash

    sudo useradd -d /var/www -m -U www-data

The -d argument sets the user's home directory to /var/www, -m creates
the home directory if it does not exist and -U will create a group with
the same name as the user.

I install nginx with both SSL and rewrite enabled, both of these modules
require some extra modules install on your system.

SSL
~~~

Debian
^^^^^^

.. code:: bash

    sudo apt-get install libssl-dev

RedHat (yum)
^^^^^^^^^^^^

.. code:: bash

    sudo yum install libssl-dev

If you don't have yum installed you will either need to find an RPM or
install openssl from source (`http://www.openssl.org/source/`_)

.. _`http://www.openssl.org/source/`: http://www.openssl.org/source/

Rewrite module
~~~~~~~~~~~~~~

Debian
^^^^^^

.. code:: bash

    sudo apt-get install libpcre3 libpcre3-dev

RedHat (yum)
^^^^^^^^^^^^

.. code:: bash

    sudo yum install libpcre-dev

Or compile from source (`http://www.pcre.org/`_)

.. _`http://www.pcre.org/`: http://www.pcre.org/

Configuring
~~~~~~~~~~~

Next we will configure the source::

.. code:: bash

    ./configure --sbin-path=/usr/bin/nginx\\
    --conf-path=/etc/nginx/nginx.conf\\
    --pid-path=/var/run/nginx.pid\\
    --lock-path=/var/lock/nginx.lock\\
    --error-log-path=/var/log/nginx/error.log\\
    --http-log-path=/var/log/nginx/access.log\\
    --user=www-data\\
    --group=www-data\\
    --http-client-body-temp-path=/var/lib/nginx/body\\
    --http-proxy-temp-path=/var/lib/nginx/proxy\\
    --http-fastcgi-temp-path=/var/lib/nginx/fastcgi\\
    --with-http_ssl_module\\
    --with-http_realip_module\\
    --with-http_addition_module\\
    --with-debug\\
    --with-http_flv_module\\
    --with-http_stub_status_module\\

The above command will configure nginx, setting the path to it's binary
to /usr/bin/nginx, config file path to /etc/nginx/nginx.conf, pid to
/var/run/nginx.pid, lock file to /var/lock/nginx.lock, error and access
logs to /var/log/nginx, tell nginx to run as www-data with group
www-data, set it's temp paths to /var/lib/nginx and enable the following
modules; ssl, realip, addition (used for adding content to the start and
end of pages), debug, flash video and status modules.

If you didn't want to install openssl or pcre then you will have to
compile without ssl and pcre. Remove --with-http_ssl_module from above
and disable the rewrite module.

.. code:: bash

    --without-http_rewrite_module

Compiling
~~~~~~~~~

Once done, if you have no errors you can actually compile nginx.

.. code:: bash

    make
    sudo make install

nginx configuration
-------------------

Next we need to configure nginx to give it some nice configuration
options. First open up nginx's main configuration file

    /etc/nginx/nginx.conf

Modify it to look like the one below.

.. code:: nginx

    user www-data www-data;
    worker_processes 2;

    error_log /var/log/nginx/error.log;
    pid /var/run/nginx.pid;

    events {
        worker_connections 1024;
    }

    http {
        include /etc/nginx/mime.types;
        access_log /var/log/nginx/access.log;
        sendfile on;
        tcp_nopush on;
        keepalive_timeout 5;
        tcp_nodelay on;
        gzip on;

        include /etc/nginx/conf.d/\*.conf;
        include /etc/nginx/sites-enabled/\*;
    }

Next we'll create the sub directories for holding site and module
configuation.

.. code:: bash

    sudo mkdir /etc/nginx/sites-available
    sudo mkdir /etc/nginx/sites-enabled
    sudo mkdir /etc/nginx/conf.d

Next we'll create the default server definition.

    /etc/nginx/sites-available/default

And put the following in it.

.. code:: nginx

    server {
        listen 80;
        server_name localhost;
        access_log /var/log/nginx/localhost.access.log;

        location / {
            root /var/www/;
            index index.html index.htm;
        }

        location /nginx_status {
            stub_status on;
            access_log off;
            allow 127.0.0.1;
            deny all;
        }

    }

Now we symlink it in to the sites-enabled directory.

.. code:: bash

    sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled

Start/stop scripts
------------------

Once installation is complete we need to install a start/stop script, to
simply make life easier.

You can get the `Debian version from here`_ or the `RedHat version from
here`_.

.. _Debian version from here: https://kura.io/static/files/nginx-debian
.. _RedHat version from here: https://kura.io/static/files/nginx-redhat

Starting nginx
--------------

.. code:: bash

    /etc/init.d/nginx start

Starting the service on boot

Edit the following file:

.. code:: bash

    /etc/rc.local

And add the following before the exit call.

.. code:: bash

    /etc/init.d/nginx start
