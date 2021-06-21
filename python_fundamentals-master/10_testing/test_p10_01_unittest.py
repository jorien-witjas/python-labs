import unittest
from p10_01_unitest import get_email

class Testp10_01_unitest(unittest.TestCase):
    # define your tests as methods in here
    def test_structure(self):
        result = "giladgressel@hotmail.com"
        self.assertEqual(result,get_email("gilad","gressel","hotmail.com"))

    def test_equal(self):
        result = "giladgressel@hotmail.com"
        self.assertEqual(result,get_email("gilad","gressel","hotmail.uk"))

if __name__ == '__main__':
    unittest.main()