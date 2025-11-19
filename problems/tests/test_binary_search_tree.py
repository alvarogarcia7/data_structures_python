import abc
from abc import ABCMeta

import pytest

from solutions.binary_search_tree import BinarySearchTree


class TestBinarySearchTreeContract(metaclass=ABCMeta):
    def test_insert_and_inorder_sorted(self) -> None:
        bst = self.instance()
        for v in [7, 3, 9, 1, 5, 8, 10]:
            bst.insert(v)
        assert bst.inorder() == [1, 3, 5, 7, 8, 9, 10]

    def test_search_existing_and_missing(self) -> None:
        bst = self.instance()
        for v in [4, 2, 6]:
            bst.insert(v)
        assert bst.search(2) is True
        assert bst.search(5) is False

    def test_height_and_balance(self) -> None:
        bst = self.instance()
        for v in [5, 3, 8, 2, 4, 7, 9]:
            bst.insert(v)
        assert bst.height() == 3
        assert bst.is_balanced() is True
        bst.insert(1)
        bst.insert(0)
        assert bst.is_balanced() is False

    def test_find_min_max(self) -> None:
        bst = self.instance()
        for v in [5, 3, 8, 2, 4, 7, 9]:
            bst.insert(v)
        assert bst.find_min() == 2
        assert bst.find_max() == 9

    @abc.abstractmethod
    def instance(self) -> BinarySearchTree:
        pass


@pytest.mark.xfail(reason="Not implemented yet")
class TestBinarySearchTree(TestBinarySearchTreeContract):
    def instance(self) -> BinarySearchTree:
        return BinarySearchTree()
