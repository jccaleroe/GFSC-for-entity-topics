#!/bin/bash
if [ $# -lt 2 ]; then
  echo 1>&2 "$0: not enough arguments"
  exit 2
elif [ $# -gt 4 ]; then
  echo 1>&2 "$0: too many arguments"
  exit 2
fi 

java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.text.Convert "$3"/myData "$1" $4 1
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar clustering.StepwiseEMHLTA "$3"/myData.sparse.txt 50 3 0.01 3 "$3"/myModel 15 30 500 10 100 1 10000 "$2" 3
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.ExtractTopicTree "$3"/topicTree "$3"/myModel.bif "$3"/myData.sparse.txt
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.Doc2VecAssignment "$3"/myModel.bif "$3"/myData.sparse.txt "$3"/myAssignment
echo "Topic coherence:" > "$3"/evaluation
java -Xms2G -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence "$3"/topicTree.nodes.json "$3"/myData.sparse.txt >> "$3"/evaluation
echo "Topic compactness:" >> "$3"/evaluation
java -Xmx7G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCompactness "$3"/topicTree.nodes.json GoogleNews-vectors-negative300.bin >> "$3"/evaluation
