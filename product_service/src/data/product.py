from app.models.product import Product

PRODUCTS: dict[str, Product] = {
    "pencil": Product(
        id="pencil",
        name="Pencil",
        price=1.50,
        available=True,
    ),
    "notebook": Product(
        id="notebook",
        name="Notebook",
        price=4.20,
        available=True,
    ),
    "backpack": Product(
        id="backpack",
        name="Backpack",
        price=35.00,
        available=False,
    ),
}