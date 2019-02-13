#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const number = parseInt(process.argv[2]);
if (!number) {
  console.log('Not a number');
} else {
  console.log('My number:', number);
}
