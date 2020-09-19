#!/bin/bash

dataset="/home/juan/Documents/datasets/thesis/"
root="/home/juan/Documents/datasets/thesis_split/"
n=3400
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

