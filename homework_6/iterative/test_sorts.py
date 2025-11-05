import random
import unittest

from homework_6.iterative.sorts import mergesort_iterative, quicksort_iterative


class TestIterativeMergeSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(mergesort_iterative([]), [])
    
    def test_single(self):
        self.assertEqual(mergesort_iterative([1]), [1])
    
    def test_two_elements_sorted(self):
        self.assertEqual(mergesort_iterative([1, 2]), [1, 2])
    
    def test_two_elements_unsorted(self):
        self.assertEqual(mergesort_iterative([2, 1]), [1, 2])
    
    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort_iterative(arr), [1, 2, 3, 4, 5])
    
    def test_reverse(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(mergesort_iterative(arr), [1, 2, 3, 4, 5])
    
    def test_random(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        self.assertEqual(mergesort_iterative(arr), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_duplicates(self):
        arr = [3, 1, 2, 1, 3, 2]
        self.assertEqual(mergesort_iterative(arr), [1, 1, 2, 2, 3, 3])
    
    def test_all_same(self):
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(mergesort_iterative(arr), [5, 5, 5, 5, 5])
    
    def test_negative_numbers(self):
        arr = [3, -1, 4, -2, 0, 2]
        self.assertEqual(mergesort_iterative(arr), [-2, -1, 0, 2, 3, 4])
    
    def test_large_random(self):
        arr = [random.randint(-100, 100) for _ in range(100)]
        result = mergesort_iterative(arr)
        self.assertEqual(result, sorted(arr))
    
    def test_does_not_modify_original(self):
        arr = [3, 1, 2]
        original = arr.copy()
        mergesort_iterative(arr)
        self.assertEqual(arr, original)


class TestIterativeQuickSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quicksort_iterative([]), [])
    
    def test_single(self):
        self.assertEqual(quicksort_iterative([1]), [1])
    
    def test_two_elements_sorted(self):
        self.assertEqual(quicksort_iterative([1, 2]), [1, 2])
    
    def test_two_elements_unsorted(self):
        self.assertEqual(quicksort_iterative([2, 1]), [1, 2])
    
    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort_iterative(arr), [1, 2, 3, 4, 5])
    
    def test_reverse(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quicksort_iterative(arr), [1, 2, 3, 4, 5])
    
    def test_random(self):
        arr = [3, 7, 1, 9, 2, 5, 8, 4, 6]
        self.assertEqual(quicksort_iterative(arr), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_duplicates(self):
        arr = [3, 1, 2, 1, 3, 2]
        self.assertEqual(quicksort_iterative(arr), [1, 1, 2, 2, 3, 3])
    
    def test_all_same(self):
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(quicksort_iterative(arr), [5, 5, 5, 5, 5])
    
    def test_negative_numbers(self):
        arr = [3, -1, 4, -2, 0, 2]
        self.assertEqual(quicksort_iterative(arr), [-2, -1, 0, 2, 3, 4])
    
    def test_large_random(self):
        arr = [random.randint(-100, 100) for _ in range(100)]
        result = quicksort_iterative(arr)
        self.assertEqual(result, sorted(arr))
    
    def test_does_not_modify_original(self):
        arr = [3, 1, 2]
        original = arr.copy()
        quicksort_iterative(arr)
        self.assertEqual(arr, original)


class TestIterativeComparison(unittest.TestCase):
    def test_same_output_on_random(self):
        arr = [random.randint(1, 100) for _ in range(50)]
        merge_result = mergesort_iterative(arr)
        quick_result = quicksort_iterative(arr)
        self.assertEqual(merge_result, quick_result)
    
    def test_same_output_on_sorted(self):
        arr = list(range(50))
        merge_result = mergesort_iterative(arr)
        quick_result = quicksort_iterative(arr)
        self.assertEqual(merge_result, quick_result)
    
    def test_same_output_on_reverse(self):
        arr = list(range(50, 0, -1))
        merge_result = mergesort_iterative(arr)
        quick_result = quicksort_iterative(arr)
        self.assertEqual(merge_result, quick_result)
    
    def test_same_output_on_duplicates(self):
        arr = [random.randint(1, 5) for _ in range(50)]
        merge_result = mergesort_iterative(arr)
        quick_result = quicksort_iterative(arr)
        self.assertEqual(merge_result, quick_result)


if __name__ == "__main__":
    unittest.main()

