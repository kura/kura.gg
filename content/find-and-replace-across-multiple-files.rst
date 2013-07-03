Find and replace across multiple files
######################################
:date: 2010-08-13 19:19
:author: kura
:category: tutorials
:tags: find, sed, xargs
:slug: find-and-replace-across-multiple-files

I needed to quickly modify 500 hundred XML files, each was about 10MB in
size, thankfully Linux makes that pretty fast and very easy.

    find . -name "\*.xml" -print \| xargs sed -i 's/FROM/TO/g'

A semi "real world" example:

    find . -name "\*.xml" -print \| xargs sed -i 's/foo/bar/g'
