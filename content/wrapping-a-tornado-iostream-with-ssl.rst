Wrapping a Tornado IOStream with SSL
####################################
:date: 2013-07-29 20:00
:author: kura
:category: coding
:tags: python, tornado, iostream, ssl, blackhole
:slug: wrapping-a-tornado-iostream-with-ssl

.. contents::

As part of my effort to make `Blackhole <http://blackhole.io/>`_ as
useful and usable as possible, I needed to be able to support SSL/TLS
enabled connections.

Tornado itself has two built-in IOStreams that help us do the job;
the first is the standard `IOStream <http://www.tornadoweb.org/en/stable/iostream.html#tornado.iostream.IOStream>`_
and the second is the `SSLIOStream <http://www.tornadoweb.org/en/stable/iostream.html#tornado.iostream.SSLIOStream>`_.

With this in mind we simply need to spawn two sockets, by default these
listen on port 25 for standard SMTP and port 465 for SSL/TLS
encrypted SMTP. With these two sockets bound we're then very
simply able to listen for incoming connections on either socket
and use `socket.socket.getsockname()` to figure out if the
connection is to the encrypted or unencrypted socket.

Code
====

.. code:: python

    def connection_stream(connection):
        """
        Detect which socket the connection is being made on,
        create and iostream for the connection, wrapping it
        in SSL if connected over the SSL socket.

        The parameter 'connection' is an instance of 'socket'
        from stdlib.
        """
        if connection.getsockname()[1] == options.ssl_port and options.ssl:
            try:
                ssl_connection = ssl.wrap_socket(connection, **sslkwargs)
            except (ssl.SSLError, socket.error) as e:
                if e.errno == ssl.SSL_ERROR_EOF or e.errno == errno.ECONNABORTED:
                    ssl_connection.close()
                    return
                else:
                    raise
            # Do a nasty blanket Exception until SSL exceptions are fully known
            try:
                return iostream.SSLIOStream(ssl_connection)
            except Exception as e:
                log.error(e)
                ssl_connection.close()
                return
        else:
            return iostream.IOStream(connection)

So let's explain a little bit how this works.

if connection.getsockname...
============================

.. code:: python

    if connection.getsockname()[1] == options.ssl_port and options.ssl:

This piece of code checks the second value in the list returned by `getsockname()`,
this item in the list will be the port number the socket is listening to.

So we simply check to see if it's the configured SSL/TLS port and if
SSL/TLS is turned on.

1st try... except...
====================

.. code:: python

    try:
        ssl_connection = ssl.wrap_socket(connection, **sslkwargs)
    except (ssl.SSLError, socket.error) as e:
        if e.errno == ssl.SSL_ERROR_EOF or e.errno == errno.ECONNABORTED:
            ssl_connection.close()
            return
        else:
            raise


The first try/except group will attemp to wrap the socket using Python's
built-in SSL.

.. code:: python

    ssl_connection = ssl.wrap_socket(connection, **sslkwargs)

If this throws an exception we try to determine what caused it and
close the connection, otherwise we raise the exception and crash out.
It's not the nicest way to do it but in theory you shouldn't be able
to reach the else (I may be wrong on this point though...).

2nd try... except...
====================

.. code:: python

    # Do a nasty blanket Exception until SSL exceptions are fully known
    try:
        return iostream.SSLIOStream(ssl_connection)
    except Exception as e:
        log.error(e)
        ssl_connection.close()
        return

Here we simply try to return an instance of Tornado's
`iostream.SSLIOStream`, if we get any kind of Exception it will be
raised, logged and the connection will be close.

else
====

.. code:: python

    else:
        return iostream.IOStream(connection)

And the final else will return an instance of Tornado's
`iostream.IOStream` if SSL/TLS is disabled or if the connection
was made to the non SSL/TLS port.
