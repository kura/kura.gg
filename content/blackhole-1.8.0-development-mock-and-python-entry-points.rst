Blackhole 1.8.0 development, Mock and Python entry_points
#########################################################
:date: 2013-08-18 12:00
:author: kura
:category: coding
:tags: python, blackhole, setup.py, entry_points, mock, tests, testing
:slug: blackhole-1.8.0-development-mock-and-python-entry-points

.. contents::
    :backlinks: none

Over the last week I've been doing a huge amount of refactoring of
`Blackhole <https://blackhole.io>`_ as well as writing dozens of additional
tests. To make Blackhole more testable I needed to make a big change to
how the program is launched and controlled.

setup.py scripts vs. entry_points
=================================

Whenever I've written Python programs that require some kind of command line
script I've always used distutils' scripts, this can be seen `in blackhole's
setup.py on GitHub <https://github.com/kura/blackhole/blob/05c6647aeb25ecfcc17d9df535db330a68016a24/setup.py#L37-L39>`_
or in the three line example below.

.. code-block:: python

      scripts=[
          'blackhole/bin/blackhole',
      ],

In doing so, it allowed me to be lazy and write a lot of prodecural code in the
main "binary" which made it pretty much impossible to test. You can also see
that `on GitHub in the main "binary"
<https://github.com/kura/blackhole/blob/bb6cccca3a75def324ed5cb64a32fd2e5773a038/blackhole/bin/blackhole>`_.

I've noticed that most people who write Python packages that have some kind of
command line entry point use distutils' `entry_points` option instead of
`scripts`. I decided to rewrite Blackhole to make it use the same entry_points
option and also make it's new entry point as testable as possible.

setup.py entry_point change
---------------------------

.. code-block:: python

    entry_points = {
        'console_scripts': [
            'blackhole = blackhole.application:run',
        ]
    }

    setup(name='blackhole',
          # ...
          entry_points=entry_points,
          # ...
          )

I'm not going to go in to any real detal on how `entry_points` works, there are
plenty of articles elsewhere on the internet that detail this.

That being said, `entry_points` is a dictionary, in it I set a `console_scripts`
key that has a list of scripts that should be usable from the command line.

Each list item is made up of two parts; the command name (what will be typed on
the command line to trigger the command) and the module(s) and method to run.

blackhole.application:run
-------------------------

With the `entry_points` changes outlined above, this allowed me to write an
entirely new and testable application.

Now the method that launches Blackhole is much smaller and split in to testable
parts.

For example the `run` method is below.

.. code-block:: python

    def run():
        """
        The run method is what actually spawns and manages blackhole.
        """
        signal.signal(signal.SIGTERM, terminate)
        action = set_action()
        set_options()
        # Grab the sockets early for multiprocessing
        if action in ('start',):
            socks = sockets()
            setgid()
            setuid()
        d = daemon(action)
        # Change group and user
        io_loop = fork()
        # Iterate over the dictionary of socket connections
        # and add them to the IOLoop
        for _, sock in socks.iteritems():
            callback = functools.partial(connection_ready, sock)
            io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
        try:
            io_loop.start()
        except (KeyboardInterrupt, SystemExit):
            io_loop.stop()
            d.stop()
            sys.exit(0)

For the full set of changes, take a look `on GitHub at blackhole.application
<https://github.com/kura/blackhole/blob/05c6647aeb25ecfcc17d9df535db330a68016a24/blackhole/application.py>`_.

Fun with Mock
=============

`Mock <https://www.voidspace.org.uk/python/mock/>`_ is an amazing library that
allows you to mock (fake) method calls and much more.

I've known about Mock for a while, it's used quite heavily at work but I've
never really felt like I needed to use it. Then I started writing more and more
tests for Blackhole, started using Mock and instantly fell in love.

Mocking FQDN
------------

As an example, with Blackhole 1.6.4 I added functionality to return an FQDN
when HELO or EHLO commands are received. I didn't write any tests for this
because it uses a file on the filesystem or falls back to getting the FQDN
from the socket library.

After playing with Mock, I decided I would actually write tests for this piece
of functionality and thankfully Mock made it insanely simple.

.. code-block:: python

    class TestMailNameFile(unittest.TestCase):
        check_value = "file.blackhole.io"

        @patch('os.path.exists', return_value=True)
        def test_mail_name_file(self, exists_mock):
            try:
                with patch('__builtin__.open',
                           return_value=StringIO(self.check_value)):
                    mn = get_mailname()
                    self.assertEqual(mn, self.check_value)
            except ImportError:
                with patch('builtins.open',
                           return_value=StringIO(self.check_value)):
                    mn = get_mailname()
                    self.assertEqual(mn, self.check_value)

