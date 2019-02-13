#!/usr/bin/node
// function that increments and calls a function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
