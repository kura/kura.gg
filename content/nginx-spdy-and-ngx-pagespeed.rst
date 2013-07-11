nginx, SPDY and ngx_pagespeed (Debian/Ubuntu)
#############################################
:date: 2013-07-10 22:30
:author: kura
:category: tutorials
:tags: debian, ubuntu, nginx, spdy, pagespeed, ngx_pagespeed, mod_pagespeed
:slug: nginx-spdy-and-ngx-pagespeed

I decided to rebuild syslog.tv as pure HTML using RST and
`Pelican`_ and rebrand it as kura.io.

.. _`Pelican`: http://blog.getpelican.com/

In doing so I decided I would go all out and use `SPDY`_ and
`ngx_pagespeed`_ (`mod_pagespeed`_) for fun to see exactly
what I could do.

.. _`SPDY`: http://www.chromium.org/spdy
.. _`ngx_pagespeed`: http://nginx.org/en/docs/http/ngx_http_spdy_module.html
.. _`mod_pagespeed`: https://developers.google.com/speed/

Sadly no version of nginx has been officially released with SPDY
or ngx_pagespeed enabled, you can compile nginx from source to
enable SPDY so I thought I would go ahead and do it, releasing
some Debian packages in the process.

After compiling nginx from the source package available at the
`Ubuntu PPA`_, I decided I would go further and compile in
ngx_pagespeed.

.. _`Ubuntu PPA`: https://launchpad.net/~nginx

Installing
==========

I have released the 4 required debian packages below (please note
they are only available for amd64);

+-------------------------------+------------------+------------------+------------------+
| FILE                          | GPG              | MD5              | SHA1             |
+===============================+==================+==================+==================+
| `nginx_1.4.1_all.deb`_        | `owGMl1NwLw...`_ | `e0fb636905...`_ | `d0d1e073eb...`_ |
+-------------------------------+------------------+------------------+------------------+
| `nginx-common_1.4.1_all.deb`_ | `owGMt1NwJU...`_ | `4ef36131b2...`_ | `7043e0828d...`_ |
+-------------------------------+------------------+------------------+------------------+
| `nginx-full_1.4.1_amd64.deb`_ | `owG09ndUk1...`_ | `5f9da5109c...`_ | `a023efb3f8...`_ |
+-------------------------------+------------------+------------------+------------------+
| `nginx-doc_1.4.1_all.deb`_    | `owGMtlOQJQ...`_ | `1857b64f9d...`_ | `bd814c7465...`_ |
+-------------------------------+------------------+------------------+------------------+


.. _`nginx_1.4.1_all.deb`: https://kura.io/static/files/nginx_1.4.1_all.deb
.. _`owGMl1NwLw...`: https://kura.io/static/files/nginx_1.4.1_all.deb.asc
.. _`e0fb636905...`: https://kura.io/static/files/nginx_1.4.1_all.deb.md5
.. _`d0d1e073eb...`: https://kura.io/static/files/nginx_1.4.1_all.deb.sha1

.. _`nginx-common_1.4.1_all.deb`: https://kura.io/static/files/nginx-common_1.4.1_all.deb
.. _`owGMt1NwJU...`: https://kura.io/static/files/nginx-common_1.4.1_all.deb.asc
.. _`4ef36131b2...`: https://kura.io/static/files/nginx-common_1.4.1_all.deb.md5
.. _`7043e0828d...`: https://kura.io/static/files/nginx-common_1.4.1_all.deb.sha1

.. _`nginx-full_1.4.1_amd64.deb`: https://kura.io/static/files/nginx-full_1.4.1_amd64.deb
.. _`owG09ndUk1...`: https://kura.io/static/files/nginx-full_1.4.1_amd64.deb.asc
.. _`5f9da5109c...`: https://kura.io/static/files/nginx-full_1.4.1_amd64.deb.md5
.. _`a023efb3f8...`: https://kura.io/static/files/nginx-full_1.4.1_amd64.deb.sha1

.. _`nginx-doc_1.4.1_all.deb`: https://kura.io/static/files/nginx-doc_1.4.1_all.deb
.. _`owGMtlOQJQ...`: https://kura.io/static/files/nginx-doc_1.4.1_all.deb.asc
.. _`1857b64f9d...`: https://kura.io/static/files/nginx-doc_1.4.1_all.deb.md5
.. _`bd814c7465...`: https://kura.io/static/files/nginx-doc_1.4.1_all.deb.sha1


You can install them by simply running:

    sudo dpkg -i nginx*.deb

If you already have nginx installed, make sure to remove it first.

Configuring SPDY
================

SPDY only works over HTTPS, so bare that in mind. All you need to do is
enable SPDY in your server configuration as below.

::

    server {
        listen 443 ssl spdy;
        server_name kura.io;
        ...
    }

It's a simple as that, you can test this using the `Firefox`_ and
`Chrome`_ extensions that show you websites with SPDY enabled.

.. _`Firefox`: https://addons.mozilla.org/en-us/firefox/addon/spdy-indicator/
.. _`Chrome`: https://chrome.google.com/webstore/detail/spdy-indicator/mpbpobfflnpcgagjijhmgnchggcjblin

Configuring ngx_pagespeed
=========================

To enable ngx_pagespeed you first need to create a directory
that it can write cache files to.

    sudo mkdir /var/cache/ngx_pagespeed/

    sudo chown www-data:www-data /var/cache/ngx_pagespeed/

Once this is done you can enable ngx_pagespeed in your
server configuration as below.

::

    server {
        ...
        pagespeed on;
        pagespeed RewriteLevel CoreFilters;
        pagespeed FileCachePath "/var/cache/ngx_pagespeed/";
        pagespeed EnableFilters combine_css,combine_javascript,remove_comments,collapse_whitespace;
        ...
    }

The three filters that are enabled do the following:

 - combines CSS <style> elements in to one,
 - combines multiple <script> elements in to one,
 - removes all comments from HTML and,
 - removes additional whitespace from HTML excluding <pre>, <script>, <style> and <textarea> elements.

You can test this by simply viewing the source code of your
website and seeing all of the HTML compressed.

You can find `more information on filters here`_.

.. _`more information on filters here`: https://developers.google.com/speed/pagespeed/module/config_filters
