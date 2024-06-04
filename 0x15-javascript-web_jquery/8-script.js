$(document).ready(function () {
  // Make an AJAX GET request to fetch the movie data
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract the movie results from the data
    const movies = data.results;

    // Loop through each movie and add its title to the list
    for (let i = 0; i < movies.length; i++) {
      const title = movies[i].title;
      $('#list_movies').append('<li>' + title + '</li>');
    }
  });
});
