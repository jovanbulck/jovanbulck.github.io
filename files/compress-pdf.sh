#!/bin/bash
set -x

target=`basename $1 .pdf`-compressed.pdf
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$target $1
mv $target $1
