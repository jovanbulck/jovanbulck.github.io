#!/bin/bash
./parse_refs.py
./fetch_titles.py
./gen_timeline.py
./gen_previews.py

for file in files/*.svg; do
    png_file="${file%.svg}.png"
    if [ ! -f "$png_file" ]; then
        echo .. generating $png_file
        inkscape "$file" --export-filename="$png_file" --export-dpi=300
    fi
done

bundle exec jekyll serve -l -H localhost
