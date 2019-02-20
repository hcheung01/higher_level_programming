#!/usr/bin/node
const req = require('request');
const id = parseInt(process.argv[2]);
req('https://swapi.co/api/films', function (error, response, body) {
  if (error) { console.log(error); }
  JSON.parse(body).results.forEach(function (movie) {
    if (movie.episode_id === id) {
      movie.characters.forEach(function (peeps) {
        req(peeps, function (error, response, body) {
          if (error) { console.log(error); }
          console.log(JSON.parse(body).name);
        });
      });
    }
  });
});
