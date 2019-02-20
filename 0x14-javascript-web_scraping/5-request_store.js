#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request(url).pipe(fs.createWriteStream(path));
