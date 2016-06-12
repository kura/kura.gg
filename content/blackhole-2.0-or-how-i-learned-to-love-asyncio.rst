Blackhole 2.0: or, How I Learned to Love Asyncio
################################################
:date: 2016-05-21 00:20
:author: kura
:category: coding
:tags: python, python3.5, 3.5, asyncio, email, smtp, mta
:slug: blackhole-2.0-or-how-i-learned-to-love-asyncio

.. contents::
    :backlinks: none

A brief history of a tiny part of the Internet.

`Blackhole 1 -- Blackhole as it was originally
known <https://blackhole.io/1>`_ -- was written on `Python 2.7
<https://docs.python.org/2/whatsnew/2.7.html>`_, briefly supporting `Python 2.6
<https://docs.python.org/2.6/whatsnew/2.6.html>`_ for a time and also
supporting early version of `Python 3
<https://docs.python.org/3.2/whatsnew/3.2.html>`_, `PyPy 2
<http://www.pypy.org/features.html>`_ and `PyPy 3
<http://www.pypy.org/features.html>`_. Built on top of `Tornado
<http://www.tornadoweb.org/en/stable/>`_, it was asynchronous in a fashion and
-- quite simply -- worked.

The original prototype that became Blackhole was `SimpleMTA </simplemta>`_ -- a
prototype that was created quickly, to serve a very simple testing purpose that
I had for it.

As I needed SimpleMTA to do more, I wrote Blackhole to accomplish that task.
I'd been using Tornado a bit and wanted to experiment with it more. Building
on top of Tornado created some oddities in how the program was designed and
that always irked me.

Between the time of the last 1.8.X and the 2.0 release, I experimented with
rewriting the program on top of various libraries. The most obvious of these
was `Twisted <https://twistedmatrix.com/trac/>`_. I've always been a fan of
Twisted but I don't like ``theFormattingOfItsFunctionNames`` and -- like too
much of a good thing -- callbacks can be bad for you.

Another experiment was built on top of the old `asyncore
<https://docs.python.org/2/library/asyncore.html>`_ and `asynchat
<https://docs.python.org/2/library/asynchat.html>`_ standard library modules. A
branch of Blackhole 1.8 is indeed built and in working order built on top of
these very modules. Although never merged and released in the wild.

Enter asyncio
=============

Originating as `Tulip <https://github.com/python/asyncio>`_ and merged in to
the Python standard library in `Python 3.4
<https://docs.python.org/3.4/whatsnew/3.4.html>`_, asyncio looked like a great
module to achieve what I wanted to achieve and to force me to actually use
Python 3.

With `Python 3.5 <https://docs.python.org/3.5/whatsnew/3.5.html>`_ came the
`async def
<https://docs.python.org/3.5/reference/compound_stmts.html#async-def>`_
declaration, the `await
<https://docs.python.org/3.5/reference/expressions.html#await>`_ expression and
the `async for
<https://docs.python.org/3.5/reference/compound_stmts.html#async-for>`_
statement.

Since Blackhole is a tool written by me, for me and exposed as a service, it
made complete sense for me to jump-in-at-the-deep-end as it were and rewrite
the entirety of the software specifically for Python 3.5.

Doing so meant I bypassed the need to use the ``@coroutine`` decorator and the
``yield from`` expression, instead using their 3.5 equivalents in ``async def``
and ``await`` respectively.

All I see are bytes
===================

The trickest part for me was forcing myself to remember that the data passed
to and from the socket in Python 3 are bytes.

That took a little while of constantly smashing my head in to my desk to
realise and remember. If something didn't work during development, it was
always because I forgot to use ``.encode()`` or ``.decode()``.

Getting to grips with asyncio
=============================

I can honestly say that, with a little reading and checking out how some
libraries like `aiohttp <https://github.com/KeepSafe/aiohttp>`_ work, I got to
grips with the actual ``asyncio`` module pretty quickly.

I found using the ``async def`` and ``await`` syntax made it even easier for me
to read and write the code, because I instantly knew how a function I'd written
previously should work, simply by looking at it's declaration. Something I
have sometimes forgotten when passing callbacks all over the place.

Show me the code
================

So, let's take a specific task and look at the code that handles it, written
on top of asyncio in Python 3.5.

First up I'll show the method that waits for data to be received on the socket.

.. code-block:: python3

    async def wait(self):
        """
        Wait for data from the client.
        :returns: A line of received data.
        :rtype: :any:`str`
        .. note::
           Also handles client timeouts if they wait too long before sending
           data. -- https://blackhole.io/configuration-options.html#timeout
        """
        while not self.connection_closed:
            try:
                line = await asyncio.wait_for(self._reader.readline(),
                                              self.config.timeout,
                                              loop=self.loop)
            except asyncio.TimeoutError:
                await self.timeout()
                return None
            return line

This function waits for data to be received from a client and returns it once
it's been received.

.. code-block:: python3

    async def wait(self):

The declaration of this function is different to how you'd write it for Python
3.4 or lower.

