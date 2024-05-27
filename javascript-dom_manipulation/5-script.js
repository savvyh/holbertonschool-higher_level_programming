document.addEventListener('DOMContentLoaded', () => {
  const currentHeader = document.querySelector('header');
  const newHeader = document.querySelector('#update_header');

  newHeader.addEventListener('click', () => {
    currentHeader.textContent = 'New Header!!!';
  });
});
