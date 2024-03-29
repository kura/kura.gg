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
    sudo shot-scraper $url -o $output-orig.png --width 1920 --height 1080
    sudo convert $output-orig.png -resize 100% $output-orig.png
    pngquant $output-orig.png -o $output
    rm $output-orig.png
}

find $1 -name "*.html" | grep -v '/tor/' | grep -v '/donate/' | grep -v '/apt.kura.io/' | grep -v '/curriculum-vitae/' | grep -v '/category/' | grep -v '/categories/' | grep -v '/tag/' | grep -v '/tags/' | grep -v '/authors/' | grep -v '/archives/' | grep -v '/500.html' | grep -v '/404.html' | while read page
do
    output=$(echo $page | sed -e 's/\.html/\.png/g')
    url=$(echo "http://localhost:8000/${page}" | sed -e "s|$1||g")
    screenshot $url $output
done

# sleep 2
# echo "waiting for screenshot jobs to complete"
# wait < <(jobs -p)
