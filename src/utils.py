import json
import os

from src.main import Product, Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)

    with open(full_path, 'r', encoding="UTF-8") as file:
        products = json.load(file)
    return products


def create_objects(products):
    categories = []
    for category_data in products:
        products = [
            Product(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"]
            ) for product in category_data["products"]
        ]
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)

    return categories


if __name__ == "__main__":
    raw_products = read_json("../data/products.json")
    product_data = create_objects(raw_products)
    print(product_data)
