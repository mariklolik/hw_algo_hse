import random
import time
import unittest

from homework_7.makeheap.makeheap import (
    is_minheap,
    makeheap,
    makeheap_n_log_n,
)


class TestMakeheapNLogN(unittest.TestCase):
    def test_empty(self):
        result = makeheap_n_log_n([])
        self.assertEqual(result, [])
        self.assertTrue(is_minheap(result))
    
    def test_single(self):
        result = makeheap_n_log_n([5])
        self.assertEqual(result, [5])
        self.assertTrue(is_minheap(result))
    
    def test_two_elements_ordered(self):
        result = makeheap_n_log_n([1, 2])
        self.assertTrue(is_minheap(result))
        self.assertIn(result[0], [1, 2])
    
    def test_two_elements_reverse(self):
        result = makeheap_n_log_n([2, 1])
        self.assertTrue(is_minheap(result))
        self.assertEqual(result[0], 1)
    
    def test_simple_array(self):
        result = makeheap_n_log_n([3, 1, 4, 1, 5])
        self.assertTrue(is_minheap(result))
        self.assertEqual(result[0], 1)
    
    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        result = makeheap_n_log_n(arr)
        self.assertTrue(is_minheap(result))
    
    def test_sorted_descending(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        result = makeheap_n_log_n(arr)
        self.assertTrue(is_minheap(result))
    
    def test_random_array(self):
        arr = [9, 2, 7, 1, 8, 3, 6, 4, 5]
        result = makeheap_n_log_n(arr)
        self.assertTrue(is_minheap(result))
    
    def test_duplicates(self):
        arr = [3, 3, 1, 1, 2, 2]
        result = makeheap_n_log_n(arr)
        self.assertTrue(is_minheap(result))
    
    def test_large_array(self):
        arr = [random.randint(1, 1000) for _ in range(100)]
        result = makeheap_n_log_n(arr)
        self.assertTrue(is_minheap(result))
    
    def test_negative_numbers(self):
        arr = [-5, -1, -10, 3, 0, -2]
        result = makeheap_n_log_n(arr)
        self.assertTrue(is_minheap(result))
        self.assertEqual(result[0], -10)


class TestMakeheap(unittest.TestCase):
    def test_empty(self):
        result = makeheap([])
        self.assertEqual(result, [])
        self.assertTrue(is_minheap(result))
    
    def test_single(self):
        result = makeheap([5])
        self.assertEqual(result, [5])
        self.assertTrue(is_minheap(result))
    
    def test_two_elements_ordered(self):
        result = makeheap([1, 2])
        self.assertTrue(is_minheap(result))
        self.assertIn(result[0], [1, 2])
    
    def test_two_elements_reverse(self):
        result = makeheap([2, 1])
        self.assertTrue(is_minheap(result))
        self.assertEqual(result[0], 1)
    
    def test_simple_array(self):
        result = makeheap([3, 1, 4, 1, 5])
        self.assertTrue(is_minheap(result))
        self.assertEqual(result[0], 1)
    
    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        result = makeheap(arr)
        self.assertTrue(is_minheap(result))
    
    def test_sorted_descending(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        result = makeheap(arr)
        self.assertTrue(is_minheap(result))
    
    def test_random_array(self):
        arr = [9, 2, 7, 1, 8, 3, 6, 4, 5]
        result = makeheap(arr)
        self.assertTrue(is_minheap(result))
    
    def test_duplicates(self):
        arr = [3, 3, 1, 1, 2, 2]
        result = makeheap(arr)
        self.assertTrue(is_minheap(result))
    
    def test_large_array(self):
        arr = [random.randint(1, 1000) for _ in range(100)]
        result = makeheap(arr)
        self.assertTrue(is_minheap(result))
    
    def test_negative_numbers(self):
        arr = [-5, -1, -10, 3, 0, -2]
        result = makeheap(arr)
        self.assertTrue(is_minheap(result))
        self.assertEqual(result[0], -10)


class TestBothMethodsEquivalence(unittest.TestCase):
    def test_both_produce_valid_heaps(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)
        self.assertTrue(is_minheap(heap1))
        self.assertTrue(is_minheap(heap2))
    
    def test_both_have_same_min(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)
        self.assertEqual(heap1[0], heap2[0])
    
    def test_same_elements(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)
        self.assertEqual(sorted(heap1), sorted(heap2))


class TestTimingComparison(unittest.TestCase):
    def test_timing_small_array(self):
        sizes = [100, 500, 1000]
        
        print("\n=== Timing Comparison ===")
        for size in sizes:
            arr = [random.randint(1, size * 10) for _ in range(size)]
            
            arr1 = arr.copy()
            start = time.time()
            makeheap_n_log_n(arr1)
            time_nlogn = time.time() - start
            
            arr2 = arr.copy()
            start = time.time()
            makeheap(arr2)
            time_n = time.time() - start
            
            print(f"Size {size}: makeheap_n_log_n={time_nlogn:.6f}s, makeheap={time_n:.6f}s")
            
            self.assertGreater(time_nlogn, 0)
            self.assertGreater(time_n, 0)
    
    def test_timing_large_array(self):
        sizes = [5000, 10000, 20000]
        
        print("\n=== Large Array Timing ===")
        for size in sizes:
            arr = [random.randint(1, size * 10) for _ in range(size)]
            
            arr1 = arr.copy()
            start = time.time()
            makeheap_n_log_n(arr1)
            time_nlogn = time.time() - start
            
            arr2 = arr.copy()
            start = time.time()
            makeheap(arr2)
            time_n = time.time() - start
            
            ratio = time_nlogn / time_n if time_n > 0 else 0
            print(f"Size {size}: makeheap_n_log_n={time_nlogn:.6f}s, makeheap={time_n:.6f}s, ratio={ratio:.2f}x")
    
    def test_timing_sorted_data(self):
        size = 10000
        arr = list(range(size))
        
        print("\n=== Sorted Data Timing ===")
        
        arr1 = arr.copy()
        start = time.time()
        makeheap_n_log_n(arr1)
        time_nlogn = time.time() - start
        
        arr2 = arr.copy()
        start = time.time()
        makeheap(arr2)
        time_n = time.time() - start
        
        ratio = time_nlogn / time_n if time_n > 0 else 0
        print(f"Size {size}: makeheap_n_log_n={time_nlogn:.6f}s, makeheap={time_n:.6f}s, ratio={ratio:.2f}x")
    
    def test_timing_reverse_sorted(self):
        size = 10000
        arr = list(range(size, 0, -1))
        
        print("\n=== Reverse Sorted Data Timing ===")
        
        arr1 = arr.copy()
        start = time.time()
        makeheap_n_log_n(arr1)
        time_nlogn = time.time() - start
        
        arr2 = arr.copy()
        start = time.time()
        makeheap(arr2)
        time_n = time.time() - start
        
        ratio = time_nlogn / time_n if time_n > 0 else 0
        print(f"Size {size}: makeheap_n_log_n={time_nlogn:.6f}s, makeheap={time_n:.6f}s, ratio={ratio:.2f}x")


if __name__ == "__main__":
    unittest.main()

