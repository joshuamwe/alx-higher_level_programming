#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const results = JSON.parse(body).results;
  let count = 0;

  for (const list of results) {
    for (const character of list.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }

  console.log(count);
});
