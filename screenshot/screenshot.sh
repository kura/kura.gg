#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

for page in `find $1 -name "*.html" | grep -v '/tor/' | grep -v '/donate/' | grep -v '/apt.kura.io/' | grep -v '/curriculum-vitae/' | grep -v '/category/' | grep -v '/categories/' | grep -v '/tag/' | grep -v '/tags/' | grep -v '/authors/' | grep -v '/archives/'`
do
    output=`echo $page | sed -e 's/\.html/\.png/g'`
    url=`echo "https://kura.gg/${page}" | sed -e "s|$1||g"`
    echo "${url} -> ${output}"
    phantomjs screenshot/screenshot.js $url $output-orig.png
    convert $output-orig.png -resize 100% $output-orig.png
    pngquant $output-orig.png -o $output
    rm $output-orig.png
done
