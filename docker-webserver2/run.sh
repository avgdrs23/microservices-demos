#!/bin/sh

image=$(basename $PWD)

#basename give the only name of current folder without path 
# PWD - current path 
# The image will be the name of current folder

docker run  -p  8081:8081 -d  "${image}:latest"

#Docker run webserver using port 8080