The above test mocks the filesystem calls, returning a known value. This allows
the tests to be run no matter how the machine running the tests is configured.

The one slightly less standard part of this test is the fact it has a
try: except: block inside it, this is because I need to mock Python's builtin
`open` method. Blackhole works on both Python 2.6/7 and on Python 3.X and with
Python 3 the `open` method was moved from `__builtin__.open` to `builtins.open`.
As such I have to attempt to run the Python 2.X version of the code and fallback
to Python 3.X version if the import fails.

.. code-block:: python

    class TestMailNameSocket(unittest.TestCase):
        check_value = "socket.blackhole.io"

        @patch('os.path.exists', return_value=False)
        @patch('socket.getfqdn', return_value=check_value)
        def test_mail_name_socket(self, exists_mock, socket_mock):
            mn = get_mailname()
            self.assertEqual(mn, self.check_value)

And the test above is for forcing the FQDN to be returned by Python's socket
library, again the return value is a known value so that it can be tested
on any machine.

Mocking --delay and --debug options
-----------------------------------

Very little changes when the `--delay` and `--debug` arguments are passed in to
Blackhole and sadly it's quite hard to test both of those calls.

One thing that I would like to test is that a relevant warning message is
printed out to the console when either of these arguments is passed. Because
both options can be quite dangerous to use.

It's kind of a pointless thing to test for but it's also nice to know that the
user is being warned correctly.

With Mock I am able to to mock `sys.stdout` and have it write the output to
`StringIO` instead, so I can test the contents of `StringIO` and confirm they
match what I expect them to be.

.. code-block:: python

    class TestSetOptionsDebug(unittest.TestCase):

        def setUp(self):
            options.delay = 0
            options.debug = True
            options.ssl = False

        @patch('sys.stdout', new_callable=StringIO)
        def test_set_options_debug(self, stdout_mock):
            val = """WARNING: Using the debug flag!\nThis will generate a lots"""\
                  """ of disk I/O and large log files\n\n"""
            set_options()
            self.assertEquals(stdout_mock.getvalue(), val)


    class TestSetOptionsDelay(unittest.TestCase):

        def setUp(self):
            options.debug = False
            options.delay = 1
            options.ssl = False

        @patch('sys.stdout', new_callable=StringIO)
        def test_set_options_delay(self, stdout_mock):
            val = """WARNING: Using the delay flag!\n"""\
                  """The delay flag is a blocking action """\
                  """and will cause connections to block.\n\n"""
            set_options()
            self.assertEquals(stdout_mock.getvalue(), val)

Mocking daemon actions
----------------------

Another thing that is nice to test is that the daemon is working correctly. I
decided it would be a good idea to mock start, stop and status commands as well
as mocking unknown commands too, to be sure how Blackhole would respond to a
user's actions.

Thankfully Mock allows you to mock calls and confirm that they have indeed been
called, for example the stop method calls `sys.exit`, so I can confirm that this
call has actually been made.

.. code-block:: python

    class TestDaemonStop(unittest.TestCase):

        def setUp(self):
            sys.argv = ('blackhole', 'stop')

        @patch('sys.exit')
        @patch('deiman.Deiman.stop')
        def test_daemon_stop(self, exit_mock, daemon_mock):
                daemon('stop')
                assert daemon_mock.called
                assert exit_mock.called


    class TestDaemonStatus(unittest.TestCase):

        def setUp(self):
            sys.argv = ('blackhole', 'status')

        @patch('sys.exit')
        @patch('deiman.Deiman.status')
        def test_daemon_status(self, exit_mock, daemon_mock):
                daemon('status')
                assert daemon_mock.called
                assert exit_mock.called


    class TestDaemonStart(unittest.TestCase):

        def setUp(self):
            sys.argv = ('blackhole', 'start')

        @patch('deiman.Deiman.start')
        def test_daemon_start(self, daemon_mock):
                d = daemon('start')
                assert daemon_mock.called
                self.assertTrue(isinstance(d, Deiman))


    class TestDaemonInvalidAction(unittest.TestCase):

        @patch('sys.exit')
        def test_daemon_invalid_action(self, exit_mock):
                daemon('kurakurakura')
                assert exit_mock.called
