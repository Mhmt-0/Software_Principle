# SRP(Single Responsibility Principle)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductRepository:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def get_total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

product_repo = ProductRepository()
product_repo.add_product(Product("Phone", 1000))
product_repo.add_product(Product("Laptop", 2000))
product_repo.add_product(Product("Headphones", 100))

cart = Cart()
products = product_repo.get_products()
cart.add_item(products[0])
cart.add_item(products[2])

total_price = cart.get_total_price()
print("Total Price:", total_price)
