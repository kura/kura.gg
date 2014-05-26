Software
########
:date: 2014-05-26 12:30:00
:author: kura
:slug: software

.. contents::

apt
===

I run my own APT repository with custom builds of;

- nginx (1.7.0 with pagespeed 1.7.30.3-beta)
- haproxy (1.5-dev25)

and several of my own packages;

- `vagrant-bash-completion <https://kura.io/vagrant-bash-completion/>`__
- `go-bash-completion <https://kura.io/go-bash-completion/>`__
- `denyhosts-unban <https://kura.io/denyhosts-unban/>`__

A detailed guide on how to use this repository can be found 
`here <https://kura.io/apt.kura.io/>`__.

Software
========

Blackhole
---------

Blackhole is a fake MTA (mail transfer agent) that is designed blindly accept,
bounce or reject all inbound and outbound email without actually processing or
storing any of the data. This makes it safe for handling large volumes of
email messages.

Blackhole is designed mostly for testing purposes and can be used to test numerous things suchs as;

- Email send rates, if you need to test how much mail you can send per minute, hour etc
- Email integration testing and finally
- if you work in the real world, chances are you’ll need work on a copy of production
  data from time to time. You can try to anonymous all the data but there is always a chance
  you’ll miss something. Configuring blackhole as your applications default SMTP gateway
  will remove any chance of a real person receiving an email they shouldn’t have received.

It is available as source and as SaaS.

`https://blackhole.io <https://blackhole.io/>`__

Am I Secure
-----------

Am I Secure is a relatively simple Python script that will check *some* of your
server configuration and report on security and configuration issues.

`/amisecure <https://kura.io/amisecure/>`__

pypipin
-------

pypipin is a SaaS that provides shields for your GitHub repository, documentation
or website powered by information directly from PyPI.

`https://pypip.in <https://pypip.in/>`__

Deiman
------

Deiman is a Python utility class for daemonizing a process. It has start and
stop methods as well as a method for retrieving a process status information.
It can also detect stale PIDs and remove them.

`/deiman <https://kura.io/deiman/>`__

PyBozo
------

PyBozo is a Python implementation of BozoCrack for using Google to crack
unsalted MD5 passwords.

`/pybozo <https://kura.io/pybozo/>`__

Pelican [YouTube/Vimeo]
-----------------------

Pelican YouTube and Vimeo are a set of plugins that enable you to embed videos
in to your pages and articles.

`/pelican-youtube <https://kura.io/pelican-youtube/>`__
`/pelican-vimeo <https://kura.io/pelican-vimeo/>`__

apt-security
------------

A simple set of commands to allow you to update to the security releases
without updating your entire operating system.

`/apt-security <https://kura.io/apt-security/>`__

rabbitmq-nagios
---------------

A set of plugins for Nagios to monitor RabbitMQ using *rabbitmqctl*.

`/rabbitmq-nagios <https://kura.io/rabbitmq-nagios/>`__

denyhosts-unban
---------------

Tool for unbanning people from DenyHosts without having to manually edit half a
dozen files.

`/denyhosts-unban <https://kura.io/denyhosts-unban/>`__

Bash completion
---------------

- `go-bash-completion <https://kura.io/go-bash-completion/>`__
- `vagrant-bash-completion <https://kura.io/vagrant-bash-completion/>`__
- `tugboat-bash-completion <https://github.com/kura/tugboat-bash-completion>`__