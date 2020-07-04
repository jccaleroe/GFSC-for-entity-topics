#!/bin/bash

#First parameter, dataset folder, for the moment must be in this folder and with sub folders specified in the list
#prefixes with the structure folder_prefix
#Second parameter, number of cores to be used
#You can modify this script and hlta.sh and hlta-es.sh scripts to specify more parameters

if [ $# -lt 3 ]; then
  echo 1>&2 "$0: not enough arguments"
  exit 2
elif [ $# -gt 3 ]; then
  echo 1>&2 "$0: too many arguments"
  exit 2
fi

#Modify according to your dataset
prefixes=("propn" "verb" "org" "loc" "per" "adj" "noun")

#Modify according how important is each hierarchy for you

#for the silla vacia
words_per_type=(600 500 400 400 400 300 200)

#for the abstracts
#words_per_type=(600 500 200 200 200 300 200)

for i in ${prefixes[@]}; do
  mkdir -p topic_models/"$2"/$i
  rm -rf topic_models/"$2"/$i/*
done

for i in ${!prefixes[@]}; do
  sh hlta-es.sh "$1"/${prefixes[$i]} "$3" topic_models/"$2"/${prefixes[$i]} ${words_per_type[$i]}
done

mkdir -p ../fusion/"$2"/evaluation
touch ../fusion/"$2"/evaluation/myData.sparse.txt

for i in ${prefixes[@]}; do
  mkdir -p ../fusion/"$2"/$i
  rm -rf ../fusion/"$2"/$i/*
  cp topic_models/"$2"/$i/myAssignment.topics.json ../fusion/"$2"/$i/
  cp topic_models/"$2"/$i/myData.dict.csv ../fusion/"$2"/$i/
  cp topic_models/"$2"/$i/myData.files.txt ../fusion/"$2"/$i/
  cp topic_models/"$2"/$i/topicTree.nodes.json ../fusion/"$2"/$i/
  cp topic_models/"$2"/$i/myModel.bif ../fusion/"$2"/$i/
  cat topic_models/"$2"/$i/myData.sparse.txt >> ../fusion/"$2"/evaluation/myData.sparse.txt
done

sort -u ../fusion/"$2"/evaluation/myData.sparse.txt | sort -g -o ../fusion/"$2"/evaluation/myData.sparse.txt
