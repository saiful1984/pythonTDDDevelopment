
import os
import sys
import unittest
par_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, par_dir)
from src.Calculator import Calculator


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calci = Calculator()

    def test_add(self):
        #test_list = [2, 2]
        self.assertEqual(4, self.calci.add([2, 2]))

    def test_typeErr(self):
        self.assertRaises(TypeError, self.calci.add, 'Hello', 'World')


if __name__ == "__main__":
    unittest.main()
