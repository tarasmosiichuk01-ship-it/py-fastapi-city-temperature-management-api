# City Temperature Management API

A FastAPI application for managing cities and storing temperature history data.

The application provides:

* CRUD operations for cities
* Fetching current weather data from an external API
* Saving temperature history to a SQLite database
* Filtering temperature records by city

---

## Features

* Async FastAPI application
* Async SQLAlchemy support
* SQLite database
* External weather API integration
* Temperature history storage
* REST API architecture
* Swagger documentation

---

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Alembic
* Pydantic
* HTTPX
* AsyncIO

---

## Project Structure

```text
app/
├── routers/
│   ├── city.py
│   └── temperature.py
├── crud.py
├── models.py
├── schemas.py
├── dependencies.py
├── temperature_service.py
├── database.py
└── main.py
```

---

## Installation

### Clone repository

```bash
git clone <repository-url>
cd py-fastapi-city-temperature-management-api
```

---

### Create virtual environment

#### MacOS/Linux

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root, as in `.env.sample`:

```env
API_WEATHER_KEY=your_weather_api_key
```

---

## Database Migration

Run Alembic migrations:

```bash
alembic upgrade head
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Cities

#### Create city

```http
POST /cities
```

#### Get all cities

```http
GET /cities
```

#### Get city by ID

```http
GET /cities/{city_id}
```

#### Update city

```http
PUT /cities/{city_id}
```

#### Delete city

```http
DELETE /cities/{city_id}
```

---

### Temperatures

#### Fetch and save temperatures

```http
POST /temperatures/update
```

#### Get all temperatures

```http
GET /temperatures
```

#### Filter temperatures by city

```http
GET /temperatures?city_id=1
```

---

## Design Decisions

* Async SQLAlchemy was used for asynchronous database operations.
* HTTPX AsyncClient was used for concurrent weather API requests.
* Separate routers and service layers were used to improve project structure and maintainability.
* SQLite was chosen for simplicity and lightweight local development.

---
