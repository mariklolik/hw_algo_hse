from __future__ import annotations

import heapq
from typing import List, TypeVar

T = TypeVar("T")


def find_kth_largest_custom(nums: List[T], k: int) -> T:
    if not nums or k < 1 or k > len(nums):
        raise ValueError(f"Invalid k={k} for array of length {len(nums)}")
    
    heap = []
    
    for num in nums:
        if len(heap) < k:
            _heap_push(heap, num)
        elif num > heap[0]:
            _heap_pop(heap)
            _heap_push(heap, num)
    
    return heap[0]


def find_kth_largest_heapq(nums: List[T], k: int) -> T:
    if not nums or k < 1 or k > len(nums):
        raise ValueError(f"Invalid k={k} for array of length {len(nums)}")
    
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]


def _heap_push(heap: List[T], value: T) -> None:
    heap.append(value)
    _sift_up(heap, len(heap) - 1)


def _heap_pop(heap: List[T]) -> T:
    if not heap:
        raise IndexError("pop from empty heap")
    
    result = heap[0]
    last = heap.pop()
    
    if heap:
        heap[0] = last
        _sift_down(heap, 0)
    
    return result


def _sift_up(heap: List[T], idx: int) -> None:
    value = heap[idx]
    while idx > 0:
        parent = (idx - 1) // 2
        if value < heap[parent]:
            heap[idx] = heap[parent]
            idx = parent
        else:
            break
    heap[idx] = value


def _sift_down(heap: List[T], idx: int) -> None:
    n = len(heap)
    value = heap[idx]
    
    while True:
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        if left < n and heap[left] < value:
            smallest = left
        if right < n and heap[right] < (heap[smallest] if smallest == left else value):
            smallest = right
        
        if smallest != idx:
            heap[idx] = heap[smallest]
            idx = smallest
        else:
            break
    
    heap[idx] = value

