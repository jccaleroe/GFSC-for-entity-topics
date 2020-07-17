#!/bin/bash
if [ $# -lt 6 ]; then
  echo 1>&2 "Usage: source_dir target_dir words_num concatenation max_island cores"
  exit 2
elif [ $# -gt 6 ]; then
  echo 1>&2 "Usage: source_dir target_dir words_num concatenation max_island cores"
  exit 2
fi 

java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.text.Convert "$2"/myData "$1" $3 $4
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar clustering.StepwiseEMHLTA "$2"/myData.sparse.txt 50 3 0.01 3 "$2"/myModel $5 30 500 10 100 1 10000 $6 3
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.ExtractTopicTree "$2"/topicTree "$2"/myModel.bif "$2"/myData.sparse.txt
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.Doc2VecAssignment "$2"/myModel.bif "$2"/myData.sparse.txt "$2"/myAssignment
echo "Topic coherence:" > "$2"/evaluation
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence "$2"/topicTree.nodes.json "$2"/myData.sparse.txt >> "$2"/evaluation
echo "Topic compactness:" >> "$2"/evaluation
java -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCompactness "$2"/topicTree.nodes.json GoogleNews-vectors-negative300.bin >> "$2"/evaluation
