#Test case for string methods
import unittest
from String_Methods import string_methods

class TestStringMethods(unittest.TestCase):

    def test_capitalize_string(self):
        output = string_methods.capitalize_string("software testing")
        self.assertEqual(output, "Software testing")
if __name__ == '__main__':
    unittest.main()