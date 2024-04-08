#!/usr/bin/node

const { argv } = require('process');

const myVar = parseInt(argv[2], 10);

if (!myVar) {
  console.log('Not a number');
} else {
  console.log('My number:', myVar);
}
