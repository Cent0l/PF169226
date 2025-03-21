import unittest
from src.stringmanipulator import StringManipulator

class TestStringManipulator(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(StringManipulator("test").reverse_string(), "tset")
        self.assertEqual(StringManipulator("12345").reverse_string(), "54321")
        self.assertEqual(StringManipulator("").reverse_string(), "")
        self.assertEqual(StringManipulator("!@#$%").reverse_string(), "%$#@!")
        self.assertEqual(StringManipulator("Ala ma kota").reverse_string(), "atok am alA")

    def test_count_words(self):
        self.assertEqual(StringManipulator("dwa slowa").count_words(), 2)
        self.assertEqual(StringManipulator("trzy niezle slowa").count_words(), 3)
        self.assertEqual(StringManipulator("").count_words(), 0)
        self.assertEqual(StringManipulator("   ").count_words(), 0)
        self.assertEqual(StringManipulator("Slowo wykrzynik!").count_words(), 2)
        self.assertEqual(StringManipulator("JednoDlugieINiepoprawneSlowo").count_words(), 1)

    def test_capitalize_words(self):
        self.assertEqual(StringManipulator("dwa slowa").capitalize_words(), "Dwa Slowa")
        self.assertEqual(StringManipulator("trzy Niezle slowa").capitalize_words(), "Trzy Niezle Slowa")
        self.assertEqual(StringManipulator("NIE KRZYCZ").capitalize_words(), "Nie Krzycz")
        self.assertEqual(StringManipulator("").capitalize_words(), "")
        self.assertEqual(StringManipulator("  spacje  ").capitalize_words(), "  Spacje  ")
        self.assertEqual(StringManipulator("123 abc").capitalize_words(), "123 Abc")

if __name__ == "__main__":
    unittest.main()
