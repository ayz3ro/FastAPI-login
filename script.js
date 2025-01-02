document.getElementById('loginButton').addEventListener('click', function () {
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();
  const errorMessage = document.getElementById('errorMessage');

  // Check if both fields are filled out
  if (!email || !password) {
    errorMessage.textContent = 'Both fields are required.';
    errorMessage.style.display = 'block';
  }
  // Check if the email format is valid
  else if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email)) {
    errorMessage.textContent = 'Please enter a valid email address.';
    errorMessage.style.display = 'block';
  }
  // Check if the password meets the minimum length (e.g., 8 characters)
  else if (password.length < 8) {
    errorMessage.textContent = 'Password must be at least 8 characters long.';
    errorMessage.style.display = 'block';
  }
  else {
    errorMessage.style.display = 'none';
  }
});