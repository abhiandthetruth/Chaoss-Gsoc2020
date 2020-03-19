#!/bin/bash

url="http://localhost:9200/"
index=$1
if [ "$1" == "-s" ]
then
	url="https://admin:admin@localhost:9200/"
	index=$2
fi
elasticdump --input=$url$index --output=./${index}_mapping.json --type=mapping
elasticdump --input=$url$index --output=./${index}_data.json --type=data

