#!/usr/bin/node
// compute && print factorial
var n = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 1 || !n) {
    return 1;
  }
  return n * factorial(n - 1);
}
let final = factorial(n);
console.log(final);
