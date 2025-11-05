from __future__ import annotations

import random
from typing import List, TypeVar

T = TypeVar("T")


def find_kth_largest(nums: List[T], k: int) -> T:
    if not nums or k < 1 or k > len(nums):
        raise ValueError(f"Invalid k={k} for array of length {len(nums)}")
    
    arr = nums.copy()
    n = len(arr)
    target_idx = n - k
    
    return _quickselect(arr, 0, n - 1, target_idx)


def _quickselect(arr: List[T], left: int, right: int, target_idx: int) -> T:
    if left == right:
        return arr[left]
    
    pivot_idx = _randomized_partition(arr, left, right)
    
    if target_idx == pivot_idx:
        return arr[target_idx]
    elif target_idx < pivot_idx:
        return _quickselect(arr, left, pivot_idx - 1, target_idx)
    else:
        return _quickselect(arr, pivot_idx + 1, right, target_idx)


def _randomized_partition(arr: List[T], left: int, right: int) -> int:
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    
    return _partition(arr, left, right)


def _partition(arr: List[T], left: int, right: int) -> int:
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def find_kth_smallest(nums: List[T], k: int) -> T:
    if not nums or k < 1 or k > len(nums):
        raise ValueError(f"Invalid k={k} for array of length {len(nums)}")
    
    arr = nums.copy()
    target_idx = k - 1
    
    return _quickselect(arr, 0, len(arr) - 1, target_idx)

