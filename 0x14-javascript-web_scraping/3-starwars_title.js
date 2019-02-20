#!/usr/bin/node
const r = require('request');
const u = 'http://swapi.co/api/films/' + process.argv[2];
r(u, function (error, response, body) {
  console.log(JSON.parse(body).title || error);
});
