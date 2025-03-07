from abc import ABC, abstractmethod

class Shop(ABC):
    pass

### Product Interface ###
class Products(Shop):
    """To initialize any product you're required to confirm: A product number, a product name, a price and the quantity.
    """
    def __init__(self, product_number: str, product_name: str, product_price: float, product_quantity: int):
        self.product_number = product_number
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __repr__(self):
        return f"{self.product_number} - {self.product_name}: {self.product_price} - {self.product_quantity}"


### Warehouse Interface ###
class Warehouse(Shop):
    @abstractmethod
    def add_to_warehouse(Product):
        pass

    @abstractmethod
    def rem_from_warehouse(Product):
        """Removes a product from the warehouse.
        """
        pass

    @abstractmethod
    def get_warehouse(Warehouse):
        """"Returns a dictionairy of all products in the warehouse.
        """
        pass

    @abstractmethod
    def check_availabilty(Warehouse, Product)->bool:
        """Returns True if this product is available.
        """
        pass

### Shopping Cart Interface ###
class ShoppingCart(Shop):
    @abstractmethod
    def create_cart()->list:
        """Creates a new shopping cart.
        """
        pass

    @abstractmethod
    def add_to_cart():
        """Adds items to the shopping cart.
        """
        pass

    @abstractmethod
    def rem_from_cart():
        """Removes items from shopping cart.
        """
        pass
### Payment Interface ###
class Payment(Shop):
    @abstractmethod
    def confirm_payment()->bool:
        """Returns True if the payment of an order is complete.
        """
        pass

### Simple Storage ###
class SimpleStorage(Warehouse):
    def __init__(self, location: str, size: float):
        self.location = location
        self.size = size
        self.inventory = {}

    def __repr__(self):
        return f"Location: {self.location}, Size: {self.size}"

    def add_to_warehouse(self, Product):
        """Adds a product to the warehouse.
        """
        self.inventory.update({Product.product_number: [Product.product_name, Product.product_price, Product.product_quantity]})
        return self.inventory

    def rem_from_warehouse(self, Product):
        """Removes a product from the warehouse.
        """
        self.inventory.pop(Product.product_number)

    def get_warehouse(self):
        """Returns all available items in the warehouse.
        """
        for k in self.inventory:
            print(f"{k}: {self.inventory[k]}")


    def check_availabilty(self, Product):
        """Returns True if this product is available.
        """
        if Product.product_number in self.inventory:
            print(f"{Product.product_number} - {Product.product_name} is available. {Product.product_quantity} in stock.")
            return True
        else:
            print("Product is not available")
            return False

class Article(Products):
    def __init__(self, product_number, product_name, product_price, product_quantity, edible: bool):
        super().__init__(product_number, product_name, product_price, product_quantity)
        self.edible = edible

    def need_cooling(self)->bool:
        if self.edible == True:
            return True
        else:
            return False





if __name__ == "__main__":
    shop = Shop()
    shoe = Article(product_number="0001", product_name="Gummies", product_price=0.99, product_quantity=1000, edible=True)
    shirt = Article(product_number="0002", product_name="T-Shirt", product_price=19.99, product_quantity=100, edible=False)


    store = SimpleStorage("Strasse 123", 1000)

    store.add_to_warehouse(shoe)
    store.add_to_warehouse(shirt)
    print(store.inventory)

    # store.rem_from_warehouse(shoe)
    store.get_warehouse()

    store.check_availabilty(shoe)
    store.check_availabilty(shirt)


