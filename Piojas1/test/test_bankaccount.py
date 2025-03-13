import unittest
from src.bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        self.account.deposit(200)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw_too_much(self):
        self.account.deposit(100)
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-20)

if __name__ == "__main__":
    unittest.main()
