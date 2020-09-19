#!/bin/bash

delay_download=0.1
folder_content="content/"

if [ ! -d "$folder_content" ]; then
    mkdir -p "$folder_content"
fi

wget http://bdigital.unal.edu.co/cgi/exportview/types/thesis/Ids/thesis.txt > thesis.txt
cat thesis.txt | xargs -I{} sh -c 'sleep '$delay_download'; curl -s -L http://bdigital.unal.edu.co/cgi/export/eprint/{}/JSON/repositorioun-eprint-{}.js | jq ".title,.abstract" | sed "s/\"//g" | sed -r "s/^ *|\[|\]|null//" | sed -r "s/\\\r|\\\n/ /g" | sed -r "s/ ?\/? ?abstract.*//I" | sed -r "1 s/ ?\/.*//" | iconv -f UTF-8 -t ASCII//TRANSLIT > '"$folder_content"'{}.txt'
sync
