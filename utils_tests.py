import unittest
from utils import Utils


class TestUtils(unittest.TestCase):

    def test_reverse(self):
        # String input - should raise error
        self.assertRaises(TypeError, Utils.reversed, "12345")
        # Float input - should raise error
        self.assertRaises(TypeError, Utils.reversed, 1.2345)
        # Integer input
        self.assertEqual(Utils.reversed(12345), 54321)
        self.assertEqual(Utils.reversed(-12345), -54321)

    def test_formatter(self):
        # String input - should raise error
        self.assertRaises(TypeError, Utils.formatter, "12345")
        # Float input - should raise error
        self.assertRaises(TypeError, Utils.formatter, 1.2345)
        # Integer input
        self.assertEqual(Utils.formatter(12345), ('0b11000000111001', '0o30071'))
        self.assertEqual(Utils.formatter(-12345), ('-0b11000000111001', '-0o30071'))
