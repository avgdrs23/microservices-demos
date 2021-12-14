#!/bin/sh

image=$(basename $PWD)

#basename give the only name of current folder without path 
#PWD - current path
# The image will be the name of current folder

docker build -t "${image}:latest" .
