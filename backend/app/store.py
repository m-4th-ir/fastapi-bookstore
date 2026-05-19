import uuid
from datetime import datetime
from typing import Dict, List, Optional


store: Dict[str, Dict[str, dict]] = {
    "books": {}
}


# Seed data
_seed_books = [
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "price": 39.99,
        "in_stock": 10,
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "price": 42.50,
        "in_stock": 7,
    },
]

for book in _seed_books:
    book_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    store["books"][book_id] = {
        "id": book_id,
        "created_at": now,
        "updated_at": None,
        **book,
    }


def list_books() -> List[dict]:
    return list(store["books"].values())


def get_book(book_id: str) -> Optional[dict]:
    return store["books"].get(book_id)


def create_book(data: dict) -> dict:
    book_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    book = {
        "id": book_id,
        "created_at": now,
        "updated_at": None,
        **data,
    }
    store["books"][book_id] = book
    return book


def update_book(book_id: str, data: dict) -> Optional[dict]:
    existing = store["books"].get(book_id)
    if not existing:
        return None
    existing.update(data)
    existing["updated_at"] = datetime.utcnow().isoformat()
    return existing


def delete_book(book_id: str) -> bool:
    if book_id not in store["books"]:
        return False
    del store["books"][book_id]
    return True
