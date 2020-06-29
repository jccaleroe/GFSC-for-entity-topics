#!/bin/bash

#First parameter, dataset folder, for the moment must be in this folder and with sub folders specified in the list
#prefixes with the structure folder_prefix
#Second parameter, number of cores to be used
#You can modify this script and hlta.sh and hlta-es.sh scripts to specify more parameters

if [ $# -lt 2 ]; then
  echo 1>&2 "$0: not enough arguments"
  exit 2
elif [ $# -gt 2 ]; then
  echo 1>&2 "$0: too many arguments"
  exit 2
fi

#Modify according to your dataset
prefixes=("propn" "verb" "org" "loc" "per" "adj" "noun")

#Modify according how important is each hierarchy for you

#for the silla vacia
#words_per_type = (400 400 300 300 300 200 200)

#for the abstracts
words_per_type=(500 500 200 200 200 300 200)

for i in ${prefixes[@]}; do
  mkdir -p topic_models/"$1"/"$1"_$i
  rm -rf topic_models/"$1"/"$1"_$i/*
done

for i in ${!prefixes[@]}; do
  sh hlta-es.sh "$1"/"$1"_${prefixes[$i]} "$2" topic_models/"$1"/"$1"_${prefixes[$i]} ${words_per_type[$i]}
done

mkdir -p ../fusion/"$1"/evaluation
touch ../fusion/"$1"/evaluation/myData.sparse.txt

for i in ${prefixes[@]}; do
  mkdir -p ../fusion/"$1"/"$1"_$i
  rm -rf ../fusion/"$1"/"$1"_$i/*
  cp topic_models/"$1"/"$1"_$i/myAssignment.topics.json ../fusion/"$1"/"$1"_$i/
  cp topic_models/"$1"/"$1"_$i/myData.dict.csv ../fusion/"$1"/"$1"_$i/
  cp topic_models/"$1"/"$1"_$i/myData.files.txt ../fusion/"$1"/"$1"_$i/
  cp topic_models/"$1"/"$1"_$i/topicTree.nodes.json ../fusion/"$1"/"$1"_$i/
  cat topic_models/"$1"/"$1"_$i/myData.sparse.txt >> ../fusion/"$1"/evaluation/myData.sparse.txt
done

sort -u ../fusion/"$1"/evaluation/myData.sparse.txt | sort -g -o ../fusion/"$1"/evaluation/myData.sparse.txt
