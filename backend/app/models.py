from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class AuthorBase(BaseModel):
    name: str = Field(..., min_length=1)
    bio: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    bio: Optional[str] = None


class AuthorOut(AuthorBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    isbn: str = Field(..., min_length=10, max_length=17)
    published_date: Optional[date] = None
    stock: int = Field(..., ge=0)
    category: Optional[str] = None
    author_id: str

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title must not be blank")
        return v


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    isbn: Optional[str] = Field(None, min_length=10, max_length=17)
    published_date: Optional[date] = None
    stock: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None
    author_id: Optional[str] = None


class BookOut(BookBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class ErrorResponse(BaseModel):
    error: str
    message: str
    detail: Optional[object] = None
