#!/usr/bin/node
// prints the sum of 2 integers

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
