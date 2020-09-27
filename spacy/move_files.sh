#!/bin/bash

if [ $# -lt 3 ]; then
  echo 1>&2 "usage: source_dir target_dir number_per_folder"
  exit 2
elif [ $# -gt 3 ]; then
  echo 1>&2 "usage: source_dir target_dir number_per_folder"
  exit 2
fi

folder=1
cnt=0
target="$2""$folder"/
mkdir -p "$target"

for filename in "$1"*; do
  if [ $cnt -ge "$3" ]; then
    ((folder+=1))
    cnt=0
    target="$2""$folder"/
    mkdir -p "$target"
  fi
  mv "$filename" "$target"
  ((cnt+=1))
done
