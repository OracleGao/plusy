#!/usr/bin/env bash
docker run -v $(pwd):/runtime/app aciobanu/scrapy $*
