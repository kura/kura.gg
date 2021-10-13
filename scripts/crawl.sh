#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

for page in `find $1 -type f`
do
    url=`echo "https://kura.gg${page}" | sed -e "s|$1||g"`
    echo $url
    curl -s $url -o /dev/null
done
