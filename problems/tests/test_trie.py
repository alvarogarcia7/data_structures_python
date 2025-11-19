import abc
from abc import ABCMeta
import pytest
from solutions.trie import Trie

class TestTrieContract(metaclass=ABCMeta):
    def test_insert_and_contains(self) -> None:
        t = self.instance()
        t.insert("app")
        t.insert("apple")
        t.insert("apt")
        assert t.contains("app") is True
        assert t.contains("apple") is True
        assert t.contains("ap") is False  # prefix but not word

    def test_starts_with_prefix_results_sorted(self) -> None:
        t = self.instance()
        for w in ["app","apple","application","apt","bat","batch","bath"]:
            t.insert(w)
        assert t.starts_with("app") == ["app","apple","application"]
        assert t.starts_with("ba") == ["bat","batch","bath"]
        assert t.starts_with("zzz") == []

    def test_find_by_keyword_alias(self) -> None:
        t = self.instance()
        for w in ["car","cart","carbon","care"]:
            t.insert(w)
        assert t.find_by_keyword("car") == ["car","carbon","care","cart"]  # sorted lexicographically

    def test_list_regex(self) -> None:
        t = self.instance()
        words = ["action","atom","axis","ask","bat","batch","bath","", "aaaardvark"]
        for w in words:
            t.insert(w)
        assert t.list_regex(r"^a.*") == ["aaaardvark","action","ask","atom","axis"]
        assert t.list_regex(r".*tion$") == ["action"]
        assert t.list_regex(r"^[aeiou]{2}.*") == ['aaaardvark']  # no other word begins with 2 vowels
        assert t.list_regex(r"^$") == [""]  # empty word

    @abc.abstractmethod
    def instance(self) -> Trie:
        pass

@pytest.mark.xfail(reason="Not implemented yet")
class TestTrie(TestTrieContract):
    def instance(self) -> Trie:
        return Trie()
