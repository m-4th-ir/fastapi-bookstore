import uuid
from datetime import datetime, date
from typing import Dict, List, Optional


store: Dict[str, Dict[str, dict]] = {
    "authors": {},
    "books": {},
}


# Seed data

author_id_1 = str(uuid.uuid4())
author_id_2 = str(uuid.uuid4())

store["authors"][author_id_1] = {
    "id": author_id_1,
    "name": "Chinua Achebe",
    "bio": "Nigerian novelist, poet, and critic, best known for 'Things Fall Apart'.",
    "created_at": datetime.utcnow().isoformat(),
    "updated_at": None,
}

store["authors"][author_id_2] = {
    "id": author_id_2,
    "name": "Ama Ata Aidoo",
    "bio": "Ghanaian author, poet, and academic, known for exploring African women's experiences.",
    "created_at": datetime.utcnow().isoformat(),
    "updated_at": None,
}

book_id_1 = str(uuid.uuid4())
book_id_2 = str(uuid.uuid4())

store["books"][book_id_1] = {
    "id": book_id_1,
    "title": "Things Fall Apart",
    "description": "A classic novel about pre-colonial life in Nigeria and the arrival of Europeans.",
    "price": 15.99,
    "isbn": "9780385474542",
    "published_date": date(1958, 6, 17).isoformat(),
    "stock": 12,
    "category": "Fiction",
    "author_id": author_id_1,
    "created_at": datetime.utcnow().isoformat(),
    "updated_at": None,
}

store["books"][book_id_2] = {
    "id": book_id_2,
    "title": "Changes: A Love Story",
    "description": "A novel exploring modern relationships and gender roles in urban Africa.",
    "price": 12.5,
    "isbn": "9780435910105",
    "published_date": date(1991, 1, 1).isoformat(),
    "stock": 7,
    "category": "Fiction",
    "author_id": author_id_2,
    "created_at": datetime.utcnow().isoformat(),
    "updated_at": None,
}


# Author accessors

def list_authors() -> List[dict]:
    return list(store["authors"].values())


def get_author(author_id: str) -> Optional[dict]:
    return store["authors"].get(author_id)


def create_author(data: dict) -> dict:
    author_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    author = {
        "id": author_id,
        "created_at": now,
        "updated_at": None,
        **data,
    }
    store["authors"][author_id] = author
    return author


def update_author(author_id: str, data: dict) -> Optional[dict]:
    author = store["authors"].get(author_id)
    if not author:
        return None
    author.update(data)
    author["updated_at"] = datetime.utcnow().isoformat()
    return author


def delete_author(author_id: str) -> bool:
    if author_id not in store["authors"]:
        return False
    # Also delete books by this author
    books_to_delete = [
        book_id
        for book_id, book in store["books"].items()
        if book["author_id"] == author_id
    ]
    for book_id in books_to_delete:
        del store["books"][book_id]
    del store["authors"][author_id]
    return True


# Book accessors

def list_books() -> List[dict]:
    return list(store["books"].values())


def search_books(query: Optional[str] = None, category: Optional[str] = None, author_id: Optional[str] = None) -> List[dict]:
    books = list(store["books"].values())
    if query:
        q = query.lower()
        books = [
            b
            for b in books
            if q in b["title"].lower()
            or (b.get("description") and q in b["description"].lower())
        ]
    if category:
        books = [b for b in books if b.get("category") == category]
    if author_id:
        books = [b for b in books if b.get("author_id") == author_id]
    return books


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
    book = store["books"].get(book_id)
    if not book:
        return None
    book.update(data)
    book["updated_at"] = datetime.utcnow().isoformat()
    return book


def delete_book(book_id: str) -> bool:
    if book_id not in store["books"]:
        return False
    del store["books"][book_id]
    return True
