#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

for f in `find $1 -type f -iname "*.png"`
do
  mv $f $f.orig
  pngquant $f.orig -o $f
  rm $f.orig
done
