import random
import unittest

from homework_6.kth.kth_element import find_kth_largest, find_kth_smallest


class TestKthLargest(unittest.TestCase):
    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(find_kth_largest(nums, k), 5)
    
    def test_example_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(find_kth_largest(nums, k), 4)
    
    def test_largest_element(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_largest(nums, 1), 6)
    
    def test_smallest_as_largest(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_largest(nums, 6), 1)
    
    def test_single_element(self):
        """Array with single element."""
        nums = [42]
        self.assertEqual(find_kth_largest(nums, 1), 42)
    
    def test_two_elements(self):
        nums = [1, 2]
        self.assertEqual(find_kth_largest(nums, 1), 2)
        self.assertEqual(find_kth_largest(nums, 2), 1)
    
    def test_all_same(self):
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(find_kth_largest(nums, 3), 5)
    
    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(find_kth_largest(nums, 2), 4)
    
    def test_sorted_descending(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(find_kth_largest(nums, 2), 4)
    
    def test_negative_numbers(self):
        nums = [-1, -5, 3, 2, 0]
        self.assertEqual(find_kth_largest(nums, 2), 2)
    
    def test_duplicates(self):
        nums = [1, 2, 2, 3, 3, 3, 4]
        self.assertEqual(find_kth_largest(nums, 3), 3)
    
    def test_large_array(self):
        nums = list(range(100))
        random.shuffle(nums)
        self.assertEqual(find_kth_largest(nums, 10), 90)
    
    def test_does_not_modify_original(self):
        """Ensure the original array is not modified."""
        nums = [3, 2, 1, 5, 6, 4]
        original = nums.copy()
        find_kth_largest(nums, 2)
        self.assertEqual(nums, original)
    
    def test_invalid_k_zero(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest(nums, 0)
    
    def test_invalid_k_too_large(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest(nums, 4)
    
    def test_empty_array(self):
        nums = []
        with self.assertRaises(ValueError):
            find_kth_largest(nums, 1)


class TestKthSmallest(unittest.TestCase):
    def test_smallest_element(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_smallest(nums, 1), 1)
    
    def test_example_converted(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_smallest(nums, 5), 5)
    
    def test_second_smallest(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_smallest(nums, 2), 2)
    
    def test_largest_as_smallest(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_smallest(nums, 6), 6)
    
    def test_with_duplicates(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(find_kth_smallest(nums, 4), 3)
    
    def test_single_element(self):
        """Array with single element."""
        nums = [42]
        self.assertEqual(find_kth_smallest(nums, 1), 42)
    
    def test_does_not_modify_original(self):
        """Ensure the original array is not modified."""
        nums = [3, 2, 1, 5, 6, 4]
        original = nums.copy()
        find_kth_smallest(nums, 2)
        self.assertEqual(nums, original)


class TestKthRelationship(unittest.TestCase):
    def test_relationship(self):
        nums = [3, 2, 1, 5, 6, 4]
        n = len(nums)
        k = 2
        
        kth_largest = find_kth_largest(nums, k)
        # k-th largest is (n-k+1)-th smallest
        kth_smallest = find_kth_smallest(nums, n - k + 1)
        
        self.assertEqual(kth_largest, kth_smallest)
    
    def test_relationship_multiple_k(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        n = len(nums)
        
        for k in range(1, n + 1):
            kth_largest = find_kth_largest(nums, k)
            kth_smallest = find_kth_smallest(nums, n - k + 1)
            self.assertEqual(kth_largest, kth_smallest, 
                           f"Failed for k={k}: largest={kth_largest}, smallest={kth_smallest}")


class TestPerformance(unittest.TestCase):
    def test_large_random_array(self):
        size = 10000
        nums = [random.randint(1, size * 10) for _ in range(size)]
        k = size // 2
        
        result = find_kth_largest(nums, k)
        
        sorted_nums = sorted(nums, reverse=True)
        expected = sorted_nums[k - 1]
        self.assertEqual(result, expected)
    
    def test_worst_case_sorted(self):
        nums = list(range(1000))
        result = find_kth_largest(nums, 500)
        
        self.assertEqual(result, 500)
    
    def test_many_duplicates(self):
        nums = [random.randint(1, 10) for _ in range(1000)]
        k = 500
        
        result = find_kth_largest(nums, k)
        
        sorted_nums = sorted(nums, reverse=True)
        expected = sorted_nums[k - 1]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

