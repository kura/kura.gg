#!/usr/bin/python3
import pathlib
import sys


output_dir=sys.argv[1]

with open(pathlib.Path(output_dir).joinpath("theme/css/eevee.min.css")) as f:
    css = f.read()

with open(pathlib.Path(output_dir).joinpath("theme/js/eevee.min.js")) as f:
    js = f.read()


def replace(path):
    with open(path) as f:
        c = f.read()
    out = c.replace("CSS_REPLACEMENT_TOKEN", css).replace("JS_REPLACEMENT_TOKEN", js)
    with open(path, "w") as f:
        f.write(out)


path = pathlib.Path(output_dir)
for p in sorted(path.rglob("*.html")):
    print(p)
    replace(p)
