import random
import unittest

from homework_6.compare.sorts import mergesort, quicksort
from homework_6.compare.timer import measure_time


class TestRecursiveSorts(unittest.TestCase):
    def test_mergesort_empty(self):
        self.assertEqual(mergesort([]), [])
    
    def test_mergesort_single(self):
        self.assertEqual(mergesort([1]), [1])
    
    def test_mergesort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort(arr), [1, 2, 3, 4, 5])
    
    def test_mergesort_reverse(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(mergesort(arr), [1, 2, 3, 4, 5])
    
    def test_mergesort_random(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        self.assertEqual(mergesort(arr), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_mergesort_duplicates(self):
        arr = [3, 1, 2, 1, 3, 2]
        self.assertEqual(mergesort(arr), [1, 1, 2, 2, 3, 3])
    
    def test_quicksort_empty(self):
        self.assertEqual(quicksort([]), [])
    
    def test_quicksort_single(self):
        self.assertEqual(quicksort([1]), [1])
    
    def test_quicksort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5])
    
    def test_quicksort_reverse(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5])
    
    def test_quicksort_random(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_quicksort_duplicates(self):
        arr = [3, 1, 2, 1, 3, 2]
        self.assertEqual(quicksort(arr), [1, 1, 2, 2, 3, 3])


class TestTimingComparison(unittest.TestCase):
    def test_timing_on_sorted_data(self):
        size = 1000
        arr = list(range(size))
        
        print("\n=== Sorted data ===")
        mergesort_timed = measure_time(mergesort)
        quicksort_timed = measure_time(quicksort)
        
        result_merge = mergesort_timed(arr.copy())
        result_quick = quicksort_timed(arr.copy())
        
        self.assertEqual(result_merge, sorted(arr))
        self.assertEqual(result_quick, sorted(arr))
    
    def test_timing_on_reverse_sorted(self):
        size = 1000
        arr = list(range(size, 0, -1))
        
        print("\n=== Reverse sorted data ===")
        mergesort_timed = measure_time(mergesort)
        quicksort_timed = measure_time(quicksort)
        
        result_merge = mergesort_timed(arr.copy())
        result_quick = quicksort_timed(arr.copy())
        
        self.assertEqual(result_merge, sorted(arr))
        self.assertEqual(result_quick, sorted(arr))
    
    def test_timing_on_many_duplicates(self):
        size = 1000
        arr = [random.randint(1, 10) for _ in range(size)]
        
        print("\n=== Many duplicates (values 1-10 only) ===")
        mergesort_timed = measure_time(mergesort)
        quicksort_timed = measure_time(quicksort)
        
        result_merge = mergesort_timed(arr.copy())
        result_quick = quicksort_timed(arr.copy())
        
        self.assertEqual(result_merge, sorted(arr))
        self.assertEqual(result_quick, sorted(arr))
    
    def test_timing_on_random_data(self):
        size = 1000
        arr = random.sample(range(size * 10), size)
        
        print("\n=== Random data ===")
        mergesort_timed = measure_time(mergesort)
        quicksort_timed = measure_time(quicksort)
        
        result_merge = mergesort_timed(arr.copy())
        result_quick = quicksort_timed(arr.copy())
        
        self.assertEqual(result_merge, sorted(arr))
        self.assertEqual(result_quick, sorted(arr))
    
    def test_timing_on_nearly_sorted(self):
        size = 1000
        arr = list(range(size))
        for _ in range(10):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        
        print("\n=== Nearly sorted data ===")
        mergesort_timed = measure_time(mergesort)
        quicksort_timed = measure_time(quicksort)
        
        result_merge = mergesort_timed(arr.copy())
        result_quick = quicksort_timed(arr.copy())
        
        self.assertEqual(result_merge, sorted(arr))
        self.assertEqual(result_quick, sorted(arr))
    
    def test_large_dataset_comparison(self):
        size = 5000
        arr = [random.randint(1, size) for _ in range(size)]
        
        print("\n=== Large random dataset (5000 elements) ===")
        mergesort_timed = measure_time(mergesort)
        quicksort_timed = measure_time(quicksort)
        
        result_merge = mergesort_timed(arr.copy())
        result_quick = quicksort_timed(arr.copy())
        
        self.assertEqual(result_merge, sorted(arr))
        self.assertEqual(result_quick, sorted(arr))


if __name__ == "__main__":
    unittest.main()

