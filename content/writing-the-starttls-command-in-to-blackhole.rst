Writing the STARTTLS command in to Blackhole
############################################
:date: 2013-07-31 13:36
:author: kura
:category: coding
:tags: python, tornado, iostream, ssl, starttls, blackhole
:slug: writing-the-starttls-command-in-to-blackhole

.. contents::

Blackhole has always been able to handle unencrypted SMTP and
for a long time it's been able to handle encrypted SMTP via TLSv1.

One thing Blackhole hasn't been able to do until the 1.7.0 release
is handle `STARTTLS`.

In the past the `STARTTLS` command would cause Blackhole to return the
standard `250 OK` response but would continue to operate on unencrypted
SMTP.

I wanted to fix this and do it properly, but this meant learning how
to do so with Tornado, which itself proved to be tricky. I ended up
deciding to go to my local coding spot - the pub and hash it out.

connection_stream
=================

The first thing I had to do was refactor the code that created the
instance of `tornado.iostream.IOStream` and `tornado.iostream.SSLIOStream`
so that it didn't actually do the ssl wrapping.

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
            return ssl_connection(connection)
        else:
            return iostream.IOStream(connection)

ssl_connection
==============

In doing so I added another method that actually created an instance of
`tornado.iostream.SSLIOStream`.

.. code:: python

    def ssl_connection(connection):
        try:
            ssl_connection = ssl.wrap_socket(connection, **sslkwargs)
            return iostream.SSLIOStream(ssl_connection)
        except (ssl.SSLError, socket.error) as e:
            if e.errno == ssl.SSL_ERROR_EOF or e.errno == errno.ECONNABORTED:
                ssl_connection.close()
                return

This now gave me the ability to create an instance of `SSLIOStream` without
doing all of the port checks that are required to create it when a connection
is made through the SSL enabled port.

Next I had to find a way of modifying the stream on-the-fly, which was really
just a case of adding the current stream as an attribute of the `MailState`
object which is unique for each connection to the server.

The next and final step was to identify if `STARTTLS` had been called and
overwrite the stream attribute of `IOStream` with `SSLIOStream`... This is
where everything got tricky.

Broken file descriptors
=======================

Tornado would error out when `STARTTLS` was called with the following error

.. code:: python

    Exception in callback <functools.partial object at 0x26d8260>
        Traceback (most recent call last):
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/ioloop.py", line 453, in _run_callback
            callback()
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/stack_context.py", line 241, in wrapped
            callback(*args, **kwargs)
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/iostream.py", line 316, in wrapper
            callback(*args)
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/stack_context.py", line 241, in wrapped
            callback(*args, **kwargs)
          File "/home/kura/workspace/blackhole.io/blackhole/connection.py", line 212, in handle
            loop()
          File "/home/kura/workspace/blackhole.io/blackhole/connection.py", line 219, in loop
            mail_state.stream.read_until("\n", handle)
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/iostream.py", line 148, in read_until
            self._try_inline_read()
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/iostream.py", line 404, in _try_inline_read
            self._maybe_add_error_listener()
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/iostream.py", line 550, in _maybe_add_error_listener
            self._add_io_state(ioloop.IOLoop.READ)
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/iostream.py", line 580, in _add_io_state
            self.fileno(), self._handle_events, self._state)
          File "/home/kura/.virtualenvs/blackhole-python2.7/local/lib/python2.7/site-packages/tornado-3.0.1-py2.7.egg/tornado/ioloop.py", line 516, in add_handler
            self._impl.register(fd, events | self.ERROR)
        IOError: [Errno 17] File exists

I had no choice at this point but to do what I always do when I'm stumped,
`head over to the mailing list! <https://groups.google.com/forum/#!topic/python-tornado/>`_

I didn't get a response for a while so while waiting I decided to ask some intelligent
people.

I pointed a tweet at `@alex_gaynor <https://twitter.com/alex_gaynor>`_ which was
responded to by `@fijall <https://twitter.com/fijall>`_ but neither could help.
Alex mentioned Twisted which triggered a response from `@hynek <https://twitter.com/hynek>`_
but sadly still no solution.

The fix
=======

Then I received an email response from Ben Darnell on the Tornado mailing list which pointed
me in the right direction.

In the end the simple fix was to modify the instance of `tornado.ioloop.IOLoop` during run time
and removed the original instance of `IOStream` from it.

.. code:: python

    if line.lower().startswith("starttls"):
        fileno = mail_state.stream.socket.fileno()
        IOLoop.current().remove_handler(fileno)
        mail_state.stream = ssl_connection(connection)

connection_ready
================

You can see this at work in the final version of the connect_ready method.

.. code:: python

    def connection_ready(sock, fd, events):
        """
        Accepts the socket connections and passes them off
        to be handled.

        'sock' is an instance of 'socket'.
        'fd' is an open file descriptor for the current connection.
        'events' is an integer of the number of events on the socket.
        """
        while True:
            try:
                connection, address = sock.accept()
            except socket.error as e:
                if e.errno not in (errno.EWOULDBLOCK, errno.EAGAIN):
                    raise
                return

            log.debug("Connection from '%s'" % address[0])

            connection.setblocking(0)
            stream = connection_stream(connection)
            if not stream:
                return
            mail_state = MailState()
            mail_state.email_id = email_id()
            mail_state.stream = stream

            # Sadly there is nothing I can do about the handle and loop
            # fuctions. They have to exist within connection_ready
            def handle(line):
                """
                Handle a line of socket data, figure out if
                it's a valid SMTP keyword and handle it
                accordingly.
                """
                log.debug("[%s] RECV: %s" % (mail_state.email_id, line.rstrip()))
                resp, close = handle_command(line, mail_state)
                if resp:
                    if isinstance(resp, list):
                        for r in resp:
                            write_response(mail_state, r)
                    else:
                        # Otherwise it's a single response
                        write_response(mail_state, resp)
                if line.lower().startswith("starttls"):
                    fileno = mail_state.stream.socket.fileno()
                    IOLoop.current().remove_handler(fileno)
                    mail_state.stream = ssl_connection(connection)
                if close is True:
                    log.debug("Closing")
                    mail_state.stream.close()
                    del mail_state.stream
                    return
                else:
                    loop()

            def loop():
                """
                Loop over the socket data until we receive
                a newline character (\n)
                """
                # Protection against stream already reading exceptions
                if not mail_state.stream.reading():
                    mail_state.stream.read_until("\n", handle)

            hm = "220 %s [%s]\r\n" % (get_mailname(), __fullname__)
            mail_state.stream.write(hm)
            loop()
