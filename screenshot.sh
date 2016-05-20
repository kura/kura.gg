for page in `find output/ -name "*.html" | grep -v '/c/' | grep -v '/t/' | egrep -v '[0-9][0-9]\/index\.html'`
do
    output=`echo $page | sed -e 's/\.html/\.png/g'`
    url=`echo "https://kura.io/${page}" | sed -e 's/output\///g'`
    echo "${url} -> ${output}"
    phantomjs screenshot.js $url $output
done
