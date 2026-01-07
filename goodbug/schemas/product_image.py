from pydantic import BaseModel
from uuid import UUID


class ProductImageCreate(BaseModel):
    image_url: str
    is_primary: bool = False
    position: int = 1


class ProductImageResponse(BaseModel):
    id: UUID
    image_url: str
    is_primary: bool
    position: int

    class Config:
        from_attributes = True
