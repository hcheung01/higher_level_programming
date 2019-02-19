#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
var num = 0;
exports.logMe = function (item) {
  function print () {
    console.log(num + ': ' + item);
    num += 1;
  }
  print();
};
