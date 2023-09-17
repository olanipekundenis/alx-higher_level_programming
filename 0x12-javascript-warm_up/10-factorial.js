#!/usr/bin/node
// It computes and prints a factorial of a number

function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
