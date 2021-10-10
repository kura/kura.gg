#!/bin/sh
CUR=$PWD
REPO=$HOME/workspace/resume-template

cd $REPO
make build
cd $CUR
cp -R $REPO/_site/* cv/
