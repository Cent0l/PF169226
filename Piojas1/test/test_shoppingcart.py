import unittest
from src.shoppingcart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Jabłko", 2.5, 3)
        self.assertEqual(self.cart.items, {"Jabłko": (3, 2.5)})

        self.cart.add_item("Banany", 4.0, 2)
        self.assertEqual(self.cart.items, {"Jabłko": (3, 2.5), "Banany": (2, 4.0)})

        self.cart.add_item("Jabłko", 2.5, 2)
        self.assertEqual(self.cart.items["Jabłko"], (5, 2.5))

    def test_add_item_invalid_values(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Jabłko", -5, 2)  # Ujemna cena
        with self.assertRaises(ValueError):
            self.cart.add_item("Banany", 4, 0)  # Ilość mniejsza niż 1

    def test_remove_item(self):
        self.cart.add_item("Jabłko", 2.5, 3)
        self.cart.remove_item("Jabłko", 2)
        self.assertEqual(self.cart.items, {"Jabłko": (1, 2.5)})

        self.cart.remove_item("Jabłko", 1)
        self.assertEqual(self.cart.items, {})


    def test_remove_item_not_in_cart(self):
        with self.assertRaises(KeyError):
            self.cart.remove_item("Nieistniejący produkt", 1)


    def test_get_total(self):
        self.cart.add_item("Jabłko", 2.5, 3)  # 3 * 2.5 = 7.5
        self.cart.add_item("Banany", 4.0, 2)  # 2 * 4.0 = 8.0
        self.assertEqual(self.cart.get_total(), 7.5 + 8.0)  # 15.5

    def test_clear(self):
        self.cart.add_item("Jabłko", 2.5, 3)
        self.cart.add_item("Banany", 4.0, 2)
        self.cart.clear()
        self.assertEqual(self.cart.items, {})

if __name__ == "__main__":
    unittest.main()
