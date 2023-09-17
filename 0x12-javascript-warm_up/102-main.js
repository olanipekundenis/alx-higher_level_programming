#!/usr/bin/node
//adds integer 4 to the result of 102-add_me_maybe

const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
