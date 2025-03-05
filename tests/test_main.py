import pytest
from src.main import Product, Smartphone, LawnGrass, Categoryiter


def test_product_creation():
    p = Product("Bread", "Fresh bread", 2.5, 10)
    assert p.name == "Bread"
    assert p.description == "Fresh bread"
    assert p.price == 2.5
    assert p.quantity == 10


def test_new_product():
    info = {"name": "Milk", "price": 1.5, "description": "Low fat", "quantity": 8}
    p = Product.new_product(info)
    assert p.name == "Milk"
    assert p.price == 1.5
    assert p.description == "Low fat"
    assert p.quantity == 8


def test_str_representation():
    p = Product("Eggs", "Farm fresh eggs", 3.0, 12)
    expected = "Eggs, 3.0 руб. Остаток: 12 шт. Описание: Farm fresh eggs"
    assert str(p) == expected


def test_product_addition():
    p1 = Product("Bread", "Fresh bread", 2.5, 10)
    p2 = Product("Milk", "Low fat", 1.5, 8)
    total = p1 + p2
    assert total == (2.5 * 10) + (1.5 * 8)


def test_product_add_wrong_type():
    p = Product("Bread", "Fresh bread", 2.5, 10)
    with pytest.raises(TypeError):
        _ = p + "not a product"


def test_price_setter_increase():
    p = Product("Bread", "Fresh bread", 2.5, 10)
    # Установка цены, которая больше текущей, должна пройти без диалога с пользователем
    p.price = 3.0
    assert p.price == 3.0


def test_price_setter_decrease_confirm_yes(monkeypatch, capsys):
    p = Product("Bread", "Fresh bread", 3.0, 10)
    # Имитируем ввод "y" – подтверждение понижения цены
    monkeypatch.setattr("builtins.input", lambda prompt: "y")
    p.price = 2.0
    captured = capsys.readouterr().out
    assert "Цена успешно понижена до 2.0." in captured
    assert p.price == 2.0


def test_price_setter_decrease_confirm_no(monkeypatch, capsys):
    p = Product("Bread", "Fresh bread", 3.0, 10)
    # Имитируем ввод "n" – отмена понижения цены
    monkeypatch.setattr("builtins.input", lambda prompt: "n")
    p.price = 2.0
    captured = capsys.readouterr().out
    assert "Понижение цены отменено." in captured
    # Цена должна остаться прежней
    assert p.price == 3.0


def test_price_setter_invalid_value():
    p = Product("Bread", "Fresh bread", 2.5, 10)
    with pytest.raises(ValueError):
        p.price = 0
    with pytest.raises(ValueError):
        p.price = -5


def test_smartphone_addition():
    phone = Smartphone("iPhone", "Latest Model", 80000, 2, 0.9, "iPhone 14", "128GB", "Black")
    p = Product("Charger", "Fast charger", 1500, 1)
    total = phone + p
    expected_total = (80000 * 2) + (1500 * 1)
    assert total == expected_total


def test_categoryiter(monkeypatch):
    cat = Categoryiter("Electronics", "Electronic items", [])
    p1 = Product("TV", "LED TV", 20000, 1)
    p2 = Product("Radio", "Portable radio", 5000, 2)
    cat.add_product(p1)
    cat.add_product(p2)

    # Проверяем итерацию
    products = list(cat)
    assert products == [p1, p2]

    # Проверяем общее количество единиц в категории
    assert cat.total_quantity() == (1 + 2)

    # Проверяем, что метод get_products возвращает строковые представления продуктов
    strings = cat.get_products()
    assert isinstance(strings, list)
    for s in strings:
        assert isinstance(s, str)
