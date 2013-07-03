HOWTO: SSH config on Debian/Ubuntu
##################################
:date: 2010-02-18 21:03
:author: kura
:category: tutorials
:tags: debian, howto, ssh, ssh_config, ubuntu
:slug: howto-ssh-config-on-debian-ubuntu

Today I *finally* got round to setting up my local user ssh config on my
new work laptop and figured I'd do a quick write up on it and it's uses.

You can create a configuration file in your home directory that will
override the options set in your machine-wide config.

Your configuration files
------------------------

Your local config can be found/created in:

    ~/.ssh/config

And your machine-wide configuration is in:

    /etc/ssh/ssh\_config

Rather than editing my ssh config across my whole machine I'm doing it
for my local user specifically.

Reading the man page for ssh\_config will give you a full list of
available options, below I will outline several that I use and find very
useful.

Your host definitions
---------------------

First things first, we need to define a host.

    Host host.domain.com

Each host you add to your config will need to have a host definition

    Host host.domain.com

    ...

    Host host2.domain.com

    ...

You can also create a wildcard host, hosts will actually build together
unless overwritten, so if you set a variable within the wildcard host it
will be set on all other defined hosts, unless the option is respecified
on that host.

You can set up a wildcard host with this option:

    Hostname \*

    ...

Configuration options
---------------------

I use several options across all my hosts

    Compression yes

Setting this to yes will enable SSH compression. See setting below for
more information.

    CompressionLevel 9

This is used to set compression on SSH, the higher the level (1-9) the
higher the compression rate, this also means less bandwidth is needed
but will require more processing to actually compress the request. I
generally set this in my wildcard host and leave it set.

    HostName 192.168.1.2

This is a great little option, it means you can set an IP address to
connect to within a host definition, this basically means no more need
for /etc/hosts specifically for SSH.

    KeepAlive yes

Setting this will enable keep alive packets to be sent to the host,
making it easier to continue working after network disconnect.

    TCPKeepAlive yes

This option is like the one above, except it only sends TCP keep alive
packets.

There are many, many more settings but these are the ones I find useful.

Configuration example
---------------------

    Host host1
        HostName 192.168.1.1

    Host host2
        HostName 192.168.1.2

    Host host3
        HostName host3.example.com

    Host \*
        Compression yes
        CompressionLevel 9
        KeepAlive yes

Why use it?
-----------

The beauty of this config means that you are able to type ssh, press
your Tab key and a whole list of your hosts will be displayed, using the
name set in the host definition, just like when you type commands, this
also means you could type "ssh h" with the above config file and it will
display host1, host2 and host3 for you to chose from.
