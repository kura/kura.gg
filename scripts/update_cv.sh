#!/bin/sh
CUR=$PWD
REPO=$HOME/workspace/resume-template

cd $REPO
make build
cd $CUR
cp -R $REPO/_site/* cv/
wkhtmltopdf --enable-local-file-access cv/index.html cv/kura_uncomp.pdf
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=cv/kura.pdf cv/kura_uncomp.pdf
rm cv/kura_uncomp.pdf
