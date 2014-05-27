Automatic/Unattended updates on Debian 6 (Squeeze)
##################################################
:date: 2012-01-28 17:41
:author: kura
:category: tutorials
:tags: automatic update, debian, unattended-upgrades, update
:slug: automaticunattended-updates-on-debian-6-squeeze

.. contents::
    :backlinks: none

The unattended-upgrades package used on Debian is based on the one from
Ubuntu. It is generally pretty safe in my opinion but I only ever enable
it for security upgrades.

Installation
------------

.. code:: bash

    apt-get install unattended-upgrades apticron

*unattended-upgrades* handles the actual updates, *apticron* is used for
emailing you of available updates - it is not required but I like it.

Configuring unattended-upgrades
-------------------------------

Open up **/etc/apt/apt.conf.d/50unattended-upgrades** and change it to
the content below.

::

    APT::Periodic::Enable "1";
    APT::Periodic::Update-Package-Lists "1";
    APT::Periodic::AutocleanInterval "7";
    APT::Periodic::Unattended-Upgrade "1";
    Unattended-Upgrade::Mail "**YOUR_EMAIL_HERE**";

    // Automatically upgrade packages from these (origin, archive) pairs
    Unattended-Upgrade::Allowed-Origins {
        "${distro_id} stable";
        "${distro_id} ${distro_codename}-security";
    };

    // Automatically reboot *WITHOUT CONFIRMATION* if a
     // the file /var/run/reboot-required is found after the upgrade
     Unattended-Upgrade::Automatic-Reboot "false";

So lets explain the above. As you can see we enable periodic updates,
enable update package lists (triggers an apt-get update), enable
autoclean to clean out the local package repository every 7 days, enable
the actual unattended update and finally you can set your email address
so that you will get an email when an update has happened.
Next up we configure the origins to update from, as you can see we've
only enabled security and as a very final step we make sure we've
disabled automatic reboots - you probably don't want your server
randomly rebooting to update the running kernel, this means you will
have to reboot when convenient after a kernel update.

Your unattended update will happen every day, triggered by
**cron.daily**. Next time your cron.daily has triggered, look inside
**/var/log/unattended-upgrades/unattended-upgrades.log**, you should see
something like this

::

    2012-01-28 06:54:04,730 INFO Initial blacklisted packages:
    2012-01-28 06:54:04,730 INFO Starting unattended upgrades script
    2012-01-28 06:54:04,731 INFO Allowed origins are: ["('Debian','squeeze-security')"]
    2012-01-28 06:54:05,952 INFO No packages found that can be upgraded unattended

If you installed apticron in the above step and want to configure it and
use it then continue reading, if not then congratulations everything is
done.

Configuring apticron
--------------------

Open up **/etc/apticron/apticron.conf**, all you need to change is the
**EMAIL** option.

::

    EMAIL="**YOUR_EMAIL_HERE**"

Now each day you will receive an email when **cron.daily** runs with all
available package updates.
