from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def mergesort_iterative(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr
    
    result = arr.copy()
    n = len(result)
    
    current_size = 1
    while current_size < n:
        left_start = 0
        while left_start < n:
            left_end = min(left_start + current_size - 1, n - 1)
            right_end = min(left_start + current_size * 2 - 1, n - 1)
            
            if left_end < right_end:
                _merge_inplace(result, left_start, left_end, right_end)
            
            left_start += current_size * 2
        
        current_size *= 2
    
    return result


def _merge_inplace(arr: List[T], left_start: int, left_end: int, right_end: int) -> None:
    left = arr[left_start:left_end + 1]
    right = arr[left_end + 1:right_end + 1]
    
    i = j = 0
    k = left_start
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def quicksort_iterative(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr
    
    result = arr.copy()
    n = len(result)
    
    stack = [(0, n - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_idx = _partition(result, low, high)
            
            if pivot_idx - low > high - pivot_idx:
                stack.append((low, pivot_idx - 1))
                stack.append((pivot_idx + 1, high))
            else:
                stack.append((pivot_idx + 1, high))
                stack.append((low, pivot_idx - 1))
    
    return result


def _partition(arr: List[T], low: int, high: int) -> int:
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

