"""Min Heap starter code (array-backed binary heap).

Represent the heap as a list where for index i:
- left child = 2*i + 1
- right child = 2*i + 2
- parent = (i - 1) // 2

Methods:
- __init__(values: list[int] | None = None)
- push(value: int) -> None              O(log n)
- peek() -> int                         O(1) raise IndexError if empty
- pop() -> int                          O(log n) remove and return smallest
- build_heap(values: list[int]) -> None O(n)
- replace_root(value: int) -> int       O(log n) return old root, insert new value at root and heapify down
- __len__() -> int                      O(1)

Helper (private) methods (implement):
- _heapify_up(i: int)
- _heapify_down(i: int)

Edge cases: empty pop/peek, duplicates, building from empty list.
"""
from __future__ import annotations
from typing import Optional, List

class MinHeap:
    _data: List[int]

    def __init__(self: 'MinHeap', values: Optional[List[int]] = None) -> None:
        self._data: List[int] = []
        if values:
            self.build_heap(values)

    def push(self: 'MinHeap', value: int) -> None: # type: ignore
        pass  # TODO: implement

    def peek(self: 'MinHeap') -> int: # type: ignore
        pass  # TODO: implement

    def pop(self: 'MinHeap') -> int: # type: ignore
        pass  # TODO: implement

    def build_heap(self: 'MinHeap', values: List[int]) -> None:
        pass  # TODO: implement

    def replace_root(self: 'MinHeap', value: int) -> int: # type: ignore
        pass  # TODO: implement

    def _heapify_up(self: 'MinHeap', index: int) -> None: # type: ignore
        pass  # TODO: implement

    def _heapify_down(self: 'MinHeap', index: int) -> None: # type: ignore
        pass  # TODO: implement

    def __len__(self: 'MinHeap') -> int:  # pragma: no cover - trivial
        return len(self._data)
