#!/usr/bin/node
// prints if its Not a Number with My number:

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
