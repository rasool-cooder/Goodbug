from fastapi import FastAPI

from goodbug.routers import (
    product,
    product_image,
    admin_product,
    admin_product_image,
)

app = FastAPI(title="GoodBug Backend")

app.include_router(product)
app.include_router(product_image)
app.include_router(admin_product)
app.include_router(admin_product_image)
