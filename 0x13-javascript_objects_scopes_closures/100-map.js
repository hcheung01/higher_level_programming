#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let num = 0;
const map1 = list.map(x => x * num++);
console.log(map1);
