import unittest
from pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("44051401359"))
        self.assertFalse(PeselValidator.validate_format("1234567890"))
        self.assertFalse(PeselValidator.validate_format("abcdefghijk"))
        self.assertFalse(PeselValidator.validate_format("123456789012"))

    def test_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit("44051401359"))
        self.assertFalse(PeselValidator.validate_check_digit("44051401358"))

    def test_birth_date(self):
        self.assertTrue(PeselValidator.validate_birth_date("44051401359"))
        self.assertFalse(PeselValidator.validate_birth_date("99023112345"))

    def test_gender(self):
        self.assertEqual(PeselValidator.get_gender("44051401359"), "M")
        self.assertEqual(PeselValidator.get_gender("44051401358"), "F")

    def test_is_valid(self):
        self.assertTrue(PeselValidator.is_valid("44051401359"))
        self.assertFalse(PeselValidator.is_valid("12345678901"))

    def test_edge_cases(self):
        self.assertTrue(PeselValidator.is_valid("02222999994"))  
        self.assertTrue(PeselValidator.is_valid("00222999997"))  
