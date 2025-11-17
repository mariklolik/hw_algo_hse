from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def makeheap_n_log_n(arr: List[T]) -> List[T]:
    heap = []
    for elem in arr:
        heap.append(elem)
        _sift_up(heap, len(heap) - 1)
    return heap


def makeheap(arr: List[T]) -> List[T]:
    heap = arr.copy()
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(heap, i, n)
    return heap


def _sift_up(heap: List[T], idx: int) -> None:
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break


def _sift_down(heap: List[T], idx: int, size: int) -> None:
    while True:
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        if left < size and heap[left] < heap[smallest]:
            smallest = left
        if right < size and heap[right] < heap[smallest]:
            smallest = right
        
        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break


def is_minheap(arr: List[T]) -> bool:
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

