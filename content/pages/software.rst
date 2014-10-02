Software
########
:slug: software

.. contents::
    :backlinks: none

apt
===

I run my own APT repository with custom builds of;

- nginx (1.7.6 with pagespeed 1.9.32.1, naxsi 0.53-2)
- haproxy (1.6-dev0)

and several of my own packages;

- `vagrant-bash-completion </vagrant-bash-completion/>`__
- `go-bash-completion </go-bash-completion/>`__
- `denyhosts-unban </denyhosts-unban/>`__

A detailed guide on how to use this repository can be found
`here </apt.kura.io/>`__.

Software
========

Yarg
----

Yarg is a PyPI client, it was written for `pypip.in
<https://pypip.in>`_ and can search packages as well as read the RSS feeds
from PyPI for new packages and new package version releases.

`/yarg </yarg>`_

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

`/amisecure </amisecure/>`__

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

`/deiman </deiman/>`__

PyBozo
------

PyBozo is a Python implementation of BozoCrack for using Google to crack
unsalted MD5 passwords.

`/pybozo </pybozo/>`__

Pelican [YouTube/Vimeo]
-----------------------

Pelican YouTube and Vimeo are a set of plugins that enable you to embed videos
in to your pages and articles.

`/pelican-youtube </pelican-youtube/>`__
`/pelican-vimeo </pelican-vimeo/>`__

Pelican FontAwesome
-------------------

Pelican FontAwesome allows you to embed FontAwesome icons in your RST documents.

`/pelican-fontawesome </pelican-fontawesome>`__

Pelican GitHub Projects
-----------------------

Pelican GitHub Projects allows you to embed a list of your public GitHub
projects in your pages.

`/pelican-githubprojects </pelican-githubprojects>`_

apt-security
------------

A simple set of commands to allow you to update to the security releases
without updating your entire operating system.

`/apt-security </apt-security/>`__

rabbitmq-nagios
---------------

A set of plugins for Nagios to monitor RabbitMQ using *rabbitmqctl*.

`/rabbitmq-nagios </rabbitmq-nagios/>`__

denyhosts-unban
---------------

Tool for unbanning people from DenyHosts without having to manually edit half a
dozen files.

`/denyhosts-unban </denyhosts-unban/>`__

Bash completion
---------------

- `go-bash-completion </go-bash-completion/>`__
- `vagrant-bash-completion </vagrant-bash-completion/>`__
- `tugboat-bash-completion </tugboat-bash-completion>`__

Pelican Themes
==============

Ghastly
-------

A clean and minimal, lightweight theme for the
`Pelican <http://getpelican.com>`__ blogging platform. Ghastly is based
heavily off of Casper, the default theme for `Ghost <https://ghost.org>`__.

`/ghastly </ghastly/>`__

Hauntr
------

Hauntr is a minimal, lightweight and clean theme for the
`Pelican <http://getpelican.com>`__ blogging platform.

It is named after the Pokemon 'Haunter' because it is a modified version
(you might say evolved) of my previous theme, `Ghastly
<https://kura.io/ghastly/>`__.

`/hauntr </hauntr/>`__
