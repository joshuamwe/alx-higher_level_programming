#!/usr/bin/node
// script that display the status code of a GET request

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
