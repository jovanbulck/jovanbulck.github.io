#!/bin/bash
./parse_refs.py
bundle exec jekyll build
bundle exec htmlproofer ./_site
