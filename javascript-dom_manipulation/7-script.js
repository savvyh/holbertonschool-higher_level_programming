document.addEventListener('DOMContentLoaded', () => {
  const movieList = document.querySelector('#list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      data.results.forEach(film => {
        const li = document.createElement('li');
        li.textContent = film.title;
        movieList.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
