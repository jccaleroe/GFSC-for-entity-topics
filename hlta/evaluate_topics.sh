#!/bin/bash

#usage: topics, sparse, target_file
{
  "Topic coherence:"
  java -Xms2G -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence "$1" "$2"
  "Topic compactness:"
} >> "$3"
mv "$1" "$1".bak
sed -r 's/xyz/_/g' "$1".bak >"$1"
java -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCompactness "$1" GoogleNews-vectors-negative300.bin >>"$3"
mv "$1".bak "$1"
