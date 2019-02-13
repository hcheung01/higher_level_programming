#!/usr/bin/node
// function that increments and calls a function
module.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
