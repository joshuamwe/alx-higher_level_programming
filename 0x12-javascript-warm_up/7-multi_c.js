#!/usr/bin/node

const { argv } = require('process');

const myVar = parseInt(argv[2], 10);
const myMessage = 'C is fun';

if (!myVar) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log(myMessage);
  }
}
