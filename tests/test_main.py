import pytest
from src.main import Product, Smartphone, LawnGrass, Categoryiter, Categorypro


def mock_input_yes(prompt):
    return 'y'


def mock_input_no(prompt):
    return 'n'


# Тесты для класса Product
class TestProduct:
    def test_initialization(self):
        product = Product("Product1", "A test product", 100.0, 10)
        assert product.name == "Product1"
        assert product.description == "A test product"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_price_getter_setter_increase(self):
        product = Product("Product2", "Another test product", 200.0, 5)
        product.price = 250.0
        assert product.price == 250.0

    def test_price_setter_invalid_type(self, capsys):
        product = Product("Product3", "Invalid price type", 300.0, 2)
        product.price = "invalid"
        captured = capsys.readouterr()
        assert "Цена должна быть числом." in captured.out
        assert product.price == 300.0  # Цена не должна измениться

    def test_price_setter_zero_or_negative(self, capsys):
        product = Product("Product4", "Zero price", 400.0, 3)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 400.0

        product.price = -50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 400.0

    def test_price_setter_decrease_confirm_yes(self, monkeypatch):
        product = Product("Product5", "Decrease price", 500.0, 4)
        monkeypatch.setattr('builtins.input', lambda _: 'y')
        product.price = 450.0
        assert product.price == 450.0

    def test_price_setter_decrease_confirm_no(self, monkeypatch):
        product = Product("Product6", "Cancel decrease", 600.0, 6)
        monkeypatch.setattr('builtins.input', lambda _: 'n')
        product.price = 550.0
        assert product.price == 600.0  # Цена не должна измениться

    def test_add_method(self):
        product1 = Product("Product7", "Description7", 100.0, 2)
        product2 = Product("Product8", "Description8", 200.0, 3)
        total = product1 + product2
        assert total == (100.0 * 2) + (200.0 * 3)  # 200 + 600 = 800

    def test_add_method_with_invalid_type(self):
        product = Product("Product9", "Description9", 150.0, 1)
        with pytest.raises(TypeError):
            _ = product + "not a product"

    def test_str_method(self):
        product = Product("Product10", "A test product for __str__", 250.0, 5)
        expected_str = "Product10, 250.0 руб. Остаток: 5 шт.Описание: A test product for __str__Product10, 250.0 руб. Остаток: 5 шт."
        assert str(product) == expected_str

    def test_new_product_classmethod(self):
        product_info = {
            "name": "Product11",
            "description": "Created via classmethod",
            "price": 300.0,
            "quantity": 7
        }
        product = Product.new_product(product_info)
        assert product.name == "Product11"
        assert product.description == "Created via classmethod"
        assert product.price == 300.0
        assert product.quantity == 7


# Тесты для класса Smartphone
class TestSmartphone:
    def test_initialization(self):
        smartphone = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        assert smartphone.name == "iPhone"
        assert smartphone.description == "Latest model"
        assert smartphone.price == 999.99
        assert smartphone.quantity == 5
        assert smartphone.efficiency == "High"
        assert smartphone.model == "iPhone 14"
        assert smartphone.memory == "128GB"
        assert smartphone.color == "Black"

    def test_add_method(self):
        smartphone1 = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        smartphone2 = Smartphone("Samsung", "Latest model", 799.99, 3, "Medium", "Galaxy S21", "256GB", "Blue")
        total = smartphone1 + smartphone2
        expected_total = (999.99 * 5) + (799.99 * 3)
        assert total == expected_total

    def test_add_method_with_product(self):
        smartphone = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        product = Product("Accessory", "Charger", 50.0, 10)
        total = smartphone + product
        expected_total = (999.99 * 5) + (50.0 * 10)
        assert total == expected_total

    def test_add_method_with_invalid_type(self):
        smartphone = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        with pytest.raises(TypeError):
            _ = smartphone + 123  # Invalid type

    def test_str_method_inherited(self):
        smartphone = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        expected_str = "iPhone, 999.99 руб. Остаток: 5 шт.Описание: Latest modeliPhone, 999.99 руб. Остаток: 5 шт."
        assert str(smartphone) == expected_str


