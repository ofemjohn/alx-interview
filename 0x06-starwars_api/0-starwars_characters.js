#!/usr/bin/node

const request = require('request');
const apiEndpoint = 'https://swapi-api.hbtn.io/api';

// Fetches the list of character URLs for the specified movie
function fetchCharacterUrls (movieId) {
  const url = `${apiEndpoint}/films/${movieId}/`;
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Unexpected response: ${response.statusCode}`));
      } else {
        const { characters } = JSON.parse(body);
        resolve(characters);
      }
    });
  });
}

// Fetches the name of the character at the specified URL
function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Unexpected response: ${response.statusCode}`));
      } else {
        const { name } = JSON.parse(body);
        resolve(name);
      }
    });
  });
}

// Prints the names of all characters in the specified movie
async function printCharacters (movieId) {
  try {
    const characterUrls = await fetchCharacterUrls(movieId);
    for (const url of characterUrls) {
      const name = await fetchCharacterName(url);
      console.log(name);
    }
  } catch (error) {
    console.error(error);
  }
}

// Main
if (require.main === module) {
  const movieId = process.argv[2];
  printCharacters(movieId);
}

module.exports = {
  fetchCharacterUrls,
  fetchCharacterName,
  printCharacters
};
