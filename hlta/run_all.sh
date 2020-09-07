#!/bin/bash

#the dataset folder mus have sub folders specified in the list prefixes
#You can modify this script and hlta-es.sh scripts to specify more parameters

if [ $# -lt 2 ]; then
  echo 1>&2 "usage: source_dir target_dir"
  exit 2
elif [ $# -gt 2 ]; then
  echo 1>&2 "usage: source_dir target_dir"
  exit 2
fi

#profiles
#declare -A map=(["VERB"]=1000 ["ORG"]=800 ["LOC"]=800 ["PER"]=800 ["NOUN"]=600 ["ADJ"]=400)

#Organisms
declare -A map=(["PERSON"]=600 ["ORG"]=800 ["LOC"]=2000 ["OBJ"]=800 ["EVENT"]=1400 ["VERB"]=1000 ["ADJ"]=400 ["NOUN"]=3000)

for key in "${!map[@]}"; do
  mkdir -p topic_models/"$2"/"$key"
  rm -rf topic_models/"$2"/"$key"/*
  sh hlta-es.sh "$1"/"$key" topic_models/"$2"/"$key" "${map[$key]}" 0 4 4
done

rm -rf ../fusion/"$2"/*
mkdir -p ../fusion/"$2"/evaluation
touch ../fusion/"$2"/myData.sparse.txt

for i in "${!map[@]}"; do
  mkdir -p ../fusion/"$2"/"$i"
  cp topic_models/"$2"/"$i"/myAssignment.topics.json ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/myData.dict.csv ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/myData.files.txt ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/topicTree.nodes.json ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/myModel.bif ../fusion/"$2"/"$i"/
  cat topic_models/"$2"/"$i"/myData.sparse.txt >>../fusion/"$2"/myData.sparse.txt
done

sort -u ../fusion/"$2"/myData.sparse.txt | sort -g -o ../fusion/"$2"/myData.sparse.txt

