# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints that handle reading and updating data for a resource such as items or tasks.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a new FastAPI application and configure a basic root or health endpoint.

#### Requirements
Completed program should:

- Import and initialize `FastAPI`
- Start the app with a meaningful title
- Add a `GET /health` or `/` endpoint
- Return a JSON response such as `{"status": "ok"}`

### 🛠️ Build a Resource Endpoint

#### Description
Create an API for a simple collection of items, such as books, tasks, or products.

#### Requirements
Completed program should:

- Define a list of sample data in memory
- Add a `GET /items` endpoint to return all items
- Add a `GET /items/{item_id}` endpoint to return one item by ID
- Return JSON responses with item details

### 🛠️ Add Create and Update Operations

#### Description
Expand the API to support creating and updating items using HTTP methods common in REST APIs.

#### Requirements
Completed program should:

- Add a `POST /items` endpoint to create a new item
- Accept JSON data from the request body
- Add a `PUT` or `PATCH` endpoint to update an item
- Return the updated item or confirmation message

### 🛠️ Validate and Improve the API

#### Description
Improve the API by validating inputs and making the responses easier to use.

#### Requirements
Completed program should:

- Use request models or simple validation for required fields
- Handle missing or invalid IDs gracefully
- Return clear status codes such as `200`, `201`, or `404`
- Keep the code organized with clear function names and a simple structure
