#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

# find $1 -type f -iname '*.html' | xargs sed -i 's/\¶/\&#xb6;/g'
find $1 -type f -iname '*.html' | xargs sed -i 's/\※/\&#x203B;/g'
