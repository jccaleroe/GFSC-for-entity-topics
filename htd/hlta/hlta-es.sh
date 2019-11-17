if [ $# -lt 2 ]; then
  echo 1>&2 "$0: not enough arguments"
  exit 2
elif [ $# -gt 2 ]; then
  echo 1>&2 "$0: too many arguments"
  exit 2
fi 

java -Xms2G -Xmx30G -cp HLTA-es.jar:HLTA-deps.jar tm.text.Convert myData "$1" 1000 1
java -Xms2G -Xmx30G -cp HLTA-es.jar:HLTA-deps.jar clustering.StepwiseEMHLTA myData.sparse.txt 50 3 0.01 3 myModel 15 30 500 10 100 1 10000 "$2" 3
java -Xms2G -Xmx30G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.ExtractTopicTree topicTree myModel.bif myData.sparse.txt
java -Xms2G -Xmx30G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.Doc2VecAssignment myModel.bif myData.sparse.txt myAssignment
java -Xms2G -Xmx30G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence topicTree.nodes.json myData.sparse.txt