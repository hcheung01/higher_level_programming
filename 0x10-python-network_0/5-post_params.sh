#!/bin/bash
# takes in a URL sends a POST request to passed URL and displays response body
curl -s "$1" -X POST -d "email:hr@holbertonschool.com&subject:I will always be here for PLD"
