"""Functions that test methods of MaxHeap class."""
import pytest
from bin_heap import MaxHeap


@pytest.fixture
def empty_max_heap():
    """Create an empty MaxHeap."""
    return MaxHeap()


def test_heap_empty_upon_init(empty_max_heap):
    """Function to test heap is empty list upon init."""
    m = empty_max_heap
    assert len(m.heap) == 0
    assert isinstance(m.heap, list)


def test_push_method_inserts_node_containing_val_at_head(empty_max_heap):
    """Function to test push method adds new value to heap."""
    m = empty_max_heap
    m.push(1)
    assert m.heap[0] == 1


def test_heap_unpacks_iterable_upon_init():
    """Function to test optional iterable enters into heap list upon init."""
    m = MaxHeap([1, 2, 3])
    assert m.heap[0] == 3
    assert m.heap[1] == 2
    assert m.heap[2] == 1


def test_heap_pop_method_removes_and_returns_value_at_heap_head(empty_max_heap):
    """Function to test if pop method remove and return head value of heap."""
    m = empty_max_heap
    m.push(1)
    assert m.pop() == 1
    assert len(m.heap) == 0


def test_heap_maintains_max_heap_when_values_are_pushed_in(empty_max_heap):
    """Function to test if heap maintains max when multiple values are pushed
    in."""
    m = empty_max_heap
    m.push(1)
    m.push(2)
    m.push(3)
    m.push(500)
    m.push(4)
    assert m.heap[0] == 500
    assert m.heap[1] == 4
    assert m.heap[2] == 1
    assert m.heap[3] == 2
    assert m.heap[4] == 3


def test_heap_maintains_max_heap_when_values_are_popped_out(empty_max_heap):
    """Function to test if heap maintatins max when pop method removes head value
    from heap."""
    m = empty_max_heap
    m.push(1)
    m.push(2)
    m.push(3)
    m.push(500)
    m.push(4)
    m.push(5)
    m.pop()
    assert m.heap[0] == 5
    assert m.heap[1] == 4
    assert m.heap[2] == 2
    assert m.heap[3] == 3
    assert m.heap[4] == 1
