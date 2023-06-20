#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find $1 -type f | grep -v -e md5 -e sha1 | while read f
do
  md5sum $f > $f.md5.bak
  cat $f.md5.bak | sed -r 's/^([a-z0-9]*) .*\/(.*)$/\1 \2/g' > $f.md5
  rm $f.md5.bak
done
