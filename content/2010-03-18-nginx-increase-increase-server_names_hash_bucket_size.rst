nginx - increase increase server_names_hash_bucket_size
#######################################################
:date: 2010-03-18 21:54
:author: kura
:category: tutorials
:tags: nginx
:slug: nginx-increase-increase-server_names_hash_bucket_size

Today I ran in to something I'd never seen before when configuring
nginx.

I ran the nginx config test, as I usually do before I restart it.

.. code-block:: bash

    nginx -t

But, the response I got was interesting

::

    2010/03/18 21:16:09 [emerg] 12299#0: could not build the server_names_hash, you should increase server_names_hash_bucket_size: 32
    2010/03/18 21:16:09 [emerg] 12299#0: the configuration file /etc/nginx/nginx.conf test failed

I found that one of the domain names I was using was over 32 characters
in length, nginx's default max length.

Thankfully the fix was simple.

.. code-block:: nginx

    http {
        # ...snip...
        server_names_hash_bucket_size 64;
        # ...snip...
    }
