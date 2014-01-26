#!/usr/bin/env bash
for f in `find output/theme/css/ -type f`
do
  filename=$(basename $f)
  cssmin < $f > output/theme/css/${filename%.*}.min.css
  rm $f
done
