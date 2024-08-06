# Restaurant Review Project Documentation

## Project Structure

- `main.py`: Contains the FastAPI application and endpoints.
- `models.py`: Defines the Pydantic model `RestaurantReview` used for validation.
- `utils.py`: Includes utility functions for reading reviews from an Excel file.

## Setup Instructions

### 1. Create a Virtual Environment

First, a virtual environment was created to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On macOS:

  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies

Installing FastAPI, Pydantic, and pandas using pip:

```bash
pip install fastapi pydantic pandas uvicorn
```


### 3. Running the Application

To run the FastAPI application, I used Uvicorn:

```bash
uvicorn main:app --reload
```

This command starts the FastAPI server with auto-reloading enabled. The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Add Review

**Endpoint:** `/reviews/`  
**Method:** `POST`  
**Request Body:**

```json
{
  "data": "2024-08-06",
  "reviewer": "John Doe",
  "testo": "Great service and food!",
  "sentiment": 1,
  "voto": 4.5
}
```

**Response:** Returns the added review.

### 2. Fetch Reviews

**Endpoint:** `/reviews/`  
**Method:** `GET`  
**Response:** Returns a list of all stored reviews.

### 3. Fetch Excel Reviews

**Endpoint:** `/fetch-excel-reviews/`  
**Method:** `GET`  
**Query Parameters:**

- `reviewer`: The name of the reviewer to filter reviews.

**Response:** Returns reviews from the Excel file based on the provided reviewer name or all reviews if no name is provided.

## Testing the API

### 1. Swagger UI

FastAPI automatically generates interactive API documentation using Swagger UI. Access it at `http://127.0.0.1:8000/docs` to test endpoints directly. So in my case this was easier but I had some other options as well:

### 2. Postman

Postman is a popular tool for testing APIs. We can import your API endpoints into Postman and use it to test different requests and responses.

### 3. Thunder Client

Thunder Client is a Visual Studio Code extension that provides a simple interface to test API endpoints.

## Explanation of Implementation

### FastAPI Setup

The `main.py` file initializes a basic FastAPI project and defines three endpoints:

- `create_review`: Adds a new review to the `reviews` list.
- `get_reviews`: Retrieves all stored reviews.
- `fetch_excel_reviews`: Fetches reviews from an Excel file, optionally filtered by reviewer name.

### Pydantic Model

The `models.py` file contains the `RestaurantReview` model with validation rules:

- `voto`: Must be between 0 and 5.
- `testo`: Length must be between 10 and 500 characters.

### Utilities

The `utils.py` file provides a function to read reviews from an Excel file. The reviews are converted to a dictionary format suitable for the FastAPI endpoints.

---


