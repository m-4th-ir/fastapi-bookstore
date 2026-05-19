from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class BookBase(BaseModel):
    title: str
    author: str
    price: float
    in_stock: int

    @field_validator("price")
    @classmethod
    def validate_price(cls, v: float) -> float:
        if v < 0:
            raise ValueError("price must be non-negative")
        return v

    @field_validator("in_stock")
    @classmethod
    def validate_in_stock(cls, v: int) -> int:
        if v < 0:
            raise ValueError("in_stock must be non-negative")
        return v


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[int] = None


class Book(BookBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
