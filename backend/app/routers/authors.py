from fastapi import APIRouter, HTTPException, status

from app import store
from app.models import AuthorCreate, AuthorOut, AuthorUpdate, ErrorResponse

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", response_model=list[AuthorOut])
async def list_all_authors() -> list[AuthorOut]:
    return [AuthorOut(**a) for a in store.list_authors()]


@router.get("/{author_id}", response_model=AuthorOut, responses={404: {"model": ErrorResponse}})
async def get_author(author_id: str) -> AuthorOut:
    author = store.get_author(author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Author with id {author_id} does not exist",
                "detail": None,
            },
        )
    return AuthorOut(**author)


@router.post("/", response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
async def create_author(payload: AuthorCreate) -> AuthorOut:
    author = store.create_author(payload.model_dump())
    return AuthorOut(**author)


@router.patch("/{author_id}", response_model=AuthorOut, responses={404: {"model": ErrorResponse}})
async def update_author(author_id: str, payload: AuthorUpdate) -> AuthorOut:
    updated = store.update_author(author_id, payload.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Author with id {author_id} does not exist",
                "detail": None,
            },
        )
    return AuthorOut(**updated)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": ErrorResponse}})
async def delete_author(author_id: str) -> None:
    deleted = store.delete_author(author_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "not_found",
                "message": f"Author with id {author_id} does not exist",
                "detail": None,
            },
        )
