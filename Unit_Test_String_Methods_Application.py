#Test case for string methods
import unittest
from String_Methods import string_methods

class TestStringMethods(unittest.TestCase):

    def test_capitalize_string(self):
        output = string_methods.capitalize_string("software testing")
        self.assertEqual(output, "Software testing")

    def test_islower_string(self):
        output = string_methods.islower_string("software testing")
        self.assertTrue(output, "software testing")

    def test_replace_string(self):
        output = string_methods.replace_string("software testing")
        self.assertEqual(output, "unit testing")

    def test_count_string(self):
        output = string_methods.count_string("software testing")
        self.assertEqual(output, 1)
    
if __name__ == '__main__':
    unittest.main()