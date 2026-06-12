# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework in Python, including defining endpoints, handling request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create a Product API

#### Description
Create a FastAPI application that manages a small product catalog with endpoints for listing products, retrieving a product by ID, and adding new products.

#### Requirements
Completed program should:

- Define a FastAPI app in `main.py`.
- Create an in-memory product list with at least three example products.
- Implement a GET endpoint `/products` that returns all products as JSON.
- Implement a GET endpoint `/products/{product_id}` that returns the product matching `product_id` or a 404 error if not found.
- Implement a POST endpoint `/products` that accepts product data and adds it to the list.
- Use Pydantic models for request and response validation.

### 🛠️ Support JSON Input and Output

#### Description
Add request validation and structured JSON responses so clients can safely create and retrieve products.

#### Requirements
Completed program should:

- Define a `Product` Pydantic model with `id`, `name`, `description`, and `price` fields.
- Define a request body model for creating new products if needed.
- Return created product data from the POST endpoint.
- Use proper HTTP status codes such as `201 Created` and `404 Not Found`.
