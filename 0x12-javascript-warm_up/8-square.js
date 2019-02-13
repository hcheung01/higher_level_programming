#!/usr/bin/node
// script that prints a square
const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
}
let str = '';
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    str += 'X';
  }
  console.log(str);
  str = '';
}
