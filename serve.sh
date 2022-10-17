#!/bin/bash
./parse_refs.py
bundle exec jekyll liveserve --config "_config.yml,_config.dev.yml"
