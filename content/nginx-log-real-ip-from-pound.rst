nginx log real IP from Pound
############################
:date: 2011-08-10 12:34
:author: kura
:category: tutorials
:tags: apache, load balancer, nginx, pound, reaip, x-forwarded-for
:slug: nginx-log-real-ip-from-pound

Recently I started using Pound as a load balancer to a cluster of nginx
servers and found my access logs were filled with the IP address of the
load balancer. I did some digging and found the correct way to "fix"
this.

First thing you need to do is make sure you remove X-Forwarded-For from
Pound

::

    ListenHTTP
        # ... snip ...
        # ... snip ...
        HeadRemove "X-Forwarded-For"
    End

Once this is done, reload Pound.

Next you need nginx compiled with realip module -
`http://wiki.nginx.org/NginxHttpRealIpModule`_

.. _`http://wiki.nginx.org/NginxHttpRealIpModule`: http://wiki.nginx.org/NginxHttpRealIpModule

On Ubuntu/Debian servers this module comes by default, otherwise you may
have to compile it in yourself using the following option:

.. code-block:: bash

    --with-http_realip_module

Once this is all done modify your nginx vhosts and add the following 2
lines

.. code-block:: nginx

    set_real_ip_from [IP];
    real_ip_header X-Forwarded-For;

Where [IP] is the IP address of your load balancer.

To configure this to work with Apache you need the mod_rpaf module.
