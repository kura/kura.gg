haproxy, nginx and SPDY with SSL termination (Debian 7)
#######################################################
:date: 2013-07-15 22:30
:author: kura
:category: tutorials
:tags: debian, ubuntu, haproxy, nginx, spdy, ssl, ssl termination
:slug: haproxy-nginx-and-spdy-with-ssl-termination-debian-7

.. contents::
    :backlinks: none

`I wrote an article last week`_ explaining that I had changed my blog
and built my own nginx packages with `SPDY`_ built in.

.. _`I wrote an article last week`: /2013/07/10/nginx-spdy-and-ngx-pagespeed/
.. _`SPDY`: http://www.chromium.org/spdy

I decided I would take things a little further and poke around with
haproxy some more. The initial plan was to compile the latest dev
source of haproxy with SSL termination enabled.

In doing so I realised I would lose SPDY support, which upset me a
little. After some digging I found that the 1.5-dev branch of
haproxy supports npn and thus can handle SPDY.

I tweaked my builds a little more and managed to get haproxy
running as an SSL terminating load balancer, with SPDY connections
being sent off to my nginx servers with SPDY enabled and all other
non-SPDY connections were passed on to an nginx virtual host with
SPDY disabled.

Requirements
============

I have released my haproxy build as a debian file below, it is built
off of haproxy_1.5~dev19 and is compiled for amd64. It should work on
any installation of Debian 7 and requires openssl-1.0.1d or higher.

On a standard Debian 7 install you should have openssl-1.0.1e-2, you
can find which version you have by running

.. code:: bash

    dpkg -l openssl

This should return something similar to

::

    ii  openssl        1.0.1e-2        amd64        Secure Socket Layer (SSL) binary and related cryptographic tools

Installing haproxy
==================

Download the deb file below, use either the GPG key or MD5/SHA1 sums to verify it.

+---------------------------------------+------------------+------------------+------------------+
| FILE                                  | GPG              | MD5              | SHA1             |
+=======================================+==================+==================+==================+
| `haproxy_1.5~dev19_amd64.deb`_        | `owGMeXVU1G...`_ | `715317e082...`_ | `e116e1c597...`_ |
+---------------------------------------+------------------+------------------+------------------+


.. _`haproxy_1.5~dev19_amd64.deb`: /files/haproxy_1.5~dev19_amd64.deb
.. _`owGMeXVU1G...`: /files/haproxy_1.5~dev19_amd64.deb.asc
.. _`715317e082...`: /files/haproxy_1.5~dev19_amd64.deb.md5
.. _`e116e1c597...`: /files/haproxy_1.5~dev19_amd64.deb.sha1

If you already have haproxy installed, make sure to remove it first.

You can install them by simply running:

.. code:: bash

    sudo dpkg -i haproxy_1.5~dev19_amd64.deb

You may receive an error due to missing dependencies, to fix this run:

.. code:: bash

    sudo apt-get install -f

Configuring haproxy
===================

First we need to enabled haproxy by running the following command

.. code:: bash

    sudo sed -i 's/ENABLED=0/ENABLED=1/' /etc/default/haproxy

We then need to empty the contents of the haproxy configuration and
replace it with a nice blank file. The following command will copy
the original file to a new location and create a blank file

.. code:: bash

    sudo mv /etc/haproxy/haproxy.cfg{,.orig} && sudo >/etc/haproxy/haproxy.cfg

SPDY only works over HTTPS, so bare that in mind. All you need to do is
enable SPDY in your server configuration as below.

::

    global
        maxconn 4096
        user haproxy
        group haproxy

    defaults
        option dontlognull
        retries 3
        option redispatch
        maxconn 2000
        contimeout 5000
        clitimeout 50000
        srvtimeout 50000

    frontend http
        mode http
        bind 0.0.0.0:80
        redirect sheme https if !{ ssl_fc }

    frontend kura-io
        mode tcp
        bind 0.0.0.0:443 ssl crt /etc/ssl/certs/kura.io.pem npn spdy/2 # pem is certificate, intermediate and finally private key
        use_backend kura-app-spdy if { ssl_fc_npn -i spdy/2 }
        default_backend kura-app-http

    backend kura-app-spdy
        mode tcp
        server kura-io-app1 127.0.0.1:80 check

    backend kura-app-http
        mode http
        server kura-io-app1 127.0.0.1:81 check

