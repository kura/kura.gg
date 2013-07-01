Finding files over a set size with find & awk
#############################################
:date: 2010-03-17 11:19
:author: kura
:category: debian, howto, ubuntu, Uncategorized
:tags: awk, egrep, find, linux, ls, wc
:slug: finding-files-over-a-set-size-with-find-and-awk

This is a really great simple way to find files on the filesystem that
are over 200k in size.

    find /path/to/directory/ -type f -size +200k -exec ls -lh {} ; \| awk '{ print $NF ": " $5 }'

You can use the output of this to either store in a file, or pipe to wc
for a count of lines

    find /path/to/directory/ -type f -size +200k -exec ls -lh {} ; \| awk '{ print $NF ": " $5 }' \| wc -l

You can also use egrep before wc to look for specific filetypes

    find /path/to/directory/ -type f -size +200k -exec ls -lh {} ; \| awk '{ print $NF ": " $5 }' \| egrep '(jpg\|bmp\|gif\|tiff\|jpeg)' \| wc -l
