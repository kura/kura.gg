Speeding up pypip.in and reducing load on PyPI
##############################################
:date: 2014-08-07 08:42
:author: kura
:category: coding
:tags: python, pypipins, pypip.in, shields
:slug: speeding-up-pypip.in-and-reducing-load-on-pypi

.. contents::
    :backlinks: none

As you might expect, `pypip.in <https://pypip.in>`_ employes a fair amount of
caching in the backend to control load on the imaging API and servers.

For a long time, this cache was entirely managed by Varnish and was doing a
fantastic job. Varnish has a hit:miss ration of 10/1, for every 10 hits we get
1 miss. This is a fairly decent ratio when you consider where these images are
displayed, how often they are viewed and that Varnish only caches the images
for an hour.

The impact on PyPI
==================

You will firstly need to understand how pypip.in used to work to understand the
changes that were made and why they were made.

Let's set up the request first - a request for a shield is made and it is not
present in the Varnish cache.

::

    Request received in API layer
                  |
                  v
        API layer queries PyPI
                  |
                  v
       PyPI response translated
                  |
                  v
    Image request for imaging layer

This was true for every request made that did not exist in Varnish's cache.

Generally, if one shield was displayed for a project a second or more usually
was displayed too. This meant when loading the README document on GitHub for a
project would involve pypip.in making more than one request to PyPI for
information and then translating that data.

I decided that caching the initial response for the first request from PyPI to
Redis would be a good idea. This cache is only meant to be short term and is in
place to make multiple images requested at the same time generate faster.

::

           Request received in API layer
                         |
                         v
    API layer queries Redis and falls back to PyPI
                         |
                         v
              PyPI response translated
                         |
                         v
           Image request for imaging layer

Reducing load on the imaging layer
==================================

I realised that out of all of the shields pypip.in serves, all but two of them
are generic and can be re-used.

`Downloads` and `version` information are almost entirely unique but, `Python
versions`, `Python implementations`, `development status`, `wheel`, `egg`,
`format` and `license` are all generic and will be identical for multiple
projects.

It would make perfect sense to cache these images and re-use them as required.
While caching them in Varnish would not be possible due to the URI structure,
caching the images on disk based on their data, colour and mime type would be
perfectly acceptable.

The disks used to power pypip.in are of SSD quality (`thanks DigitalOcean
<https://www.digitalocean.com/?refcode=d76795840b23>`_,) so storing the images
on the disks themselves would be perfectly reasonable and, due to their nature
can be stored for a good length of time. I opted for 24 hours.

Now the diagram looks like this:

::

           Request received in API layer
                         |
                         v
    API layer queries Redis and falls back to PyPI
                         |
                         v
              PyPI response translated
                         |
                         v
       Look for image in generic disk cache or
             request from imaging layer

Due to the nature of the shields and their content, a request has to be made to
Redis or PyPI before a look up can be made to the generic disk cache (we need
to know the text data and shield colour from PyPI data,) it is still a very
good performance improvement on the whole.
