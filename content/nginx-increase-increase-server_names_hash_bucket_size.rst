nginx - increase increase server_names_hash_bucket_size
#######################################################
:date: 2010-03-18 21:54
:author: kura
:category: howto, nginx
:tags: nginx
:slug: nginx-increase-increase-server_names_hash_bucket_size

Today I ran in to something I'd never seen before when configuring
nginx.

I ran the nginx config test, as I usually do before I restart it.

    nginx -t

But, the response I got was interesting

::

    2010/03/18 21:16:09 [emerg] 12299#0: could not build the
    server\_names\_hash, you should increase
    server\_names\_hash\_bucket\_size: 32

    2010/03/18 21:16:09 [emerg] 12299#0: the configuration file
    /etc/nginx/nginx.conf test failed

I found that one of the domain names I was using was over 32 characters
in length, nginx's default max length.

Thankfully the fix was simple.

::

    http {
        ...snip...
         server\_names\_hash\_bucket\_size 64;
         ...snip...
    }
