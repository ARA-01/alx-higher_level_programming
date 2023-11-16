#!/usr/bin/node
let narg = 0; // Initialize the counter variable

exports.logMe = function (item) {
  console.log('$(narg):$(item)');
  narg++; // increment the counter after printing
};
