#!/usr/bin/python3
import os
import pathlib
import sys


output_dir=sys.argv[1]

with open(pathlib.Path().joinpath(output_dir, "theme/css/eevee.min.css")) as f:
    css = f.read()

with open(pathlib.Path().joinpath(output_dir, "theme/js/eevee.min.js")) as f:
    js = f.read()


def replace(path):
    with open(path) as f:
        c = f.read()
    out = c.replace("CSS_REPLACEMENT_TOKEN", css).replace("JS_REPLACEMENT_TOKEN", js)
    with open(path, "w") as f:
        f.write(out)


for html_file in sorted(os.listdir(output_dir)):
    if ".html" in html_file:
        print(html_file)
        path = pathlib.Path().joinpath(output_dir, html_file)
        replace(path)

for seqs in sorted(os.walk(output_dir)):
    bp, stuff, files = seqs
    if stuff != []:
        continue
    if "index.html" in files:
        path = pathlib.Path().joinpath(bp, files[0])
        print(path)
        replace(path)
