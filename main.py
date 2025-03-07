from abc import ABC, abstractmethod

class Shop(ABC):
    pass

class Products(Shop):
    """To initialize any product you're required to confirm: A product number, a product name, a price and the quantity.
    """
    def __init__(self, product_number: str, product_name: str, product_price: float, product_quantity: int):
        self.product_number = product_number
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    @abstractmethod
    def add_to_warehouse():
        """Adds product to the warehouse.
        """
        pass

    def rem_from_warehouse():
        """Removes a product from the warehouse.
        """
        pass

class Warehouse(Shop):
    @abstractmethod
    def create_warehouse()->dict:
        pass

    @abstractmethod
    def get_warehouse():
        """"Returns a dictionairy of all products in the warehouse.
        """
        pass

    @abstractmethod
    def check_availabilty()->bool:
        """Returns True if this product is available.
        """
        pass


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

class Payment(Shop):
    @abstractmethod
    def confirm_payment()->bool:
        """Returns True if the payment of an order is complete.
        """
        pass

class Article(Products):
    def __init__(self, product_number, product_name, product_price, product_quantity, edible: bool):
        super().__init__(product_number, product_name, product_price, product_quantity)
        self.edible = edible

    def add_to_warehouse(self, warehouse):
        raise NotImplementedError

    def is_edible(self)->bool:
        pass



if __name__ == "__main__":
    shop = Shop()
    shoe = Article("0001", "Gummies", 99.9, 1000, True)

