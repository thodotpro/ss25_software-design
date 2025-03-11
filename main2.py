## CalculateCart ##
from nltk.misc.chomsky import verbs


class CalculateCart:
    def calc_cart(self, cart: MyCart) -> float:
        total = 0.0
        for item in cart.cart.values():
            product_price = item[2]
            quantity = item[3]
            total += product_price * quantity
        return total
