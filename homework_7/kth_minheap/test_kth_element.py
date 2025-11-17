import random
import unittest

from homework_7.kth_minheap.kth_element import (
    find_kth_largest_custom,
    find_kth_largest_heapq,
)


class TestKthLargestCustom(unittest.TestCase):
    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(find_kth_largest_custom(nums, k), 5)
    
    def test_example_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(find_kth_largest_custom(nums, k), 4)
    
    def test_largest_element(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_largest_custom(nums, 1), 6)
    
    def test_smallest_as_largest(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_largest_custom(nums, 6), 1)
    
    def test_single_element(self):
        nums = [42]
        self.assertEqual(find_kth_largest_custom(nums, 1), 42)
    
    def test_two_elements(self):
        nums = [1, 2]
        self.assertEqual(find_kth_largest_custom(nums, 1), 2)
        self.assertEqual(find_kth_largest_custom(nums, 2), 1)
    
    def test_all_same(self):
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(find_kth_largest_custom(nums, 3), 5)
    
    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(find_kth_largest_custom(nums, 2), 4)
    
    def test_sorted_descending(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(find_kth_largest_custom(nums, 2), 4)
    
    def test_negative_numbers(self):
        nums = [-1, -5, 3, 2, 0]
        self.assertEqual(find_kth_largest_custom(nums, 2), 2)
    
    def test_duplicates(self):
        nums = [1, 2, 2, 3, 3, 3, 4]
        self.assertEqual(find_kth_largest_custom(nums, 3), 3)
    
    def test_large_array(self):
        nums = list(range(100))
        random.shuffle(nums)
        self.assertEqual(find_kth_largest_custom(nums, 10), 90)
    
    def test_does_not_modify_original(self):
        nums = [3, 2, 1, 5, 6, 4]
        original = nums.copy()
        find_kth_largest_custom(nums, 2)
        self.assertEqual(nums, original)
    
    def test_invalid_k_zero(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest_custom(nums, 0)
    
    def test_invalid_k_too_large(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest_custom(nums, 4)
    
    def test_empty_array(self):
        nums = []
        with self.assertRaises(ValueError):
            find_kth_largest_custom(nums, 1)


class TestKthLargestHeapq(unittest.TestCase):
    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(find_kth_largest_heapq(nums, k), 5)
    
    def test_example_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(find_kth_largest_heapq(nums, k), 4)
    
    def test_largest_element(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_largest_heapq(nums, 1), 6)
    
    def test_smallest_as_largest(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_largest_heapq(nums, 6), 1)
    
    def test_single_element(self):
        nums = [42]
        self.assertEqual(find_kth_largest_heapq(nums, 1), 42)
    
    def test_two_elements(self):
        nums = [1, 2]
        self.assertEqual(find_kth_largest_heapq(nums, 1), 2)
        self.assertEqual(find_kth_largest_heapq(nums, 2), 1)
    
    def test_all_same(self):
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(find_kth_largest_heapq(nums, 3), 5)
    
    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(find_kth_largest_heapq(nums, 2), 4)
    
    def test_sorted_descending(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(find_kth_largest_heapq(nums, 2), 4)
    
    def test_negative_numbers(self):
        nums = [-1, -5, 3, 2, 0]
        self.assertEqual(find_kth_largest_heapq(nums, 2), 2)
    
    def test_duplicates(self):
        nums = [1, 2, 2, 3, 3, 3, 4]
        self.assertEqual(find_kth_largest_heapq(nums, 3), 3)
    
    def test_large_array(self):
        nums = list(range(100))
        random.shuffle(nums)
        self.assertEqual(find_kth_largest_heapq(nums, 10), 90)
    
    def test_does_not_modify_original(self):
        nums = [3, 2, 1, 5, 6, 4]
        original = nums.copy()
        find_kth_largest_heapq(nums, 2)
        self.assertEqual(nums, original)
    
    def test_invalid_k_zero(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest_heapq(nums, 0)
    
    def test_invalid_k_too_large(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest_heapq(nums, 4)
    
    def test_empty_array(self):
        nums = []
        with self.assertRaises(ValueError):
            find_kth_largest_heapq(nums, 1)


class TestBothMethodsEquivalence(unittest.TestCase):
    def test_both_return_same_result(self):
        nums = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        k = 4
        result1 = find_kth_largest_custom(nums, k)
        result2 = find_kth_largest_heapq(nums, k)
        self.assertEqual(result1, result2)
    
    def test_both_same_for_various_k(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        for k in range(1, len(nums) + 1):
            result1 = find_kth_largest_custom(nums, k)
            result2 = find_kth_largest_heapq(nums, k)
            self.assertEqual(result1, result2, f"Failed for k={k}")
    
    def test_both_same_for_random_data(self):
        for _ in range(10):
            nums = [random.randint(1, 100) for _ in range(20)]
            k = random.randint(1, len(nums))
            result1 = find_kth_largest_custom(nums, k)
            result2 = find_kth_largest_heapq(nums, k)
            self.assertEqual(result1, result2)
    
    def test_both_match_sorted_result(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        sorted_desc = sorted(nums, reverse=True)
        expected = sorted_desc[k - 1]
        
        result1 = find_kth_largest_custom(nums, k)
        result2 = find_kth_largest_heapq(nums, k)
        
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)


class TestPerformance(unittest.TestCase):
    def test_large_random_array(self):
        size = 10000
        nums = [random.randint(1, size * 10) for _ in range(size)]
        k = size // 2
        
        result1 = find_kth_largest_custom(nums, k)
        result2 = find_kth_largest_heapq(nums, k)
        
        sorted_nums = sorted(nums, reverse=True)
        expected = sorted_nums[k - 1]
        
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
    
    def test_worst_case_sorted(self):
        nums = list(range(1000))
        k = 500
        
        result1 = find_kth_largest_custom(nums, k)
        result2 = find_kth_largest_heapq(nums, k)
        
        self.assertEqual(result1, 500)
        self.assertEqual(result2, 500)
    
    def test_many_duplicates(self):
        nums = [random.randint(1, 10) for _ in range(1000)]
        k = 500
        
        result1 = find_kth_largest_custom(nums, k)
        result2 = find_kth_largest_heapq(nums, k)
        
        sorted_nums = sorted(nums, reverse=True)
        expected = sorted_nums[k - 1]
        
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)


if __name__ == "__main__":
    unittest.main()

