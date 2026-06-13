# 📘 Assignment: Intro to Flask Web Apps

## 🎯 Objective

Build a simple Flask web application that uses routes, dynamic responses, and form handling to show how Python can power a website.

## 📝 Tasks

### 🛠️ Create a Home Page

#### Description
Create a Flask app that serves a welcome page at the root URL.

#### Requirements
Completed program should:

- Define a Flask application in `app.py`.
- Implement a route for `/` that returns an HTML welcome message.
- Include a short description of the app on the home page.

### 🛠️ Add a Dynamic Greeting Route

#### Description
Add a route that greets visitors by name using a path parameter.

#### Requirements
Completed program should:

- Implement a route for `/hello/<name>`.
- Return a personalized greeting using the `name` parameter.
- Use HTML formatting in the response.

### 🛠️ Build a Contact Form

#### Description
Add a page where users can submit their name and a message with a simple HTML form.

#### Requirements
Completed program should:

- Implement a route for `/contact` that supports `GET` and `POST`.
- Display a form when the route is accessed with `GET`.
- When the form is submitted with `POST`, show a confirmation message with the submitted name and message.
- Use Flask request handling to read form data.
