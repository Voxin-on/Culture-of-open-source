from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.data.store import PRODUCTS

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "product-service"}


@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Product:
    product = PRODUCTS.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    return product