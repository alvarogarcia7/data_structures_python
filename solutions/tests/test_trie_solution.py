import pytest

from problems.tests.test_trie import TestTrieContract
from solutions.trie import Trie


@pytest.mark.xfail(reason="Not implemented yet")
class TestTrieSolution(TestTrieContract):
    def instance(self) -> Trie:
        from solutions.trie import Trie
        return Trie()
