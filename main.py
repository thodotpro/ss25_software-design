from abc import ABC, abstractmethod

### Main Shop Interface ###
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
        """Adds a product to the warehouse.
        """
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
    pass

### Payment Interface ###
class Payment(Shop):
    @abstractmethod
    def confirm_payment()->bool:
        """Returns True if the payment of an order is complete.
        """
        pass

## Simple Storage ##
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
        if Product.product_number in self.inventory.keys():
            print(f"{Product.product_number} - {Product.product_name} is available. {Product.product_quantity} in stock.")
            return True
        else:
            print("Product is not available")
            return False

## Article ##
class Article(Products):    
    def __init__(self, product_number, product_name, product_price, product_quantity, edible: bool):
        super().__init__(product_number, product_name, product_price, product_quantity)
        self.edible = edible

    def need_cooling(self)->bool:
        if self.edible == True:
            return True
        else:
            return False

## My Cart ##
class MyCart(ShoppingCart):
    """Creates MyCart shopping cart. Initial cart number is 0. Initial key is 1. Initial quantity is 1.
    """
    def __init__(self):
        self.cart = {}
        self.cart_number = 1
        self.key = 1
        self.quantity = 1

    def create_cart(self):
        self.cart = {}
        self.cart_number += 1
        return self.cart

    def add_to_cart(self, Products, order_quantity: int):
        if self.check_availabilty(Products, order_quantity) == True:
            self.quantity = order_quantity
            self.cart.update({self.key: [Products.product_number, Products.product_name, Products.product_price, self.quantity]})
            self.key += 1
            return self.cart
        else:
            print("More products are on their way. Please try again later.")

    def rem_from_cart(self, order_key: int):
        if order_key in self.cart.keys():
            self.cart.pop(order_key)
            return self.cart
        else:
            print("This article is not in your cart.")
        

    def check_availabilty(self, Product, quantity: int):
        if Product.product_quantity >= quantity:
            return True
        else:
            print(f"{quantity} of {Product.product_name} is not available. Only {Product.product_quantity} in stock.")
            return False

## Checkout ##
class Checkout(ShoppingCart):
    def checkout(self, warehouse: Warehouse, payment: Payment):
        """Geht den Warenkorb durch, prüft die Verfügbarkeit und führt die Zahlung aus."""
        if not self.cart:
            print("Dein Warenkorb ist leer!")
            return False
        
        for key, item in self.cart.items():
            product_number = item[0]  # Artikelnummer
            product_name = item[1]  # Produktname
            quantity = item[3]  # Bestellte Menge

            # Prüfen, ob das Produkt im Lager verfügbar ist
            if product_number in warehouse.inventory:
                stock_quantity = warehouse.inventory[product_number][2]  # Lagerbestand
                if stock_quantity >= quantity:
                    warehouse.inventory[product_number][2] -= quantity  # Bestand aktualisieren
                else:
                    print(f"Nicht genügend Bestand für {product_name}. Verfügbar: {stock_quantity}, benötigt: {quantity}.")
                    return False
            else:
                print(f"{product_name} ist nicht im Lager vorhanden.")
                return False

        # Zahlung bestätigen
        if payment.confirm_payment():
            print("Bezahlung erfolgreich. Bestellung abgeschlossen!")
            return True
        else:
            print("Bezahlung fehlgeschlagen!")
            return False

## Finish Order ##
class FinishOrder(ShoppingCart):
    def finish_order(ShoppingCart):
        if Payment.confirm_payment() == True:
            pass
        else:
            print("")

if __name__ == "__main__":

    # Shop #
    shop = Shop()

    # Article #
    shoe = Article(product_number="0001", product_name="Gummies", product_price=0.99, product_quantity=1000, edible=True)
    shirt = Article(product_number="0002", product_name="T-Shirt", product_price=19.99, product_quantity=100, edible=False)

    # Simple Storage #
    store = SimpleStorage("Strasse 123", 1000)

    store.add_to_warehouse(shoe)
    store.add_to_warehouse(shirt)
    # print(store.inventory)

    # store.rem_from_warehouse(shoe)
    store.get_warehouse()

    store.check_availabilty(shoe)
    store.check_availabilty(shirt)

    # Shopping Cart #
    cart = MyCart()
    cart.create_cart()
    cart.add_to_cart(shoe, 1000)
    cart.add_to_cart(shirt, 20)
    print(cart.cart)

    # cart.rem_from_cart(1)
    # print(cart.cart)