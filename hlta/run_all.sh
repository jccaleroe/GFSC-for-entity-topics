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

#Modify according to your dataset
prefixes=("verb" "org" "loc" "per" "adj")

#Modify according on how many words to use is each hierarchy

#for the profiles
words_per_type=(1000 800 800 800 400)

#for the abstracts
#words_per_type=(600 500 200 200 200 300 200)

for i in "${prefixes[@]}"; do
  mkdir -p topic_models/"$2"/"$i"
  rm -rf topic_models/"$2"/"$i"/*
done

for i in "${!prefixes[@]}"; do
  sh hlta-es.sh "$1"/"${prefixes[$i]}" topic_models/"$2"/"${prefixes[$i]}" "${words_per_type[$i]}" 0 4 4
done

rm -rf ../fusion/"$2"/*
mkdir -p ../fusion/"$2"/evaluation
touch ../fusion/"$2"/myData.sparse.txt

for i in "${prefixes[@]}"; do
  mkdir -p ../fusion/"$2"/"$i"
  cp topic_models/"$2"/"$i"/myAssignment.topics.json ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/myData.dict.csv ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/myData.files.txt ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/topicTree.nodes.json ../fusion/"$2"/"$i"/
  cp topic_models/"$2"/"$i"/myModel.bif ../fusion/"$2"/"$i"/
  cat topic_models/"$2"/"$i"/myData.sparse.txt >> ../fusion/"$2"/myData.sparse.txt
done

sort -u ../fusion/"$2"/myData.sparse.txt | sort -g -o ../fusion/"$2"/myData.sparse.txt
