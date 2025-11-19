"""Binary Search Tree starter code.

BST property: left subtree values < node.value < right subtree values (no duplicates stored; ignore inserts of existing value).

Methods:
- insert(value: int) -> None
- search(value: int) -> bool
- delete(value: int) -> bool           Return True if a node was removed.
    Cases: leaf, one child, two children (replace with inorder successor).
- inorder() -> list[int]               Return sorted values.
- height() -> int                      Height of tree (empty = 0, single node = 1).
- is_balanced() -> bool                For every node, |height(left) - height(right)| <= 1.
- find_min() -> int | None             Minimum value.
- find_max() -> int | None             Maximum value.

Implement iteratively or recursively. Keep code readable.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

BSTNodeT = Optional['_BSTNode']


@dataclass
class _BSTNode:
    value: int
    left: BSTNodeT = None
    right: BSTNodeT = None


class BinarySearchTree:
    _root: BSTNodeT

    def __init__(self: 'BinarySearchTree') -> None:
        self._root: BSTNodeT = None

    def insert(self: 'BinarySearchTree', value: int) -> None:
        pass  # TODO: implement

    def search(self: 'BinarySearchTree', value: int) -> bool:  # type: ignore
        pass  # TODO: implement

    def inorder(self: 'BinarySearchTree') -> List[int]:  # type: ignore
        pass  # TODO: implement

    def height(self: 'BinarySearchTree') -> int:  # type: ignore
        pass  # TODO: implement

    def is_balanced(self: 'BinarySearchTree') -> bool:  # type: ignore
        pass  # TODO: implement

    def find_min(self: 'BinarySearchTree') -> Optional[int]:  # type: ignore
        pass  # TODO: implement

    def find_max(self: 'BinarySearchTree') -> Optional[int]:  # type: ignore
        pass  # TODO: implement

    def delete(self: 'BinarySearchTree', value: int) -> bool:  # type: ignore
        pass  # TODO: implement
