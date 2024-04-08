#!/usr/bin/node

function add (a, b) {
  const result = Number(a) + Number(b);
  console.log(result);
}

const args = process.argv.slice(2);

add(args[0], args[1]);
