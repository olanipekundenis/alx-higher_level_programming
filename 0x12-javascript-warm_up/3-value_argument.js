#!/usr/bin/node
// prints the third lettter of argument passed

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
