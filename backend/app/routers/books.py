from typing import Optional

from fastapi import APIRouter, HTTPException, Query, status

from app import store
from app.models import BookCreate, BookOut, BookUpdate, ErrorResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookOut])
async def list_books(
    q: Optional[str] = Query(None, description="Search query for title or description"),
    category: Optional[str] = Query(None, description="Filter by category"),
    author_id: Optional[str] = Query(None, description="Filter by author id"),
) -> list[BookOut]:
    books = store.search_books(query=q, category=category, author_id=author_id)
    return [BookOut(**b) for b in books]


@router.get("/{book_id}", response_model=BookOut, responses={404: {"model": ErrorResponse}})
async def get_book(book_id: str) -> BookOut:
    book = store.get_book(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Book with id {book_id} does not exist",
                "detail": None,
            },
        )
    return BookOut(**book)


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED, responses={404: {"model": ErrorResponse}})
async def create_book(payload: BookCreate) -> BookOut:
    # Ensure author exists
    author = store.get_author(payload.author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Author with id {payload.author_id} does not exist",
                "detail": None,
            },
        )
    book = store.create_book(payload.model_dump())
    return BookOut(**book)


@router.patch("/{book_id}", response_model=BookOut, responses={404: {"model": ErrorResponse}})
async def update_book(book_id: str, payload: BookUpdate) -> BookOut:
    data = payload.model_dump(exclude_unset=True)
    if "author_id" in data:
        author = store.get_author(data["author_id"])
        if not author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "error": "not_found",
                    "message": f"Author with id {data['author_id']} does not exist",
                    "detail": None,
                },
            )
    updated = store.update_book(book_id, data)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Book with id {book_id} does not exist",
                "detail": None,
            },
        )
    return BookOut(**updated)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": ErrorResponse}})
async def delete_book(book_id: str) -> None:
    deleted = store.delete_book(book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Book with id {book_id} does not exist",
                "detail": None,
            },
        )
