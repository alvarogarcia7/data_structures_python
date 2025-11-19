import pytest

from solutions.binary_search_tree import BinarySearchTree
from problems.tests.test_binary_search_tree import TestBinarySearchTreeContract


@pytest.mark.xfail(reason="Not implemented yet")
class TestBinarySearchTreeSolution(TestBinarySearchTreeContract):
    def instance(self) -> BinarySearchTree:
        from solutions.binary_search_tree import BinarySearchTree

        return BinarySearchTree()
