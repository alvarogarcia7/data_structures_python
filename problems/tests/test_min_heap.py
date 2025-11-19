import abc
from abc import ABCMeta
import pytest
from solutions.min_heap import MinHeap

class TestMinHeapContract(metaclass=ABCMeta):
    def test_build_heap_and_peek(self) -> None:
        h = self.instance([5,3,8,1,2])
        assert h.peek() == 1

    def test_push_and_pop_sequence(self) -> None:
        h = self.instance()
        for v in [5,1,3,1,2]:
            h.push(v)
        out = [h.pop() for _ in range(len(h))]
        assert out == [1,1,2,3,5]

    def test_pop_empty_raises(self) -> None:
        h = self.instance()
        with pytest.raises(IndexError):
            h.pop()

    def test_peek_empty_raises(self) -> None:
        h = self.instance()
        with pytest.raises(IndexError):
            h.peek()

    def test_replace_root(self) -> None:
        h = self.instance([4,5,6])
        old = h.replace_root(10)
        assert old == 4
        assert h.peek() == 5

    @abc.abstractmethod
    def instance(self, *args, **kwargs) -> MinHeap:
        pass

@pytest.mark.xfail(reason="Not implemented yet")
class TestMinHeap(TestMinHeapContract):
    def instance(self, *args, **kwargs) -> MinHeap:
        return MinHeap(*args, **kwargs)
