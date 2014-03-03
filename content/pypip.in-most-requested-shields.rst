pypip.in most requested shields
###############################
:date: 2014-03-03 21:40
:author: kura
:category: misc
:tags: python, pypi, pip
:slug: pypip.in-most-requested-shields

.. contents::

pypip.in
========

`pypip.in <https://pypip.in/>`__ is a website `I have written about before
<https://kura.io/2013/12/24/shields-for-pypi-packages/>`__.

I decided I would look at the shields and see which ones were the most
requested so far this year.

Due to the volumn of requests, I only keep 90 days of logs from nginx and no
logs from Varnish, pypipin or the local version of buckler.

nginx sits in front of Varnish so, even if Varnish responds with a cached
version of the shield, a log line is still written to say it was requested.

Top 20
======

1. `requests <http://docs.python-requests.org/en/latest/index.html>`__ [downloads]
2. `Pillow <http://pillow.readthedocs.org/en/latest/>`__ [version]
3. Pillow [downloads]
4. `Theano <http://deeplearning.net/software/theano/>`__ [version]
5. Theano [downloads]
6. `fake-factory <http://github.com/joke2k/faker>`__ [downloads]
7. `livestreamer <http://livestreamer.tanuki.se/en/latest/install.html>`__ [downloads]
8. `django-cms <https://www.django-cms.org/en/>`__ [downloads]
9. django-cms [version]
10. `speedtest-cli <https://github.com/sivel/speedtest-cli>`__ [version]
11. speedtest-cli [downloads]
12. `boto <http://boto.readthedocs.org/en/latest/>`__ [downloads]
13. `thumbor <https://github.com/globocom/thumbor>`__ [downloads]
14. thumbor [version]
15. `pip <http://www.pip-installer.org/en/latest/>`__ [version]
16. `tweepy <https://pythonhosted.org/tweepy/html/>`__ [version]
17. tweepy [downloads]
18. `django-allauth <http://django-allauth.readthedocs.org/en/latest/>`__ [downloads]
19. `pymssql <http://pymssql.org/>`__ [downloads]
20. pymssql [version]

The first thing that struck me is that I actually hadn't heard of or used
quite a lot of those packages from the list.

The second thing that struck me is the popularity of the pymssql package, but
that popularity in this instance is only based on the number of requests for
the shields and cannot be used to verify the usage popularity of the package
itself.

Anyway, pretty much useless information, but I was bored.
