# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that exposes endpoints for managing a simple collection of items, using JSON responses, path parameters, and request validation.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Create a FastAPI app and configure a simple API that responds to incoming requests from a browser or client.

#### Requirements
Completed program should:

- Install and import FastAPI in Python
- Create an app instance with a clear title for the API
- Add a root endpoint that returns a welcome message
- Start the server using Uvicorn or a similar ASGI server
- Confirm the app runs successfully in a local development environment

### 🛠️ Create CRUD Endpoints

#### Description
Add endpoints for listing, retrieving, and creating items in your API.

#### Requirements
Completed program should:

- Store items in an in-memory list or dictionary
- Create a GET endpoint to return all items
- Create a GET endpoint to return one item by its ID
- Create a POST endpoint to add a new item
- Return JSON data in a consistent format
- Use simple, readable route names and response structures

### 🛠️ Add Validation and Error Handling

#### Description
Improve the API by validating input and handling missing or invalid requests more cleanly.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data
- Require important fields such as name and price when creating an item
- Return a clear error when an item ID does not exist
- Use HTTP status codes such as 200, 201, and 404 appropriately
- Test the API using the browser-based docs or a tool such as curl
