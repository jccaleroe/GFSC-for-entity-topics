#!/bin/bash

mkdir -p profiles
curl -s 'https://lasillavacia.com/quienesquien/personas/nodesjsonv2' > all_profiles.json
cat all_profiles.json | jq '.nodes[] | .name, .occupation' | xargs -n2 sh -c 'echo $0, $1. > profiles/$0'
cat all_profiles.json | jq '.nodes[] | .name, .slug' | xargs -n2 sh -c 'sleep 0.1; curl -s "https://lasillavacia.com/"$1 | xmllint --html --xpath "/html/body/div[3]/div[5]/article/div/div/div[2]/div/div/p" - 2>/dev/null | sed -e "s/<[^>]*>/ /g" | sed "s/[-_]/ /g" >> profiles/$0'
find profiles/ -type f | sed -r "p;s/ |'//g" | xargs -d '\n' -n2 sh -c 'mv "$0" "$1".txt'
