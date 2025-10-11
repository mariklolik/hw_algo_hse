from typing import List

def two_sum(arr: List[int], k: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(arr):
        complement = k - num
        if complement in num_map:
            return sorted([num_map[complement], i])
        num_map[num] = i
    return []
