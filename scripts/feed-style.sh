#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

find "$1/feeds" -type f -name "*rss.xml" | while read f
do
  sed -i '2 i <?xml-stylesheet href="/theme/xsl/rss.xsl" type="text/xsl"?>' "$f"
done

find "$1/feeds" -type f -name "*atom.xml" | while read f
do
  sed -i '2 i <?xml-stylesheet href="/theme/xsl/atom.xsl" type="text/xsl"?>' "$f"
done
