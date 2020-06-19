
# find "$1" -type d -name "$1"_* | xargs -n1 -I {} sh hlta-es.sh {} 4 topic_models/{} 

# mkdir topic_models/profiles/profiles_adj

rm -rf topic_models/profiles/profiles_adj/*
rm -rf topic_models/profiles/profiles_loc/*
rm -rf topic_models/profiles/profiles_noun/*
rm -rf topic_models/profiles/profiles_org/*
rm -rf topic_models/profiles/profiles_per/*
rm -rf topic_models/profiles/profiles_verb/*
rm -rf topic_models/profiles/profiles_propn/*

sh hlta-es.sh profiles/profiles_propn 4 topic_models/profiles/profiles_propn 400
sh hlta-es.sh profiles/profiles_adj 4 topic_models/profiles/profiles_adj 200
sh hlta-es.sh profiles/profiles_loc 4 topic_models/profiles/profiles_loc 300
sh hlta-es.sh profiles/profiles_noun 4 topic_models/profiles/profiles_noun 200
sh hlta-es.sh profiles/profiles_org 4 topic_models/profiles/profiles_org 300
sh hlta-es.sh profiles/profiles_per 4 topic_models/profiles/profiles_per 300
sh hlta-es.sh profiles/profiles_verb 4 topic_models/profiles/profiles_verb 400

rm ../fusion/profiles/profiles_propn/*
rm ../fusion/profiles/profiles_adj/*
rm ../fusion/profiles/profiles_loc/*
rm ../fusion/profiles/profiles_noun/*
rm ../fusion/profiles/profiles_org/*
rm ../fusion/profiles/profiles_per/*
rm ../fusion/profiles/profiles_verb/*

cp topic_models/profiles/profiles_propn/myAssignment.topics.json ../fusion/profiles/profiles_propn/
cp topic_models/profiles/profiles_adj/myAssignment.topics.json ../fusion/profiles/profiles_adj/
cp topic_models/profiles/profiles_loc/myAssignment.topics.json ../fusion/profiles/profiles_loc/
cp topic_models/profiles/profiles_noun/myAssignment.topics.json ../fusion/profiles/profiles_noun/
cp topic_models/profiles/profiles_org/myAssignment.topics.json ../fusion/profiles/profiles_org/
cp topic_models/profiles/profiles_per/myAssignment.topics.json ../fusion/profiles/profiles_per/
cp topic_models/profiles/profiles_verb/myAssignment.topics.json ../fusion/profiles/profiles_verb/

cp topic_models/profiles/profiles_propn/myData.dict.csv ../fusion/profiles/profiles_propn/
cp topic_models/profiles/profiles_adj/myData.dict.csv ../fusion/profiles/profiles_adj/
cp topic_models/profiles/profiles_loc/myData.dict.csv ../fusion/profiles/profiles_loc/
cp topic_models/profiles/profiles_noun/myData.dict.csv ../fusion/profiles/profiles_noun/
cp topic_models/profiles/profiles_org/myData.dict.csv ../fusion/profiles/profiles_org/
cp topic_models/profiles/profiles_per/myData.dict.csv ../fusion/profiles/profiles_per/
cp topic_models/profiles/profiles_verb/myData.dict.csv ../fusion/profiles/profiles_verb/

cp topic_models/profiles/profiles_propn/myData.files.txt ../fusion/profiles/profiles_propn/
cp topic_models/profiles/profiles_adj/myData.files.txt ../fusion/profiles/profiles_adj/
cp topic_models/profiles/profiles_loc/myData.files.txt ../fusion/profiles/profiles_loc/
cp topic_models/profiles/profiles_noun/myData.files.txt ../fusion/profiles/profiles_noun/
cp topic_models/profiles/profiles_org/myData.files.txt ../fusion/profiles/profiles_org/
cp topic_models/profiles/profiles_per/myData.files.txt ../fusion/profiles/profiles_per/
cp topic_models/profiles/profiles_verb/myData.files.txt ../fusion/profiles/profiles_verb/

cp topic_models/profiles/profiles_propn/topicTree.nodes.json ../fusion/profiles/profiles_propn/
cp topic_models/profiles/profiles_adj/topicTree.nodes.json ../fusion/profiles/profiles_adj/
cp topic_models/profiles/profiles_loc/topicTree.nodes.json ../fusion/profiles/profiles_loc/
cp topic_models/profiles/profiles_noun/topicTree.nodes.json ../fusion/profiles/profiles_noun/
cp topic_models/profiles/profiles_org/topicTree.nodes.json ../fusion/profiles/profiles_org/
cp topic_models/profiles/profiles_per/topicTree.nodes.json ../fusion/profiles/profiles_per/
cp topic_models/profiles/profiles_verb/topicTree.nodes.json ../fusion/profiles/profiles_verb/
