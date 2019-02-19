#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  const occur = list.filter(n => n === searchElement);
  return occur.length;
};
