#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find $1 -type f | while read page
do
    url=$(echo "https://kura.gg/${page}" | sed -e "s|$1||g")
    echo $url
    curl -s $url -o /dev/null &
done

sleep 2
echo "waiting for crawl jobs to complete"
wait < <(jobs -p)
