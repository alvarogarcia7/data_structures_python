import abc
from abc import ABCMeta

import pytest

from solutions.linked_list import LinkedList


class TestLinkedListContract(metaclass=ABCMeta):

    def test_find_middle_empty(self) -> None:
        ll: LinkedList = LinkedList()
        assert ll.find_middle() is None

    def test_insert_head_and_to_list(self) -> None:
        ll: LinkedList = self.instance()
        ll.insert_head(3)
        ll.insert_head(2)
        ll.insert_head(1)
        assert ll.to_list() == [1, 2, 3]

    def test_append(self) -> None:
        ll: LinkedList = self.instance()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]

    def test_delete_head_and_middle(self) -> None:
        ll: LinkedList = self.instance()
        for v in [1, 2, 3, 4]:
            ll.append(v)
        assert ll.delete(1) is True
        assert ll.to_list() == [2, 3, 4]
        assert ll.delete(3) is True
        assert ll.to_list() == [2, 4]
        assert ll.delete(42) is False

    def test_reverse_cases(self) -> None:
        ll: LinkedList = self.instance()
        assert ll.to_list() == []
        ll.reverse()  # reverse empty
        ll.append(1)
        ll.reverse()  # reverse single
        assert ll.to_list() == [1]
        for v in [2, 3, 4]:
            ll.append(v)
        ll.reverse()
        assert ll.to_list() == [4, 3, 2, 1]

    def test_find_middle_even_and_odd(self) -> None:
        ll: LinkedList = self.instance()
        for v in [10, 20, 30, 40, 50]:
            ll.append(v)
        assert ll.find_middle() == 30  # odd length
        ll.append(60)
        # even length -> left middle (index len//2 - 1) -> index 2 -> 30
        assert ll.find_middle() == 30

    @abc.abstractmethod
    def instance(self) -> LinkedList:
        pass


@pytest.mark.xfail(reason="Not implemented yet")
class TestLinkedList(TestLinkedListContract):
    def instance(self) -> LinkedList:
        return LinkedList()
