import unittest
from max_sum import max_sum_divisible_by_2


class TestMaxSum(unittest.TestCase):
    def test_example_1(self):
        arr = [5, 7, 13, 2, 14]
        self.assertEqual(max_sum_divisible_by_2(arr), 36)
    
    def test_example_2(self):
        arr = [3]
        self.assertEqual(max_sum_divisible_by_2(arr), 0)
    
    def test_empty_array(self):
        self.assertEqual(max_sum_divisible_by_2([]), 0)
    
    def test_single_even_number(self):
        self.assertEqual(max_sum_divisible_by_2([4]), 4)
        self.assertEqual(max_sum_divisible_by_2([8]), 8)
    
    def test_single_odd_number(self):
        self.assertEqual(max_sum_divisible_by_2([3]), 0)
        self.assertEqual(max_sum_divisible_by_2([7]), 0)
    
    def test_all_even_numbers(self):
        self.assertEqual(max_sum_divisible_by_2([2, 4, 6, 8]), 20)
        self.assertEqual(max_sum_divisible_by_2([10, 12, 14]), 36)
    
    def test_all_odd_numbers(self):
        self.assertEqual(max_sum_divisible_by_2([1, 3, 5]), 8)
        self.assertEqual(max_sum_divisible_by_2([7, 9, 11]), 20)
    
    def test_mixed_numbers_even_sum(self):
        self.assertEqual(max_sum_divisible_by_2([1, 2, 3, 4]), 10)
        self.assertEqual(max_sum_divisible_by_2([2, 4, 6, 1]), 12)
    
    def test_mixed_numbers_odd_sum(self):
        self.assertEqual(max_sum_divisible_by_2([1, 2, 3]), 6)
        self.assertEqual(max_sum_divisible_by_2([5, 7, 13, 2, 14]), 36)
    
    def test_two_odd_numbers(self):
        self.assertEqual(max_sum_divisible_by_2([3, 5]), 8)
        self.assertEqual(max_sum_divisible_by_2([1, 7]), 8)
    
    def test_large_numbers(self):
        self.assertEqual(max_sum_divisible_by_2([100, 200, 301]), 300)
        self.assertEqual(max_sum_divisible_by_2([1000, 2000, 3001]), 3000)


if __name__ == '__main__':
    unittest.main()
