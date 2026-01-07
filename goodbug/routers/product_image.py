from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from goodbug.core.database import SessionLocal
from goodbug.modules.product_image import ProductImage
from goodbug.schemas.product_image import ProductImageResponse

router = APIRouter(
    prefix="/api/products",
    tags=["Product Images"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/{product_id}/images",
    response_model=List[ProductImageResponse]
)
def get_product_images(
    product_id: str,
    db: Session = Depends(get_db),
):
    return (
        db.query(ProductImage)
        .filter(ProductImage.product_id == product_id)
        .order_by(
            ProductImage.is_primary.desc(),
            ProductImage.position.asc(),
        )
        .all()
    )
