--- test_calculator.py ---
import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(9), 3)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.calc.factorial(-2)
        with self.assertRaises(ValueError):
            self.calc.factorial(2.5)


--- test_utils.py ---
import unittest
from src.utils import StringUtils, ListUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.string_utils = StringUtils()

    def test_reverse_string(self):
        self.assertEqual(self.string_utils.reverse_string("hello"), "olleh")
        self.assertEqual(self.string_utils.reverse_string(""), "")
        self.assertEqual(self.string_utils.reverse_string("a"), "a")

    def test_count_vowels(self):
        self.assertEqual(self.string_utils.count_vowels("hello"), 2)
        self.assertEqual(self.string_utils.count_vowels("AEIOU"), 5)
        self.assertEqual(self.string_utils.count_vowels("xyz"), 0)

    def test_is_palindrome(self):
        self.assertTrue(self.string_utils.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.string_utils.is_palindrome("hello"))

    def test_to_uppercase(self):
        self.assertEqual(self.string_utils.to_uppercase("abc"), "ABC")

    def test_to_lowercase(self):
        self.assertEqual(self.string_utils.to_lowercase("ABC"), "abc")

class TestListUtils(unittest.TestCase):
    def setUp(self):
        self.list_utils = ListUtils()

    def test_find_max(self):
        self.assertEqual(self.list_utils.find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(self.list_utils.find_max([-5, -2, -10]), -2)
        self.assertIsNone(self.list_utils.find_max([]))

    def test_find_min(self):
        self.assertEqual(self.list_utils.find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(self.list_utils.find_min([-5, -2, -10]), -10)
        self.assertIsNone(self.list_utils.find_min([]))

    def test_calculate_average(self):
        self.assertEqual(self.list_utils.calculate_average([2, 4, 6]), 4)
        self.assertIsNone(self.list_utils.calculate_average([]))

    def test_remove_duplicates(self):
        self.assertEqual(sorted(self.list_utils.remove_duplicates([1, 2, 2, 3])), [1, 2, 3])

    def test_sort_ascending(self):
        self.assertEqual(self.list_utils.sort_ascending([3, 1, 2]), [1, 2, 3])

    def test_sort_descending(self):
        self.assertEqual(self.list_utils.sort_descending([1, 2, 3]), [3, 2, 1])


--- Dodatek do test_book_manager.py ---
    def test_return_book_deletes_empty_borrowed_list(self):
        self.manager.add_book("B001", "Python", "John")
        self.manager.register_user("U001", "Alice")
        self.manager.borrow_book("B001", "U001")

        self.assertIn("U001", self.manager.borrowed_books)
        self.manager.return_book("B001", "U001")
        self.assertNotIn("U001", self.manager.borrowed_books)
