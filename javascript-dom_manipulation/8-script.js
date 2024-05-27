document.addEventListener('DOMContentLoaded', () => {
  const helloDisplay = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      helloDisplay.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
