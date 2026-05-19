from fastapi import APIRouter, HTTPException, status

from app import store
from app.models import Book, BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[Book])
async def list_all_books():
    return store.list_books()


@router.get("/{book_id}", response_model=Book)
async def get_book_by_id(book_id: str):
    book = store.get_book(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_new_book(payload: BookCreate):
    book = store.create_book(payload.model_dump())
    return book


@router.put("/{book_id}", response_model=Book)
async def update_book_by_id(book_id: str, payload: BookUpdate):
    updated = store.update_book(book_id, {k: v for k, v in payload.model_dump().items() if v is not None})
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(book_id: str):
    deleted = store.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None
