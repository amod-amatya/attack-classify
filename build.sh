#!/bin/sh

VAR=$1

docker build --quiet -t attack-spacy .
echo "Launching on docker container....."
echo " "
docker run -t attack-spacy

