class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.__price = price

    def __str__(self):
        return (f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.Описание: {self.description}"
                f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented

    @classmethod
    def new_product(cls, product_info: dict):
        """
        Класс-метод для создания нового объекта Product на основе информации из словаря.
        :param product_info: Словарь с информацией о продукте
        :return: Новый экземпляр Product
        """
        # Извлекаем необходимые параметры из словаря
        name = product_info.get("name")
        price = product_info.get("price")
        description = product_info.get("description", "")
        quantity = product_info.get("quantity", 0)

        # Создаем и возвращаем новый объект Product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price  # Геттер для получения цены

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            print("Цена должна быть числом.")
            return

        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(
                f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): "
            )
            if confirmation.lower() == "y":
                self.__price = (
                    value  # Устанавливаем новую цену, если пользователь подтвердил
                )
                print(f"Цена успешно понижена до {value}.")
            else:
                print("Понижение цены отменено.")
        else:
            self.__price = value  # Устанавливаем новую цену, если она корректная

    def __string__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт. Описание: {self.description}"


class Categoryiter:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products
        Categoryiter.category_count += 1
        Categoryiter.product_count = len(products)
        self.__products = []

    def total_quantity(self):
        return sum(product.quantity for product in self.products)

    def get_products(self):
        return [str(product) for product in self.products]

    def __iter__(self):
        return Categoryiter(self)

    def add_product(self, product: Product):
        if isinstance(
            product, Product
        ):  # Проверяем, что переданный объект является экземпляром Product
            self.__products.append(product)
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    @property
    def get_products1(self):
        return (
            self.__products
        )  # Метод для получения списка продуктов (если это необходимо)

    def __str__(self):
        return (f"Категория: {self.name}, Товары: {[str(product) for product in self.__products]}"
                f"{self.name}, количество продуктов: {self.total_quantity()}шт.")


class Categorypro:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Categoryiter(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Categoryiter(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Categoryiter.category_count)
    print(Categoryiter.product_count)


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Categoryiter(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Categoryiter(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
