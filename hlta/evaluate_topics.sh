#!/bin/bash

if [ $# -lt 3 ]; then
  echo 1>&2 "usage: topics, sparse, target_file"
  exit 2
elif [ $# -gt 3 ]; then
  echo 1>&2 "usage: topics, sparse, target_file"
  exit 2
fi

echo "Topic coherence:" >> "$3"
java -Xms2G -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCoherence "$1" "$2" >> "$3"
echo "Topic compactness:" >> "$3"
mv "$1" "$1".bak
sed -r 's/xyz/_/g' "$1".bak >"$1"
java -Xmx8G -cp HLTA-es.jar:HLTA-deps.jar tm.hlta.TopicCompactness "$1" GoogleNews-vectors-negative300.bin >> "$3"
mv "$1".bak "$1"
cat "$3"
