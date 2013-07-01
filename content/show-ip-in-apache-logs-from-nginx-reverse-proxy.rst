Show IP in Apache logs from nginx reverse proxy
###############################################
:date: 2010-03-20 19:24
:author: kura
:category: apache, debian, howto, nginx
:tags: apache, log, nginx, proxy
:slug: show-ip-in-apache-logs-from-nginx-reverse-proxy

This is a very quick blog to show you how to show a users IP address in
your Apache access logs when the site in question is being reverse
proxied to Apache through nginx.

You need the rpaf module for Apache, on Debian and Ubuntu this is simple
to install

    apt-get update && apt-get install libapache2-mod-rpaf && a2enmod
    rpaf && apache2ctl graceful

This set of commands will do the following;

1. Update apt package list
2. Install libapache2-mod-rpaf
3. Enable mod-rpaf
4. Gracefully restart Apache (doesn't kill connections)

Once installed you simple need to be sure to pass the correct headers
through, so open up one of your nginx site configuration files and add
the following within the server definition.

::

    proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;

So you should have something that looks like this, but without the "... snip ..."

::

    server {
        ...snip...
        location / {
            ...snip...
            proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
        ...snip...
        }
    }
