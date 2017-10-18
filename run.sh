#!/bin/bash
export AMAZON_SPIDER_ACCESSTOKEN=""
scrapy crawl amazon -t 'csv' -o 'output.csv' && ./dbx.py && rm output.csv