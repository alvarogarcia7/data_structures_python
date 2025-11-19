"""Singly Linked List starter code.

Implement a singly linked list supporting these operations:

Methods to implement:
- insert_head(value: int) -> None        O(1)
- append(value: int) -> None             O(n) (no tail pointer) or O(1) if you add tail storage (optional)
- delete(value: int) -> bool             O(n)  Return True if a node was deleted.
- reverse() -> None                      O(n)  In-place reversal.
- find_middle() -> int | None            O(n)  Use slow/fast pointer. For even length return FIRST (left) middle.
- to_list() -> list[int]                 O(n)
- __len__() -> int                       O(1) if you track size, else O(n). (Track size here.)

Edge cases: empty list, single element, delete head/tail, reverse empty/single.

Do NOT modify the public method signatures. Replace pass bodies with working code when implementing.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Iterator


@dataclass
class _Node:
    value: int
    next: Optional["_Node"] = None


class LinkedList:
    def __init__(self) -> None:
        self._head: Optional[_Node] = None
        self._size: int = 0

    def insert_head(self, value: int) -> None:
        """Insert new value at the head."""
        pass  # TODO: implement

    def append(self, value: int) -> None:
        """Append value at the end."""
        pass  # TODO: implement

    def delete(self, value: int) -> bool:  # type: ignore
        """Delete first occurrence of value. Return True if deleted."""
        pass  # TODO: implement

    def reverse(self) -> None:  # type: ignore
        """Reverse the list in-place."""
        pass  # TODO: implement

    def find_middle(self) -> Optional[int]:  # type: ignore
        """Return the middle element's value. For even length L, return element at index (L//2 - 1)."""
        pass  # TODO: implement

    def to_list(self) -> list[int]:  # type: ignore
        """Return Python list of values."""
        pass  # TODO: implement

    def __len__(self) -> int:  # pragma: no cover - trivial
        return self._size

    def __iter__(self) -> Iterator[int]:  # optional helper
        cur = self._head
        while cur:
            yield cur.value
            cur = cur.next

def test_find_middle_empty() -> None:
    ll: LinkedList = LinkedList()
    assert ll.find_middle() is None

def test_insert_head_and_to_list() -> None:
    ll: LinkedList = LinkedList()
    ll.insert_head(3)
    ll.insert_head(2)
    ll.insert_head(1)
    assert ll.to_list() == [1, 2, 3]

def test_append() -> None:
    ll: LinkedList = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_delete_head_and_middle() -> None:
    ll: LinkedList = LinkedList()
    for v in [1, 2, 3, 4]:
        ll.append(v)
    assert ll.delete(1) is True
    assert ll.to_list() == [2, 3, 4]
    assert ll.delete(3) is True
    assert ll.to_list() == [2, 4]
    assert ll.delete(42) is False

def test_reverse_cases() -> None:
    ll: LinkedList = LinkedList()
    assert ll.to_list() == []
    ll.reverse()  # reverse empty
    ll.append(1)
    ll.reverse()  # reverse single
    assert ll.to_list() == [1]
    for v in [2, 3, 4]:
        ll.append(v)
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]

def test_find_middle_even_and_odd() -> None:
    ll: LinkedList = LinkedList()
    for v in [10, 20, 30, 40, 50]:
        ll.append(v)
    assert ll.find_middle() == 30  # odd length
    ll.append(60)
    # even length -> left middle (index len//2 - 1) -> index 2 -> 30
    assert ll.find_middle() == 30
