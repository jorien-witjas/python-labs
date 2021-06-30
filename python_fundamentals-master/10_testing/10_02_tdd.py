'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

import unittest
#test to validate sum
class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual((3,5,6),14,"should be 14")
if __name__ == '__main__':
    unittest.main()


#test to validate if adding to a list has worked
class TestList(unittest.TestCase):
    def test_list(self):
        result = [1,2,3,4,5]
        self.assertEqual(result,[1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()