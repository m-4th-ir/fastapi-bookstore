# FastAPI Bookstore Backend

Demo FastAPI bookstore backend with in-memory data store.

## Features

- Authors CRUD
- Books CRUD
- Search books by title/description, category, and author
- In-memory data store (no external database)

## Running Locally

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

Then open http://localhost:8000/docs for the interactive API docs.
