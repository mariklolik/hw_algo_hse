import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), [1, 2])

    def test_example_2(self):
        self.assertEqual(two_sum([5, 5, 1, 4], 10), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-1, -3, 5, 9], 4), [0, 2])

    def test_zero(self):
        self.assertEqual(two_sum([0, 7, 11, 15], 7), [0, 1])

    def test_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3, 4], 10), [])
        
    def test_large_numbers(self):
        self.assertEqual(two_sum([100, 200, 300, 400], 700), [2, 3])

if __name__ == '__main__':
    unittest.main()
