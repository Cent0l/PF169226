class ShoppingCart:

    def __init__(self):
        self.items = {}


    def add_item(self,name,price,quantity):
        if price <0 or quantity <1:
            raise ValueError("price cannot be 0, or quantity cannot be lower than one")

        if name in self.items:
            self.items[name]=(self.items[name][0]+quantity,price)
        else:
            self.items[name]=(quantity,price)


    def remove_item(self, name, quantity=1):
        if name not in self.items:
            raise KeyError(f"There is no '{name}' in cart ")

        current_quantity, price = self.items[name]

        if quantity >= current_quantity:
            del self.items[name]
        else:
            self.items[name] = (current_quantity - quantity, price)


    def get_total(self):
        return sum(quantity * price for quantity, price in self.items.values())


    def clear(self):
        self.items.clear()
