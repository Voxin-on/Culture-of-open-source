from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float
    promo_code: str | None = None


class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str


PROMO_CODES: dict[str, float] = {
    "STUDENT10": 10.0,
    "SALE20": 20.0,
}

BULK_THRESHOLD = 10
BULK_DISCOUNT = 15.0


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    if request.promo_code and request.promo_code in PROMO_CODES:
        percent = PROMO_CODES[request.promo_code]
        return DiscountResponse(
            discount_percent=percent,
            reason=f"Promo code '{request.promo_code}' applied",
        )

    if request.quantity >= BULK_THRESHOLD:
        return DiscountResponse(
            discount_percent=BULK_DISCOUNT,
            reason=f"Bulk discount for {request.quantity} units",
        )

    return DiscountResponse(
        discount_percent=0.0,
        reason="No discount applied",
    )