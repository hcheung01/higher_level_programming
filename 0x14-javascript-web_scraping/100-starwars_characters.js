#!/usr/bin/node
const req = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (error) { console.log(error); }
  JSON.parse(body).characters.forEach(function (peeps) {
    req(peeps, function (error, response, body) {
      if (error) { console.log(error); }
      console.log(JSON.parse(body).name);
    });
  });
});
