#!/bin/bash
# sends a GET request to the URL and displays the body of the response
curl -sX GET "$1" -d "X-HolbertonSchool-User-Id=98"
