#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movie = JSON.parse(body);

  let printedCharacters = 0;
  const numCharacters = movie.characters.length;

  function printNextCharacter (characterUrl) {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      printedCharacters++;
      if (printedCharacters < numCharacters) {
        printNextCharacter(movie.characters[printedCharacters]);
      }
    });
  }

  printNextCharacter(movie.characters[0]);
});
