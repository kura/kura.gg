#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 OUTPUTDIR"
    exit 1
fi

cat scripts/eevee $1/theme/css/eevee.min.css > $1/theme/css/eevee.min.css.bak
rm $1/theme/css/*.css
mv $1/theme/css/eevee.min.css{.bak,}

cat scripts/eevee $1/theme/js/eevee.min.js > $1/theme/js/eevee.min.js.bak
rm $1/theme/js/*.js
mv $1/theme/js/eevee.min.js{.bak,}
