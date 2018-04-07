#!/usr/bin/env bash
cd ${0%/*}

if [ "$1" == "" ]; then
  echo "Usage $0 <spider>"
  exit 1
fi

mkdir -p output
rm -rf output/$1.json

./scrapy.sh crawl -o output/$1.json $1 2>&1

