less is more
############
:date: 2010-03-01 21:30
:author: kura
:category: tutorials
:tags: less, linux, unix
:slug: less-is-more

To my surprise I have found that there are still people out there who
use *"more"*, this has shocked me.

So this is a very, very short blog post to tell those who visit that
**less is more and more is less**.

What?
-----

less is a command that comes as standard in almost all Linux distros
now, and unlike more it actually has the ability to do backwards and
forwards scrolling with Page Up, Page Down, arrow keys and spacebar.
It's a fantastic little command!

    less FILE

Very simple to use and an all round great tool. The best thing about
less is it doesn't need to read the whole file in one go, it reads in
chunks. Opening a 100MB log file is simple with less!

Useful options
--------------

-  **-g** - Highlights just the current match of any searched string,
-  **-I** - Case-insensitive searches,
-  **-M** - Show a more detailed prompt, including file position,
-  **-N** - Show line numbers.
-  **+F** - Follow (like tail -f)

Useful key bindings
-------------------

-  **/** - Search e.g. /test
-  **n** - Goto next search match
-  **N** (Shift + n) - Goto previous search match
-  **^** - Goto start of the file
-  **$** - Goto end of the file
-  **Spacebar** - Next page
-  **b** - Previous page

