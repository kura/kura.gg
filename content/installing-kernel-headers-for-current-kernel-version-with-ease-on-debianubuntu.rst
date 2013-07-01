Installing kernel headers for current kernel version with ease on Debian/Ubuntu
###############################################################################
:date: 2011-09-15 13:30
:author: kura
:category: debian, howto, ubuntu
:tags: apt, apt-get, debian, headers, kernel, ubuntu
:slug: installing-kernel-headers-for-current-kernel-version-with-ease-on-debianubuntu

This is a simple one but I found out that there are people out there
that don't know about it, so here we go.

    apt-get install linux-headers-$(uname -r)

This will install kernel headers for your current active kernel on
Debian/Ubuntu.
