import pytest
from src.main import Product, Category
from unittest.mock import patch


def test_product_initialization():
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_category_initialization():
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    assert category2.name == "Телевизоры"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(category2.products) == 1  # Проверяем количество продуктов
    assert Category.category_count == 1  # Проверяем количество категорий
    assert Category.product_count == 1  # Проверяем количество продуктов


def test_product_count():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    assert Category.product_count == 3  # Проверяем количество продуктов


def test_category_count():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    assert Category.category_count == 4  # Проверяем количество категорий


def test_product_creation():
    product = Product("Смартфон", "Современный смартфон", 19999.99, 10)
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 19999.99
    assert product.quantity == 10


def test_new_product_class_method():
    product_info = {
        "name": "Ноутбук",
        "price": 59999.99,
        "description": "Мощный игровой ноутбук",
        "quantity": 5
    }
    product = Product.new_product(product_info)

    assert product.name == "Ноутбук"  # Проверка имени продукта
    assert product.price == 59999.99    # Проверка цены
    assert product.description == "Мощный игровой ноутбук"  # Проверка описания
    assert product.quantity == 5         # Проверка количества


def test_set_price():
    product = Product("Смартфон", "Современный смартфон", 19999.99, 10)
    product.price = 18000  # Устанавливаем новую цену
    assert product.price == 18000


def test_set_invalid_price_type():
    product = Product("Смартфон", "Современный смартфон", 19999.99, 10)

    with patch('builtins.print') as mock_print:  # Подменяем print для проверки вывода
        product.price = "двести"  # Пробуем установить строку вместо числа
        mock_print.assert_called_once_with("Цена должна быть числом.")

    assert product.price == 19999.99  # Цена не должна измениться


def test_set_price_confirmation_yes():
    product = Product("Смартфон", "Современный смартфон", 19999.99, 10)

    with patch('builtins.input', return_value='y'):
        product.price = 18000  # Понижаем цену и подтверждаем
        assert product.price == 18000


def test_set_price_confirmation_no():
    product = Product("Смартфон", "Современный смартфон", 19999.99, 10)

    with patch('builtins.input', return_value='n'):
        product.price = 18000  # Пробуем понизить цену, но отказываемся
        assert product.price == 19999.99  # Цена не должна измениться


def test_category_creation():
    category = Category("Электроника", "Все электронные устройства", [])
    assert category.name == "Электроника"
    assert category.description == "Все электронные устройства"
    assert category.get_products == []


def test_add_product_to_category():
    category = Category("Электроника", "Все электронные устройства", [])
    product = Product("Смартфон", "Современный смартфон", 19999.99, 10)
    category.add_product(product)
    assert category.get_products == [product]  # Проверяем, что продукт добавлен в категорию


def test_add_invalid_product_to_category():
    category = Category("Электроника", "Все электронные устройства", [])

    with pytest.raises(ValueError, match="Только объекты класса Product могут быть добавлены."):
        category.add_product("Некорректный продукт")  # Пробуем добавить строку вместо объекта Product


if __name__ == "__main__":
    pytest.main()
