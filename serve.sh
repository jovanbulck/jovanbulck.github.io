#!/bin/bash
./parse_refs.py
bundle exec jekyll serve -l --config "_config.yml,_config.dev.yml"