# Тесты для класса LawnGrass
class TestLawnGrass:
    def test_initialization(self):
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        assert grass.name == "Газонная трава"
        assert grass.description == "Элитная трава для газона"
        assert grass.price == 500.0
        assert grass.quantity == 20
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"

    def test_add_method(self):
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава", "Бюджетная трава для газона", 300.0, 15, "Украина", "10 дней", "Зеленый")
        total = grass1 + grass2
        expected_total = (500.0 * 20) + (300.0 * 15)
        assert total == expected_total

    def test_add_method_with_product(self):
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        product = Product("Удобрение", "Комплексное удобрение", 100.0, 10)
        total = grass + product
        expected_total = (500.0 * 20) + (100.0 * 10)
        assert total == expected_total

    def test_add_method_with_invalid_type(self):
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        with pytest.raises(TypeError):
            _ = grass + "invalid"

    def test_str_method_inherited(self):
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        expected_str = "Газонная трава, 500.0 руб. Остаток: 20 шт.Описание: Элитная трава для газонаГазонная трава, 500.0 руб. Остаток: 20 шт."
        assert str(grass) == expected_str


# Тесты для класса Categoryiter
class TestCategoryiter:
    def setup_method(self):
        # Создаем несколько продуктов
        self.product1 = Product("Product1", "Description1", 100.0, 10)
        self.product2 = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        self.product3 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней",
                                  "Зеленый")
        self.category = Categoryiter("Electronics", "Gadgets and devices",
                                     [self.product1, self.product2, self.product3])

    def test_initialization(self):
        assert self.category.name == "Electronics"
        assert self.category.description == "Gadgets and devices"
        assert self.category.products == [self.product1, self.product2, self.product3]
        assert Categoryiter.category_count == 1
        assert Categoryiter.product_count == 3
        assert self.category._Categoryiter__products == []

    def test_add_product_valid(self):
        new_product = Product("Product4", "Description4", 150.0, 7)
        self.category.add_product(new_product)
        assert len(self.category._Categoryiter__products) == 1
        assert self.category.get_products1 == [new_product]

    def test_add_product_invalid(self):
        with pytest.raises(ValueError):
            self.category.add_product("Not a product")

    def test_total_quantity(self):
        assert self.category.total_quantity() == 10 + 5 + 20  # 35

    def test_get_products(self):
        expected = [
            "Product1, 100.0 руб. Остаток: 10 шт.Описание: Description1Product1, 100.0 руб. Остаток: 10 шт.",
            "iPhone, 999.99 руб. Остаток: 5 шт.Описание: Latest modeliPhone, 999.99 руб. Остаток: 5 шт.",
            "Газонная трава, 500.0 руб. Остаток: 20 шт.Описание: Элитная трава для газонаГазонная трава, 500.0 руб. Остаток: 20 шт."
        ]
        assert self.category.get_products() == expected

    def test_iteration(self):
        iterator = iter(self.category)
        assert next(iterator) == self.product1
        assert next(iterator) == self.product2
        assert next(iterator) == self.product3
        with pytest.raises(StopIteration):
            next(iterator)

    def test_str_method(self):
        expected_str = (
            f"Категория: Electronics, Товары: ['Product1, 100.0 руб. Остаток: 10 шт.Описание: Description1Product1, 100.0 руб. Остаток: 10 шт.', "
            f"'iPhone, 999.99 руб. Остаток: 5 шт.Описание: Latest modeliPhone, 999.99 руб. Остаток: 5 шт.', "
            f"'Газонная трава, 500.0 руб. Остаток: 20 шт.Описание: Элитная трава для газонаГазонная трава, 500.0 руб. Остаток: 20 шт.']"
            f"Electronics, количество продуктов: 35шт."
        )
        assert str(self.category) == expected_str


# Тесты для класса Categorypro
class TestCategorypro:
    def setup_method(self):
        # Создаем несколько продуктов и категорию
        self.product1 = Product("Product1", "Description1", 100.0, 10)
        self.product2 = Smartphone("iPhone", "Latest model", 999.99, 5, "High", "iPhone 14", "128GB", "Black")
        self.category = Categoryiter("Electronics", "Gadgets and devices", [self.product1, self.product2])
        self.category_pro = Categorypro(self.category)

    def test_initialization(self):
        assert self.category_pro.category == self.category
        assert self.category_pro.index == 0

    def test_iteration(self):
        iterator = iter(self.category_pro)
        assert next(iterator) == self.product1
        assert next(iterator) == self.product2
        with pytest.raises(StopIteration):
            next(iterator)

    def test_full_iteration_multiple_iterators(self):
        # Проверяем, что несколько итераторов работают независимо
        iterator1 = iter(self.category_pro)
        iterator2 = iter(self.category_pro)
        assert next(iterator1) == self.product1
        assert next(iterator2) == self.product1
        assert next(iterator1) == self.product2
        assert next(iterator2) == self.product2
        with pytest.raises(StopIteration):
            next(iterator1)
        with pytest.raises(StopIteration):
            next(iterator2)
