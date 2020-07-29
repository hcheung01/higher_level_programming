#!/bin/bash
# takes in a URL sends a POST request to passed URL and displays response body
curl -sX POST -d "email=hr@codingschool.com&subject=I will always be here for PLD" "$1"
