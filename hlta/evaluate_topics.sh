#!/bin/bash

#usage: topics, sparse, target_file

echo "Topic coherence:" >> "$3"
java -Xms2G -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence "$1" "$2" >> "$3"
echo "Topic compactness:" >> "$3"
java -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCompactness "$1" GoogleNews-vectors-negative300.bin >> "$3"

