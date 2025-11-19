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


def test_insert_and_inorder_sorted() -> None:
    bst = BinarySearchTree()
    for v in [7, 3, 9, 1, 5, 8, 10]:
        bst.insert(v)
    assert bst.inorder() == [1, 3, 5, 7, 8, 9, 10]

def test_search_existing_and_missing() -> None:
    bst = BinarySearchTree()
    for v in [4, 2, 6]:
        bst.insert(v)
    assert bst.search(2) is True
    assert bst.search(5) is False

def test_height_and_balance() -> None:
    bst = BinarySearchTree()
    for v in [5, 3, 8, 2, 4, 7, 9]:
        bst.insert(v)
    assert bst.height() == 3
    assert bst.is_balanced() is True
    bst.insert(1)
    bst.insert(0)
    assert bst.is_balanced() is False

def test_find_min_max() -> None:
    bst = BinarySearchTree()
    for v in [5, 3, 8, 2, 4, 7, 9]:
        bst.insert(v)
    assert bst.find_min() == 2
    assert bst.find_max() == 9

test_insert_and_inorder_sorted()
test_search_existing_and_missing()
test_height_and_balance()
test_find_min_max()
