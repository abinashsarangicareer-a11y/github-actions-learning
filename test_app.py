import unittest

from app import greet


class GreetTests(unittest.TestCase):
    def test_greet_includes_name(self):
        self.assertEqual(greet("Actions"), "Hello, Actions!")


if __name__ == "__main__":
    unittest.main()
