#!/usr/bin/env bash
docker run --rm -v $(pwd):/runtime/app aciobanu/scrapy $*
