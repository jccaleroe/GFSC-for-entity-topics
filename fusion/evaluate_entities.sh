#!/bin/bash

#the dataset folder mus have sub folders specified in the prefixes list
#You can modify this script and hlta-es.sh scripts to specify more parameters

if [ $# -lt 2 ]; then
  echo 1>&2 "usage: source_dir use_spanish"
  exit 2
elif [ $# -gt 2 ]; then
  echo 1>&2 "usage: source_dir use_spanish"
  exit 2
fi

#English
entities=("PERSON" "ORG" "LOC" "OBJ" "EVENT" "VERB" "ADJ" "NOUN")
if [ "$2" = true ] ; then
  entities=("VERB" "ORG" "LOC" "PER" "NOUN" "ADJ")
fi

for i in "${entities[@]}"; do
  echo "Evaluating" "$i"
  python inter_coherence.py "$1"/"$i"/topicTree.nodes.json "$1"/"$i"/myData.sparse.txt "$1"/"$i"/inter_coherence --all_metrics
done
