#!/usr/bin/node
//  script that searches the second biggest integer in the list of arguments
let a = process.argv.map(Number);
let mx = 0;
let sc = 0;
for (let i = 2; i < a.length; i++) {
  if (a[i] > mx) {
    sc = mx;
    mx = a[i];
  } else if (a[i] > sc && a[i] < mx) {
    sc = a[i];
  }
}
console.log(sc);
