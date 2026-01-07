from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    slug: str
    short_description: Optional[str] = None
    long_description: Optional[str] = None
    price: float
    mrp: Optional[float] = None
    currency: str = "INR"

class ProductUpdate(BaseModel):
    name: Optional[str]
    short_description: Optional[str]
    long_description: Optional[str]
    price: Optional[float]
    mrp: Optional[float]
    is_active: Optional[bool]

class ProductResponse(BaseModel):
    id: UUID
    name: str
    slug: str
    short_description: str | None
    long_description: str | None
    price: float
    mrp: float | None
    currency: str
    is_active: bool

    class Config:
        from_attributes = True
