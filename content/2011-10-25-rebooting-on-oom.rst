Rebooting on OOM
################
:date: 2011-10-25 10:26
:author: kura
:category: tutorials
:tags: kernel panic, oom, reboot
:slug: rebooting-on-oom

.. contents::
    :backlinks: none

***I would generally not advise using this unless you have skill at
debugging why OOM has spawned and also debugging kernel panics after
they happen, from logs.***

It is possible to configure your kernel to panic when OOM is spawned,
which in itself is not useful but, coupled with a kernel option for
auto-rebooting a system when the kernel panics it can be a very useful
tool.

Think before implementing this and use at your own risk, I take zero
responsibility for you using this.

.. code-block:: bash

    sudo sysctl vm.panic_on_oom=1
    sudo sysctl kernel.panic=X # X is the amount of seconds to wait before rebooting

***DO NOT FORGET TO CHANGE X***

This will inject the changes in to a system that is currently running
but will be forgotten on reboot so use the lines below to save
permanently.

.. code-block:: bash

    sudo echo "vm.panic_on_oom=1" >> /etc/sysctl.conf
    sudo echo "kernel.panic=X" >> /etc/sysctl.conf

***X is the amount of seconds to wait before rebooting. DO NOT FORGET TO
CHANGE X***

Testing
-------

You can test the changes with a simple C program. **Please note if you
run this you do so at your own risk**.

.. code-block:: c

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #define MB 10485760

    int main(int argc, char *argv[]) {
        void *b = NULL;
        int c = 0;
        while(1) {
            b = (void *) malloc(MB);
            if (!b) {
                break;
            }
            memset(b, 10, MB);
            printf("Allocating %d MB\n", (++c * 10));
        }
        exit(0);
    }

Compilation
-----------

You can download the `source here </files/oom.c>`_.

To compile run the command below

.. code-block:: bash

    gcc -O2 oom.c -o oom

Or download a `pre-compiled version here </files/oom>`_.

Usage
-----

And simply run it using

.. code-block:: bash

    ./oom

After a short period of time allocating and using 10MB chunks of memory
your system should run out and restart.
