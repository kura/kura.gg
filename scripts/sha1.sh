#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

for f in `find $1 -type f`
do
  sha1sum $f > $f.sha1
done
