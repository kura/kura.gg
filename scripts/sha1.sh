#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find $1 -type f | grep -v -e md5 -e sha1 | while read f
do
  sha1sum $f > $f.sha1.bak
  cat $f.sha1.bak | sed -r 's/^([a-z0-9]*) .*\/(.*)$/\1 \2/g' > $f.sha1
  rm $f.sha1.bak
done