You don't need to worry about the *global* and *defaults* sections, I will now
explain what the final four sections do.

frontend http
-------------

::

    frontend http
        mode http
        bind 0.0.0.0:80
        redirect sheme https if !{ ssl_fc }

This tells haproxy to listen on port 80 and redirect all traffic
to the HTTPS version of the site.

frontend kura-io
----------------

::

    frontend kura-io
        mode tcp
        bind 0.0.0.0:443 ssl crt /etc/ssl/certs/kura.io.pem npn spdy/2 # pem is certificate, intermediate and finally private key
        use_backend kura-app-spdy if { ssl_fc_npn -i spdy/2 }
        default_backend kura-app-http

This section sets the proxy mode to tcp, which sends tcp
data over to the backend servers rather than http requests.

We then bind to all interfaces on port 443, enabling SSL and
passing in a PEM version of the certificate in the following
format

::

    -----BEGIN CERTIFICATE-----
    MAIN CERTIFICATE FOR KURA.IO
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    INTERMEDIATE CERTIFICATE
    -----END CERTIFICATE-----
    -----BEGIN RSA PRIVATE KEY-----
    PRIVATE KEY
    -----END RSA PRIVATE KEY-----

Finally we do some magic. We tell haproxy to use
the SPDY backend if a SPDY header is present::

    use_backend kura-app-spdy if { ssl_fc_npn -i spdy/2 }

If not then we fall back to the default HTTP backend::

        default_backend kura-app-http

backend kura-app-spdy
---------------------

::

    backend kura-app-spdy
        mode tcp
        server kura-io-app1 127.0.0.1:80 check

This section simply defines the server we should talk to if
the client is using an SPDY enabled connection.

Simply define multiple servers for additional servers.

You can see I am point it at 127.0.0.1 on port 80.

backend kura-app-http
---------------------

::

    backend kura-app-http
        mode http
        server kura-io-app1 127.0.0.1:81 check

And finally, here I am defining the http backends
to fall back on for non-SPDY connections.

You can see this is almost identical to the SPDY
backend except it is running in HTTP mode.

As with the SPDY backends, simply define multiple
servers as required. Here I am using 127.0.0.1 and
port 81.

nginx
=====

To make this all tie together we simply need to
install an SPDY-enabled nginx.

You can `follow my guide on how to install my
packaged version of nginx with SPDY enabled`_.

.. _`follow my guide on how to install my packaged version of nginx with SPDY enabled`: /2013/07/10/nginx-spdy-and-ngx-pagespeed/

Follow this guide up until the configuration of nginx.

Configuring nginx
=================

Within nginx we need to enable two virtual hosts

.. code:: nginx

    server {
        listen 80 spdy;
        server_name kura.io;

        # make nginx 301 redirects work
        port_in_redirect off;
        server_name_in_redirect off;

        location / {
                root   /var/www/kura.io/;
                index  index.html index.htm;
        }
    }

    server {
        listen 81;
        server_name kura.io;

        # make nginx 301 redirects work
        port_in_redirect off;
        server_name_in_redirect off;

        location / {
                root   /var/www/kura.io/;
                index  index.html index.htm;
        }
    }

The first virtual host is our SPDY enabled host
which is configured to run on port 80.

The second is our standard HTTP host which is
running on port 81.

We have two lines *port_in_redirect* and *server_name_in_redirect*
set to *off* because otherwise nginx would try to redirect to
http://kura.io:81/ and cause issues with haproxy.

It's a simple as that, you can test this using the `Firefox`_ and
`Chrome`_ extensions that show you websites with SPDY enabled.

.. _`Firefox`: https://addons.mozilla.org/en-us/firefox/addon/spdy-indicator/
.. _`Chrome`: https://chrome.google.com/webstore/detail/spdy-indicator/mpbpobfflnpcgagjijhmgnchggcjblin
