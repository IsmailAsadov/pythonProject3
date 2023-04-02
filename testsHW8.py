import unittest
from hw8 import*

class My_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(func(5, 10), 48828125)
if __name__ == "__hw8__":
    unittest.hw8()
