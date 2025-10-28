from __future__ import annotations

from collections.abc import Iterable
from typing import List, TypeVar

from homework_5.tracer import trace_recursion


T = TypeVar("T")


@trace_recursion
def permute(nums: Iterable[T]) -> List[List[T]]:
    items = list(nums)
    result: List[List[T]] = []

    @trace_recursion
    def backtrack(path: List[T], used: List[bool]) -> None:
        if len(path) == len(items):
            result.append(path.copy())
            return

        for index, value in enumerate(items):
            if not used[index]:
                used[index] = True
                path.append(value)
                backtrack(path, used)
                path.pop()
                used[index] = False

    if not items:
        return [[]]

    used_flags = [False] * len(items)
    backtrack([], used_flags)
    return result

