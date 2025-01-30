# Factorial API

This is a simple FastAPI application that calculates the factorial of a given number.

## Features
- Computes the factorial of a given integer
- Returns the factorial result in JSON format

## Installation

Ensure you have Python installed. Then, install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

## Running the API

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server, and the API will be available at `http://127.0.0.1:8000`.

## Usage

### Calculate Factorial

Send a GET request to the following endpoint:

```
GET /factorial/{startnum}
```

#### Example Request:

```
GET http://127.0.0.1:8000/factorial/5
```

#### Example Response:

```json
{
  "starting_number": 5,
  "factorial": 120
}
```

## Error Handling
- If `startnum` is `0`, the API returns:

```json
{
  "result": false
}
```

## API Documentation
FastAPI automatically generates interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License
This project is licensed under the MIT License.

