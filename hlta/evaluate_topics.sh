#!/bin/bash

#usage: topics, sparse, target_file

echo "Topic coherence:" >> "$3"
java -Xms2G -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence "$1" "$2" >> "$3"
echo "Topic compactness:" >> "$3"
sed -r 's/xyz/_/g' "$1" > "$1".bak
java -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCompactness "$1".bak GoogleNews-vectors-negative300.bin >> "$3"
rm "$1".bak

