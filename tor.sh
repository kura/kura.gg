#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find $1 -iname '*.gz' -delete
find $1 -iname '*.br' -delete

find $1 -iname '*.html' | xargs sed -i 's|https://kura.io|http://omgkuraio276g5wo.onion|g'
find $1 -iname '*.js' | xargs sed -i 's|https://kura.io|http://omgkuraio276g5wo.onion|g'
find $1 -iname '*.css' | xargs sed -i 's|https://kura.io|http://omgkuraio276g5wo.onion|g'
find $1 -iname '*.map' | xargs sed -i 's|https://kura.io|http://omgkuraio276g5wo.onion|g'
find $1 -iname '*.xml' | xargs sed -i 's|https://kura.io|http://omgkuraio276g5wo.onion|g'
