
import unittest
import pathmagic # noqa
from Calculator import Calculator


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calci = Calculator()

    def test_add(self):
        self.assertEqual(9, self.calci.add([2.0, 2.0, 5.0]))

    def test_substract(self):
        self.assertEqual(0, self.calci.subtract([2.0, 2.0]))

    def test_typeErr(self):
        self.assertRaises(TypeError, self.calci.add, 'Hello', 'World')


if __name__ == "__main__":
    unittest.main()
