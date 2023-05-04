# Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module



```
const request = require('request');

// Get the movie ID from command line argument
const movieID = process.argv[2];

// Make a request to the Star Wars API for the movie data
request(`https://swapi.dev/api/films/${movieID}/`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Fetch the character data for each URL
    characterUrls.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
```