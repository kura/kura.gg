AFK, an SMS sender and way too much PHP...
##########################################
:date: 2010-06-13 15:09
:author: kura
:category: Uncategorized
:tags: afk, php, python, sms
:slug: afk-an-sms-sender-and-way-too-much-php

Sadly of late I've been stuck writing nothing but PHP during my work
hours. Short of a few major internal disasters I've done nothing I would
count as interesting enough to really post about, until recently.

A week or two ago I made some modifications to our internal Nagios
monitoring system - `http://nagios.com/`_ - which saw me writing a
Python-powered sms script which takes Nagios messages and passes them to
our SMS provider API and delivers them to my phone.

.. _`http://nagios.com/`: http://nagios.com/

The code isn't exactly pretty and it's rather simple but it does the job
and uses LXML to actually generate the message that gets posted to the
API - http://iamkura.com/sms

Fortunately the last week or so has seen me working heavily with Xapian
(`http://xapian.org/`_), Sphinx (`http://sphinxsearch.com/`_) and the
wonderful Solr (`http://lucene.apache.org/solr/`_) to see which is
better for various modifications to our projects. Xapian failed
miserably in my book when it came to being used with PHP so was dropped
very quickly, Sphinx showed itself to be a very, very fast full text
search engine and will definitely be used in the future but, for what we
need so far, Solr is by far the best and it's faceting ability is
amazing.

.. _`http://xapian.org/`: http://xapian.org/
.. _`http://sphinxsearch.com/`: http://sphinxsearch.com/
.. _`http://lucene.apache.org/solr/`: http://lucene.apache.org/solr/

More to come on that last paragraph in the following week including
"howto" articles on installing, configuring and using Sphinx and Solr.
