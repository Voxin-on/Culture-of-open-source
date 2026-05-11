import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .settings import get_settings

app = FastAPI(title="Order Service")


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promo_code: str | None = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    total_before_discount: float
    discount_percent: float
    discount_amount: float
    total: float


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


class DiscountFromService(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    settings = get_settings()

    product = await fetch_product(order.product_id, settings.product_service_url)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )

    discount = await fetch_discount(
        product_id=order.product_id,
        quantity=order.quantity,
        unit_price=product.price,
        promo_code=order.promo_code,
        discount_service_url=settings.discount_service_url,
    )

    total_before_discount = product.price * order.quantity
    discount_amount = round(total_before_discount * discount.discount_percent / 100, 2)
    total = round(total_before_discount - discount_amount, 2)

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        total_before_discount=total_before_discount,
        discount_percent=discount.discount_percent,
        discount_amount=discount_amount,
        total=total,
    )


async def fetch_product(product_id: str, base_url: str) -> ProductFromService:
    url = f"{base_url}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())


async def fetch_discount(
    product_id: str,
    quantity: int,
    unit_price: float,
    promo_code: str | None,
    discount_service_url: str,
) -> DiscountFromService:
    url = f"{discount_service_url}/discounts/calculate"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(
                url,
                json={
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "promo_code": promo_code,
                },
            )

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Discount service is unavailable: {exc}",
        ) from exc

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Discount service returned an unexpected error",
        )

    return DiscountFromService.model_validate(response.json())