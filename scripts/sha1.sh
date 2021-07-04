#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

for f in `find $1 -type f | grep -v -e md5 -e sha1`
do
  sha1sum $f > $f.sha1
done