The equivalent of this declaration for Python 3.4 is as follows:

.. code-block:: python3

    @coroutine
    def wait(self):

Both ways declare that the function is an asynchronous coroutine.

.. code-block:: python3

    while not self.connection_close:

This line does exactly what you'd expect, it runs the while loop until
``self.connection_closed`` does not equal ``False`` or until the loop is exited
for another reason.

This simply allows the connection handler to have connection state and stop
waiting for data if the connection is terminated elsewhere. Because the
entire program is asynchronous, the connection state may get modified elsewhere
while this method is still waiting for new data.

The ``try except`` block actually works with the while statement.

.. code-block:: python3

    try:
        line = await asyncio.wait_for(self._reader.readline(),
                                      self.config.timeout,
                                      loop=self.loop)

It's easier to explain the arguments of the ``wait_for`` method before anything
else.

``self._reader.readline()`` reads a line of data from a socket stream,
``self.config.timeout`` is the maximum time in seconds to wait for data, for
the sake of this example, let's call it ``10`` and finally ``loop=self.loop``
sets the event loop that the code executes on.

``asyncio.wait_for`` creates an asynchronous task that waits for the
``self._reader.readline()`` future to complete or raises an
``asyncio.TimeoutError`` if the future does not complete within the time limit.

As a example.

.. code-block:: python3

    await asyncio.wait_for(self._reader.readline(), 10)

Would wait for data for 10 seconds before raising a timeout error.

.. code-block:: python3

    except asyncio.TimeoutError:
        await self.timeout()
        return None

How the exception is handled shows how the ``while`` statement is used. When a
timeout exception is raised, part of the code that handles that in the
``self.timeout()`` method changes the ``connection_closed`` value.

And finally the data received is returned.

.. code-block:: python3

    return line

Without going in to too much detail, below is the piece of code for handling
a timeout and terminating a connection, setting ``connection_closed`` to exit
all possibly running ``while`` loops.

.. code-block:: python3

    async def timeout(self):
        """
        Timeout a client connection.
        Sends the 421 timeout message to the client and closes the connection.
        https://blackhole.io/configuration-options.html#timeout
        """
        await self.push(421, 'Timeout')
        await self.close()

    async def close(self):
        """Close the connection from the client."""
        if self._writer:
            try:
                self.clients.remove(self._writer)
            except ValueError:
                pass
            self._writer.close()
            await self._writer.drain()
        self._connection_closed = True


lambda woes aka. use functools.partial
======================================

Later in the development of the new version of blackhole I added a feature
called ``flags``. These flags allow multiple listeners to be configured with
different runtime parameters. i.e. bounce all emails received on port 587
while accepting all emails received on port 25.

These flags allow flexibility to control how email is handled on any specified
port.

It was during development of this feature that I discovered using a lambda
rather than a partial object from functools didn't work quite how I was
expecting it to.

The original piece of code iterated over each socket object and created an
asyncio server object for that socket as below.

.. code-block:: python3

    async def _start(self):
        """Create an asyncio 'server' for each socket."""
        for sock in self.socks:
            server = await self.loop.create_server(lambda: Smtp(self.clients),
                                                   **sock)
            self.servers.append(server)

I wanted to change this code to pass in a set of flags that also belonged to
that specific socket, as below.

.. code-block:: python3

    async def _start(self):
        """Create an asyncio 'server' for each socket."""
        for sock in self.socks:
            flags = sock['flags']
            server = await self.loop.create_server(lambda: Smtp(self.clients,
                                                                flags=flags),
                                                   **sock)
            self.servers.append(server)

Can you spot the problem?

When using a lambda in that context, creating an anonymous function to pass to
the ``create_server`` method, I discovered the flag arguments were incorrect.
In fact, none of the sockets had their correct flags set, they were being
jumbled up instead of being used as expected.

I'm not sure why that's the case and I never actually looked it up to find out
why either. I knew the way to fix it was to use ``functools.partial`` and it's
also a nice, cleaner way to do it so I did.

.. code-block:: python3

    async def _start(self):
        """Create an asyncio 'server' for each socket."""
        for sock in self.socks:
            flags = sock['flags']
            factory = functools.partial(Smtp, self.clients, flags=flags)
            server = await self.loop.create_server(factory, **sock)
            self.servers.append(server)

So is asyncio any good?
=======================

I'm going to roundup this article with this possibly loaded and difficult
question.

Well, is it?

In my eyes, yes. I have to admit that this is the first time in a very long
time -- possibly ever -- that I have fallen so head-over-heels in-love with a
library or module.

I went from someone that didn't use Python 3 and grudgingly added Python 3
support to libraries I've written, to someone that only uses Python 3.5 now.

I haven't use asyncio with Python 3.4 and I probably never will, I like the
3.5-only syntax changes far too much to go backwards and start using the
``@coroutine`` decorator and ``yield from`` statement.

My only gripe is that currently STARTTLS is not supported. Hopefully that will
arrive in the not-so-distant future and I understand why it's currently not
supported.
