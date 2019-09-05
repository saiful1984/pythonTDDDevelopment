
import unittest
import pathmagic
from src.Calculator import Calculator


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calci = Calculator()

    def test_add(self):
        self.assertEqual(4, self.calci.add([2, 2]))

    def test_typeErr(self):
        self.assertRaises(TypeError, self.calci.add, 'Hello', 'World')


if __name__ == "__main__":
    unittest.main()
