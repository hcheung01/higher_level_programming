#!/usr/bin/node
// class Square
const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) {
        console.log(Array(this.height + 1).join(c));
      }
    }
  }
};
