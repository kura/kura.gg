Load balancing HTTP/HTTPS with Pound on Debian 6/Ubuntu
#######################################################
:date: 2011-09-29 23:15
:author: kura
:category: tutorials
:tags: http, https, load, load balancing, pound, ssl, ssl offloading, ssl termination
:slug: load-balancing-httphttps-with-pound-on-debian-6ubuntu

Pound is a great little load balancer, it's fast, opensource and
supports SSL termination, which is great!

Install
-------

    apt-get install pound

Configuration
-------------

The default configuration should be pretty good for most purposes, but
feel free to tweak as you require.

HTTP
~~~~

We'll first look at load balancing HTTP, in case you don't want or need
HTTPS load balancing.

We'll need delete all the content within *ListenHTTP* block, once done
it should look like this::

    ListenHTTP
    End

Now we add an address and port to listen on and finally a line to remove
an HTTP header::

    ListenHTTP
        Address 0.0.0.0 # all interfaces
        Port 80
        HeadRemove "X-Forwarded-For"
    End

This is a basic configuration, for each backend we want to load balance
we'll need to add a service within that listener.

You'll notice we're removing incoming headers called *X-Forwarded-For*,
this is to make sure someone doesn't try to craft them in to a request
and abuse them.

::

    ListenHTTP
        Address 0.0.0.0 # all interfaces
        Port 80
        HeadRemove "X-Forwarded-For"

        Service
            BackEnd
                Address 10.0.0.1
                Port 80
                Priority 1
            End
            BackEnd
                Address 10.0.0.2
                Port 80
                Priority 1
            End
        End
    End

Here I've added 2 BackEnds that connect to port 80, it's all pretty
simple. Add as many as you want/need.

Pound will pass correct HTTP headers through to the backends so you
configure those just like you normally would.

HTTPS
~~~~~

HTTPS is basically exactly the same as HTTP except for one fantastic
option - SSL termination! Which means we can do the SSL decryption
within Pound and talk to our backend servers over standard unencrypted
HTTP - **this should only be done on a private network.**

So, we'll create an HTTPS listened like the one above but with extra
options.

::

    ListenHTTPS
        Address 0.0.0.0 # all interfaces
        Port 443
        AddHeader "X-Forwarded-Proto: https"
        HeadRemove "X-Forwarded-Proto"
        HeadRemove "X-Forwarded-For"
        Cert "/path/to/certificate.pem

        Service
            BackEnd
                Address 10.0.0.1
                Port 80
                Priority 1
            End
            BackEnd
                Address 10.0.0.2
                Port 80
                Priority 1
                End
        End
    End

You'll notice a few changes here, first we tell the HTTPS listener to
listen on port 443 - SSL port.

We add a header to pass back to our backend servers called
*X-Forwarded-Proto*, this is so that on our backend we can inspect this
header and use it if required to know we're secure.

We also remove incoming headers called *X-Forwarded-Proto* and
*X-Forwarded-For*, this is to make sure someone doesn't try to craft
them in to a request and abuse them.

Finally is the certificate which needs to be a PEM file with all
certificates and keys within it and without passphrases.

Done
----

Once configured, reload Pound.

    /etc/init.d/pound reload

That really was simple.
