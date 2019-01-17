#!/bin/bash
# Takes in a URL, sends a request to that URL and display the size
curl -sI "$1" | grep Content-Length | awk '$1 == "Content-Length:" {print $2}'
