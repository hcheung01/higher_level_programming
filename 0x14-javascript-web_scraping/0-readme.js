#!/usr/bin/node

let fs = require('fs');

fs.readFile(process.argv[2], function (err, buf) {
  if (!err) {
    console.log(buf.toString());
  } else {
    console.log(err);
  }
});
