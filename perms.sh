#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find $1 -type f | xargs chmod 0644
find $1 -type d | xargs chmod 0755
