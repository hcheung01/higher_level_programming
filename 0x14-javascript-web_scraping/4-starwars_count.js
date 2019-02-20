#!/usr/bin/node
const request = require('request');
const f = process.argv[2];
request(f, function (error, response, body) {
  if (error) { console.log(error); }
  const results = JSON.parse(body).results;
  let ct = 0;
  for (let i = 0; i < results.length; i++) {
    let characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].includes('18')) {
        ct += 1;
      }
    }
  }
  console.log(ct);
});
