Simple Login Page

This is a simple login page with client-side validation for email and password fields. It features a clean and responsive design using HTML, CSS, and JavaScript. The backend is built with Python using FastAPI, enabling secure and efficient authentication.

Features
	•	Frontend:
	•	Login form with email and password fields.
	•	Email validation using regex for proper format.
	•	Password validation to ensure a minimum length of 6 characters.
	•	Error messages for invalid input.
	•	Responsive design for various screen sizes.
	•	Backend:
	•	Built with FastAPI, a modern, fast (high-performance) web framework for Python.
	•	API endpoints for user authentication.
	•	Secure password handling (e.g., hashing and validation).
	•	Structured, scalable backend.

Technologies Used

Frontend:
	•	HTML: Structure of the login page.
	•	CSS: Styling for a clean and responsive user interface.
	•	JavaScript: Client-side input validation.

Backend:
	•	Python: Server-side language.
	•	FastAPI: Web framework for building the API.
	•	Uvicorn: ASGI server for running the FastAPI application.

Installation

Prerequisites:
	•	Python 3.9+
	•	Node.js (Optional for advanced frontend features)
	•	Package manager: pip

Steps:
	1.	Clone the Repository:

git clone https://github.com/yourusername/simple-login-page.git
cd simple-login-page


	2.	Install Backend Dependencies:

pip install fastapi uvicorn


	3.	Run the Backend Server:

uvicorn main:app --reload

	•	This will start the FastAPI backend server at http://127.0.0.1:8000.

	4.	Set Up the Frontend:
	•	Open index.html in a web browser.
	•	The login form will interact with the backend at the configured API endpoint.

Project Structure

simple-login-page/
├── frontend/
│   ├── index.html      # Main HTML file
│   ├── styles.css      # Styling for the login page
│   ├── script.js       # Client-side validation logic
├── backend/
│   ├── main.py         # FastAPI backend logic
├── README.md           # Project documentation

API Endpoints

POST /login
	•	Description: Validates user credentials.
	•	Request Body:

{
  "email": "user@example.com",
  "password": "securepassword"
}


	•	Response:
	•	200 OK: Login successful.
	•	401 Unauthorized: Invalid credentials.

Future Improvements
	•	Add database integration for user authentication.
	•	Implement password recovery functionality.
	•	Enhance frontend design with animations or frameworks like React or Vue.js.
	•	Add testing for both frontend and backend.

License
