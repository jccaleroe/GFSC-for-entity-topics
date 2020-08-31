#!/bin/bash

dataset="/home/juan/Downloads/new_life/"
root="/home/juan/Videos/organisms/"
n=74011
folder=1
cnt=0

target="$root""$folder"/
mkdir -p $target

for filename in "$dataset"*; do
  if [ $cnt -ge $n ]; then
    ((folder+=1))
    cnt=0
    target="$root""$folder"/
    mkdir -p $target
  fi
  mv "$filename" "$target"
  ((cnt+=1))
done
