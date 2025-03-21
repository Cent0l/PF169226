import unittest
from src.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib = fibonacci()

    def test_base_cases(self):
        self.assertEqual(self.fib.fibo(0), 0)
        self.assertEqual(self.fib.fibo(1), 1)

    def test_small_values(self):
        self.assertEqual(self.fib.fibo(2), 1)
        self.assertEqual(self.fib.fibo(3), 2)
        self.assertEqual(self.fib.fibo(4), 3)
        self.assertEqual(self.fib.fibo(5), 5)
        self.assertEqual(self.fib.fibo(6), 8)

    def test_large_values(self):
        self.assertEqual(self.fib.fibo(10), 55)
        self.assertEqual(self.fib.fibo(20), 6765)
        self.assertEqual(self.fib.fibo(30), 832040)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.fib.fibo(-1)

if __name__ == "__main__":
    unittest.main()