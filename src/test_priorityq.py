"""Functions that test Priority class methods."""
import pytest


@pytest.fixture
def new_pq():
    """Create an instance of a priority queue."""
    from priorityq import Priority
    pq = Priority()
    return pq


def test_new_priority_instance_empty_upon_init(new_pq):
    """Return value added by insert method."""
    assert new_pq.head is None
    assert new_pq.tail is None
    assert new_pq._counter == 0
    assert new_pq.priorities == []


def test_insert_method_adds_value_to_priority_queue(new_pq):
    """Return value added by insert method."""
    new_pq.insert(1)
    assert new_pq.head.data == 1


def test_insert_method_adds_value_to_end_of_pq(new_pq):
    """Return value added by insert method."""
    new_pq.insert(1)
    new_pq.insert(2)
    assert new_pq.tail.data == 2
    assert new_pq.head.data == 1
    assert new_pq.head.next_node.data == 2


def test_insert_method_adds_value_and_priority_to_node_in_pq(new_pq):
    """Return value added by insert method."""
    new_pq.insert(1, 100)
    assert new_pq.tail.data == 1
    assert new_pq.head.data == 1
    assert new_pq.head.priority == 100


def test_pop_method_removes_and_returns_value_from_head_of_pq(new_pq):
    """Delete and return value from head of priority queue."""
    new_pq.insert(1)
    assert new_pq.pop() == 1


def test_pop_method_removes_and_returns_only_head_of_pq(new_pq):
    """Delete and return value from head of priority queue."""
    new_pq.insert(1)
    new_pq.insert(2)
    new_pq.insert(3)
    assert new_pq.pop() == 1


def test_pop_method_removes_and_returns_highest_priority_of_pq(new_pq):
    """Delete and return value from head of priority queue."""
    new_pq.insert(1, 100)
    new_pq.insert(2, 99.9)
    new_pq.insert(3, 99.8)
    assert new_pq.pop() == 1


def test_pop_method_raises_exception_when_queue_is_empty(new_pq):
    """Delete and return value from head of priority queue."""
    with pytest.raises(IndexError):
        assert new_pq.pop() == 1


def test_peek_method_returns_none_if_pq_is_empty(new_pq):
    """Raise IndexError if priority queue is empty."""
    with pytest.raises(IndexError):
        assert new_pq.peek()


def test_peek_method_returns_value_of_highest_priority_item_in_pq(new_pq):
    """Return value of highest priority item in priority queue."""
    new_pq.insert(1, 100)
    new_pq.insert(2, 99.9)
    new_pq.insert(3, 99.8)
    assert new_pq.peek() == 1
