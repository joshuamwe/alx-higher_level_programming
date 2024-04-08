#!/usr/bin/node

const { argv } = require('process');
const myVar = parseInt(argv[2], 10);
const mySymbol = 'X';

if (!myVar) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    for (let j = 0; j < myVar; j++) {
      process.stdout.write(mySymbol);
    }
    console.log();
  }
}
