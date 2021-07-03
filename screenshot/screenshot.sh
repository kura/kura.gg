#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

screenshot() {
    url=$1
    output=$2
    echo "${url} -> ${output}"
    phantomjs screenshot/screenshot.js $url $output-orig.png
    convert $output-orig.png -resize 100% $output-orig.png
    pngquant $output-orig.png -o $output
    rm $output-orig.png
}

for page in `find $1 -name "*.html" | grep -v '/tor/' | grep -v '/donate/' | grep -v '/apt.kura.io/' | grep -v '/curriculum-vitae/' | grep -v '/category/' | grep -v '/categories/' | grep -v '/tag/' | grep -v '/tags/' | grep -v '/authors/' | grep -v '/archives/' | grep -v '/500.html' | grep -v '/404.html'`
do
    output=`echo $page | sed -e 's/\.html/\.png/g'`
    url=`echo "https://kura.gg/${page}" | sed -e "s|$1||g"`
    screenshot $url $output &
done

sleep 2
echo "waiting for screenshot jobs to complete"
wait < <(jobs -p)
