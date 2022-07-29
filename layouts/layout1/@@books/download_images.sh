#!/usr/bin/env bash


for url in $(yq '.data.books[].image_src' data.yaml); do 
    curl -sSL "$url"
done
