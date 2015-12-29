DNSSEC with Rage4 and name.com
##############################
:date: 2015-10-18 03:10
:author: kura
:category: tutorials
:tags: dnssec, dns, rage4. name.com
:slug: dnssec-with-rage4-and-name.com

I currently use `name.com <https://www.name.com/>`_ as my registrar and I use
`Rage4 <https://rage4.com/>`_ because Rage4 are awesome, they also support TLSA
and SSHFP records and of course, DNSSEC.

I'm writing this up because I found getting DNSSEC from Rage4 to work with
name.com as my registrar was a pain and the name.com support were not very helpful,
linking me to a support article that I'd already read and did not help at all.

Rage4
=====

I'm going to assume you've already got your records in Rage4, if not, the
interface is really easy so you'll figure it out.

Within the management section for your domain's zone, there is a menu bar of
icons, the icon pictured below enabled DNSSEC.

.. image:: /images/rage4-dnssec-icon.png
    :alt: Enabled DNSSEC

Clicking this will turn on DNSSEC. You will then have a new icon that will
allow you to display your DNSSEC information.

.. image:: /images/rage4-dnssec-info-icon.png
    :alt: Display DNSSEC info

Clicking this icon will give you a window that is similar to the image below,
containing all of the DNSSEC info you need. You will also have several extra
fields but you'll only need the ones shown below.

.. image:: /images/rage4-dnssec-info.png
    :alt: DNSSEC info

name.com
========

With the information from Rage4, you now need to go to name.com and configure
DNSSEC on your registrar.
`This support page <https://www.name.com/support/articles/205439058-DNSSEC>`_
will guide you through their interface.

The form is slightly confusing since it has different naming conventions than
the information provided by Rage4.

Below is an image of the form with pre-filled data taken from the previous
image from Rage4.

.. image:: /images/name.com-dnssec-form.png
    :alt: Pre-filled DNSSEC form

You can fill this form in and submit it for both type 1 (RSASHA1) and type 2
(RSASHA256.)

Testing
=======

It may take some time for your DNSSEC information to propagate but you can test
it using `the debugger from Verisign <http://dnssec-debugger.verisignlabs.com/>`_.
