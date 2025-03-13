from abc import ABC, abstractmethod

### Main Shop Interface ###
class Shop(ABC):
    pass

### Product Interface ###
class Products(Shop):
    """To initialize any product you're required to confirm: A product number, a product name, a price and the quantity."""
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
    def add_to_warehouse(self, Product):
        """Adds a product to the warehouse."""
        pass

    @abstractmethod
    def rem_from_warehouse(self, Product):
        """Removes a product from the warehouse."""
        pass

    @abstractmethod
    def get_warehouse(self):
        """Returns a dictionary of all products in the warehouse."""
        pass

    @abstractmethod
    def check_availabilty(self, Product) -> bool:
        """Returns True if this product is available."""
        pass

### Shopping Cart Interface ###
class ShoppingCart(Shop):
    pass

### Payment Interface ###
class Payment(Shop):
    @abstractmethod
    def confirm_payment(self, order=None) -> bool:
        """Returns True if the payment of an order is complete."""
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
        """Adds a product to the warehouse."""
        self.inventory.update({Product.product_number: [Product.product_name, Product.product_price, Product.product_quantity]})
        return self.inventory

    def rem_from_warehouse(self, Product):
        """Removes a product from the warehouse."""
        self.inventory.pop(Product.product_number)

    def get_warehouse(self):
        """Returns all available items in the warehouse."""
        for k in self.inventory:
            print(f"{k}: {self.inventory[k]}")

    def check_availabilty(self, Product):
        """Returns True if this product is available."""
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

    def need_cooling(self) -> bool:
        if self.edible:
            return True
        else:
            return False

## My Cart ##
class MyCart(ShoppingCart):
    """Creates MyCart shopping cart. Initial cart number is 0. Initial key is 1. Initial quantity is 1."""
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

    def calculate_total(self):
        total = 0
        for item in self.cart.values():
            total += item[2] * item[3]  # Price * Quantity
        return total

## Payment Interface Implementation ##
class PaymentA(Payment):
    def __init__(self, discount: float = 0.0):
        """Initializes PaymentA with an optional discount."""
        self.discount = discount

    def apply_discount(self, order_total: float) -> float:
        """Applies the discount to the order total and returns the discounted price."""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * order_total
            order_total -= discount_amount
            print(f"Discount applied: {self.discount}% off. New total: {order_total}")
        else:
            print("No discount applied.")
        return order_total

    def confirm_payment(self, order=None) -> bool:
        """Confirms the payment after applying the discount."""
        if order is None:
            print("No order provided. Payment cannot be processed.")
            return False
        
        discounted_total = self.apply_discount(order['total'])
        if discounted_total > 0:
            print(f"Payment confirmed. Total amount: {discounted_total}")
            return True
        else:
            print("Payment failed. Invalid order total.")
            return False

## Checkout ##
class Checkout(ShoppingCart):
    def checkout(self, cart: MyCart, warehouse: Warehouse, payment: Payment):
        # Error occurred here: The Checkout class was trying to access self.cart,

        if not cart.cart:  # Now `cart` is passed as an argument from `MyCart`
            print("Dein Warenkorb ist leer!")
            return False
        
        for key, item in cart.cart.items():
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

        # Order total calculation
        order = {'total': cart.calculate_total()}  # Calculate the total price of the cart
        if payment.confirm_payment(order):
            print("Bezahlung erfolgreich. Bestellung abgeschlossen!")
            return True
        else:
            print("Bezahlung fehlgeschlagen!")
            return False
        
class CalculateCart(ShoppingCart):
    def calc_cart(self, cart: MyCart) -> float:
        total = 0.0
        for item in cart.cart.values():
            product_price = item[2]
            quantity = item[3]
            total += product_price * quantity
        return total

## Finish Order ##
class FinishOrder(ShoppingCart):
    def finish_order(self, ShoppingCart):
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
    store.get_warehouse()

    store.check_availabilty(shoe)
    store.check_availabilty(shirt)

    # Shopping Cart #
    cart = MyCart()
    cart.create_cart()
    cart.add_to_cart(shoe, 1001)
    cart.add_to_cart(shirt, 20)
    print(cart.cart)

    # Payment #
    payment = PaymentA(discount=10)  # 10% discount

    # Checkout #
    checkout = Checkout()
    checkout.checkout(cart, store, payment)  # Pass cart, store, and payment

    # CalculateCart #
    calc = CalculateCart()
    print(calc.calc_cart(cart))