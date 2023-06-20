#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find $1 -type f | egrep '\.(asc|c|css|html|ico|js|map|md5|sha1|svg|txt|woff|woff2|xml)' | while read f
do
  gzip -9 < $f > $f.gz
  bro --quality 11 --input $f --output $f.br
done
