#!/bin/bash
# Takes in a URL, sends a request to that URL
# and display the size of body of response
curl -sI $1 | awk '$1 == "Content-Length:" {print $2}'
