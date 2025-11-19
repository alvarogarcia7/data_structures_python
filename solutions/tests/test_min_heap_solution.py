import pytest

from solutions.min_heap import MinHeap
from problems.tests.test_min_heap import TestMinHeapContract

@pytest.mark.xfail(reason="Not implemented yet")
class TestMinHeapSolution(TestMinHeapContract):
    def instance(self, *args, **kwargs) -> MinHeap:
        from solutions.min_heap import MinHeap as SolutionMinHeap
        return SolutionMinHeap(*args, **kwargs)

