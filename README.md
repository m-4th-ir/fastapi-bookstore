# FastAPI Bookstore

Demo FastAPI backend for a simple bookstore, using an in-memory store.

## Tech Stack
- FastAPI
- Pydantic v2
- Uvicorn

## Running Locally

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Base URL: `http://localhost:8000`

## API Overview

- `GET /health` - health check
- `GET /api/v1/books/` - list all books
- `GET /api/v1/books/{book_id}` - get a single book
- `POST /api/v1/books/` - create a book
- `PUT /api/v1/books/{book_id}` - update a book
- `DELETE /api/v1/books/{book_id}` - delete a book
