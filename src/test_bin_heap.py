"""Functions that test methods of MaxHeap class."""
from bin_heap import MaxHeap


def test_empty_bin_heap():
    """Test that an empty MaxHeap has len(0)."""
    m = MaxHeap()
    assert len(m) == 0


def test_pop_from_empty_heap():
    """Test that you can't pop from empty heap."""
    m = MaxHeap()
    with IndexError:
        assert m.pop()


def test_push_to_heap():
    """Test that the push method is functional."""
    m = MaxHeap()
    m.push(1)
    m.push(2)
    m.push(3)
    m.push(4)
    m.push(30)
    assert m.heap == [30, 4, 2, 1, 3]


def test_pop_from_populated_heap():
    """Test pop from populated heap."""
    m = MaxHeap()
    m.push(7)
    m.push(30)
    m.push(10)
    m.push(20)
    assert m.pop() == 30


def test_pop_multiple_times():
    """Test pop method multiple times in a row."""
    m = MaxHeap()
    m.push(7)
    m.push(30)
    m.push(10)
    m.push(20)
    m.pop()
    m.pop()
    assert m.pop()
