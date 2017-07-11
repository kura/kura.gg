#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

for f in `find $1 -type f | egrep '\.(asc|c|css|html|ico|js|map|md5|sha1|txt|woff|woff2|xml)'`
do
  md5sum $f > $f.md5
done
