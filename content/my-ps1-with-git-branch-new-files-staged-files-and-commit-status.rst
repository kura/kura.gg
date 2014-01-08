My $PS1 with git branch, new files, staged files and commit status
##################################################################
:date: 2013-08-18 17:25
:author: kura
:category: coding
:tags: bash, dash, ps1, git
:slug: my-ps1-with-git-branch-new-files-staged-files-and-commit-status

I love my prompt, always have and always will. I spend so much of my life
in a terminal, usually with half a dozen mini terminals open in each tab.
As such I like to tweak it and get it as perfect as possible for my life, needs
and even mood.

In the past I've had quite a large PS1 that covers multiple lines and gives a
lot of information, after having that PS1 in one form or another for some time
I decided it was time for a change, to a smaller PS1 that takes up a lot less
space.

So here it is, the first image is my standard PS1 when in a git repository,
the red @ means a file hasn't been added to Git, a blue @ means a tracked file
has been modified but not stage and finally a green @ means a file is staged
but still needs to be committed.

.. image:: https://kura.io/static/images/new-ps1.png
    :alt: PS1 while in a git repository

When I have run `sudo -s` my PS1 changes to alert me to the fact I have
superuser privileges.

.. image:: https://kura.io/static/images/new-ps1-root.png
    :alt: PS1 when I have scary privileges

You can find the source code used to power this PS1 below which is stored in a
Gist on GitHub.

[gist:id=6262468]
