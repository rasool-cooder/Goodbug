from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from goodbug.core.database import SessionLocal
from goodbug.modules.product import Product
from goodbug.modules.product_image import ProductImage
from goodbug.schemas.product_image import (
    ProductImageCreate,
    ProductImageResponse,
)

router = APIRouter(
    prefix="/api/admin/products",
    tags=["Admin Product Images"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/{product_id}/images",
    response_model=ProductImageResponse
)
def add_product_image(
    product_id: str,
    payload: ProductImageCreate,
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if payload.is_primary:
        db.query(ProductImage).filter(
            ProductImage.product_id == product_id
        ).update({"is_primary": False})

    image = ProductImage(
        product_id=product_id,
        image_url=payload.image_url,
        is_primary=payload.is_primary,
        position=payload.position,
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return image
