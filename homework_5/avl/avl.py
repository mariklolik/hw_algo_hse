from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, Iterable, Iterator, Optional, TypeVar


T = TypeVar("T")


@dataclass(slots=True)
class _Node(Generic[T]):
    key: T
    left: Optional["_Node[T]"] = None
    right: Optional["_Node[T]"] = None
    height: int = 1


def _height(node: Optional[_Node[T]]) -> int:
    return node.height if node else 0


def _update_height(node: _Node[T]) -> None:
    node.height = max(_height(node.left), _height(node.right)) + 1


def _balance_factor(node: Optional[_Node[T]]) -> int:
    if node is None:
        return 0
    return _height(node.left) - _height(node.right)


def _rotate_right(y: _Node[T]) -> _Node[T]:
    x = y.left
    if x is None:
        return y
    t2 = x.right

    x.right = y
    y.left = t2

    _update_height(y)
    _update_height(x)
    return x


def _rotate_left(x: _Node[T]) -> _Node[T]:
    y = x.right
    if y is None:
        return x
    t2 = y.left

    y.left = x
    x.right = t2

    _update_height(x)
    _update_height(y)
    return y


def _rebalance(node: _Node[T]) -> _Node[T]:
    _update_height(node)
    balance = _balance_factor(node)

    if balance > 1:
        if _balance_factor(node.left) < 0 and node.left is not None:
            node.left = _rotate_left(node.left)
        return _rotate_right(node)

    if balance < -1:
        if _balance_factor(node.right) > 0 and node.right is not None:
            node.right = _rotate_right(node.right)
        return _rotate_left(node)

    return node


class AVLTree(Generic[T]):
    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_Node[T]] = None
        if values is not None:
            for value in values:
                self.insert(value)

    def __contains__(self, key: T) -> bool:
        return self.search(key)

    def __iter__(self) -> Iterator[T]:
        if self._root is None:
            return iter(())
        stack = []
        current = self._root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            yield current.key
            current = current.right

    @property
    def height(self) -> int:
        return _height(self._root)

    def insert(self, key: T) -> None:
        self._root = self._insert(self._root, key)

    def _insert(self, node: Optional[_Node[T]], key: T) -> _Node[T]:
        if node is None:
            return _Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        return _rebalance(node)

    def delete(self, key: T) -> None:
        self._root = self._delete(self._root, key)

    def _delete(self, node: Optional[_Node[T]], key: T) -> Optional[_Node[T]]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        if node is None:
            return None

        return _rebalance(node)

    def search(self, key: T) -> bool:
        current = self._root
        while current:
            if key == current.key:
                return True
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def clear(self) -> None:
        self._root = None

    def to_list(self) -> list[T]:
        return list(self)

    def is_empty(self) -> bool:
        return self._root is None

