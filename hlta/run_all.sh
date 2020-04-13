
find "$1" -type d -name "$1"_* | xargs -n1 -I {} sh hlta-es.sh {} 4 topic_models/{} 
