document.getElementById('loginButton').addEventListener('click', function () {
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();
  const errorMessage = document.getElementById('errorMessage');

  if (!email) {
    errorMessage.textContent = 'Email field is required.';
    errorMessage.style.display = 'block';
  } else if (!password) {
    errorMessage.textContent = 'Password field is required.';
    errorMessage.style.display = 'block';
  }
  else if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email)) {
    errorMessage.textContent = 'Please enter a valid email address.';
    errorMessage.style.display = 'block';
  }
  else if (password.length < 6) {
    errorMessage.textContent = 'Password must be at least 6 characters long.';
    errorMessage.style.display = 'block';
  }
  else {
    errorMessage.style.display = 'none';
    fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Invalid credentials. Please try again.');
        }
      })
      .then((data) => {
        alert('Login successful!');
        console.log('Response:', data);
      })
      .catch((error) => {
        errorMessage.textContent = error.message;
        errorMessage.style.display = 'block';
      });
  }
});