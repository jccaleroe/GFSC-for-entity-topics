#!/bin/bash

delay_download=1
folder_content="thesis/"

if [ ! -d "$folder_content" ]; then
    mkdir -p "$folder_content"
fi

wget http://bdigital.unal.edu.co/cgi/exportview/types/thesis/Ids/thesis.txt

< thesis.txt xargs -n1 -I{} sh -c "sleep $delay_download; curl -s -L http://bdigital.unal.edu.co/{}/ | grep -o -m 1 'http://bdigital.unal.edu.co/{}/.*\.pdf' | xargs wget -O $folder_content{}.pdf"
