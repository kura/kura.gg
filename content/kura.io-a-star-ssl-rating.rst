kura.io's A* SSL rating
#######################
:date: 2014-02-02 15:18
:author: kura
:category: tutorials
:tags: ssl
:slug: kura.io-a-star-ssl-rating

I am a firm believer in using SSL as much as possible, for me that is pretty
much everywhere and, thanks to the wonderful guys at
`GlobalSign <https://www.globalsign.com/>`__, most of
my SSL certificates are free becauses my projects are all open source.

I used a blog post by `Hynek Schlawack <https://hynek.me/articles/hardening-your-web-servers-ssl-ciphers/>`__
as a base for my SSL setup, he is keeping this article up-to-date as much as
possible so it should be a great source for any security conscious people that
would like to know more and get good explanations about each part.

Let's take a brief look at how this website achieves it's A* rating.

Key
===

I use a 4096 bit RSA key that is no a `Debian weak key
<https://wiki.debian.org/SSLkeys#Identifying_Weak_Keys>`__.

Protcols
========

I do not support SSLv2 but do support much stronger protocols

- TLS 1.2,
- TLS 1.1,
- TLS 1.0 and,
- SSL 3

Cipher suites & key exchanges
=============================

I only support `Elliptic curve Diffie–Hellman <https://en.wikipedia.org/wiki/Elliptic_curve_Diffie%E2%80%93Hellman>`__,
`Diffie–Hellman <https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange>`__
and fall back to `RSA <https://en.wikipedia.org/wiki/RSA_(algorithm)>`__
if the browser does not support ECDH or DH.

The website prefers ECDH+AESGCM or DH+AESGCM which specifically uses AES-128,
if AESGCM isn't supported by the browser (at time of writing, it's only
support by Chrome 32) it will fall back to ECDH+AES256 or DH+AES256 or fall
further back to ECDH+AES128, DH+AES. Finally to make sure we can support
back to IE6 we allow ECDH+3DES, DH+3DES, RSA+AES and finally RSA+3DES,
preferring the most secure cipher suite and key exchange that the browser
supports.

.. code::

    ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AES:RSA+3DES:HIGH:!aNULL:!MD5:!DSS

For most browser versions this should provide extremely secure connectivity
and `Forward Secrecy <https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy>`__.

Forcing SSL usage
=================

This one is really quite simple, if you attempt to browse this site using
the unsecure interface (HTTP) you will simply be redirected to a secure
interface.

SSL compression
===============

Thankfully, at time of writing, I am using OpenSSL 1.0.1e and nginx 1.5.8
meaning SSL compression is disabled, you will have to do some Googling to find
out what specific versions you will need to disable SSL compression.

HSTS
====

Finally, I support `HSTS <https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>`__
telling my browser it should only access this website via a secure method, this
is done by simply providing an STS header as shown below.


.. code::

    Strict-Transport-Security: max-age=15768000

Testing
=======

You can use `SSL Labs by Qualys <https://www.ssllabs.com/ssltest/analyze.html>`__
to determine your own website's security and you can look at the
`Qualys report <https://www.ssllabs.com/ssltest/analyze.html?d=kura.io>`__ for
this website as a comparison.
