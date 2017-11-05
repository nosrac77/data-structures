"""Functions that test methods of MaxHeap class."""
from bin_heap import MaxHeap


def test_empty_bin_heap():
    """Test that an empty MaxHeap has len(0)."""
    m = MaxHeap()
    assert len(m.heap) == 0


def test_pop_from_empty_heap():
    """Test that you can't pop from empty heap."""
    m = MaxHeap()
    try:
        m.pop()
    except IndexError:
        pass


def test_push_to_heap():
    """Test that the push method is functional."""
    m = MaxHeap()
    m.push(1)
    m.push(2)
    m.push(3)
    m.push(4)
    m.push(30)
    assert m.heap == [30, 4, 2, 1, 3]


def test_find_children_returns_tuple_of_correct_values_given_parent_value_idx():
    """Test that the push method is functional."""
    m = MaxHeap()
    m.push(20)
    m.push(15)
    m.push(14)
    assert m.heap[0] == 20
    assert m.find_children(0) == (15, 14)
    m.push(10)
    m.push(9)
    assert m.heap[1] == 15
    assert m.find_children(1) == (10, 9)


def test_find_parent_returns_idx_of_correct_parent():
    """Test that the push method is functional."""
    m = MaxHeap()
    m.push(20)
    m.push(15)
    m.push(14)
    parent_correct_idx = m.heap.index(20)
    assert parent_correct_idx == 0
    assert m.heap[parent_correct_idx] == 20
    assert m.find_children(parent_correct_idx) == (15, 14)
    assert m.heap[1] == 15
    assert m.find_parent(1) == parent_correct_idx
    m.push(10)
    m.push(9)
    second_parent_correct_idx = m.heap.index(15)
    assert second_parent_correct_idx == 1
    assert m.heap[second_parent_correct_idx] == 15
    assert m.find_children(second_parent_correct_idx) == (10, 9)
    assert m.heap[4] == 9
    assert m.find_parent(4) == second_parent_correct_idx


def test_pop_from_populated_heap():
    """Test pop from populated heap."""
    m = MaxHeap()
    m.push(7)
    m.push(30)
    m.push(10)
    m.push(20)
    assert m.pop() == 30


def test_push_swaps_head_val_if_new_children_vals_greater_than_head_val():
    """Test push method swaps places with head value if head values children
    are greater than head value."""
    m = MaxHeap()
    m.push(7)
    assert m.heap == [7]
    m.push(30)
    assert m.heap == [30, 7]
    m.push(50)
    assert m.heap == [50, 7, 30]


def test_heap_maintains_max_through_multiple_pushes():
    """Test push method maintains max heap property when used multiple times."""
    m = MaxHeap()
    m.push(7)
    m.push(30)
    m.push(10)
    m.push(20)
    assert m.heap == [30, 20, 10, 7]
    m.push(30)
    assert m.heap == [30, 30, 10, 7, 20]
    m.push(50)
    assert m.heap == [50, 30, 30, 7, 20, 10]
    m.push(90)
    assert m.heap == [90, 30, 50, 7, 20, 10, 30]
    m.push(9)
    assert m.heap == [90, 30, 50, 9, 20, 10, 30, 7]


def test_pop_multiple_times():
    """Test pop method return and remove head value multiple times in a row."""
    m = MaxHeap()
    m.push(7)
    m.push(30)
    m.push(10)
    m.push(20)
    assert m.pop() == 30
    assert m.pop() == 20
    assert m.pop() == 10
    assert m.pop() == 7


def test_heap_instance_given_iterable_is_sorted_upon_init():
    """Test pop from populated heap."""
    m = MaxHeap([30, 50, 90, 7, 55, 20, 99, 4, 66])
    assert m.heap == [99, 90, 66, 55, 50, 30, 20, 7, 4]


def test_push_maintains_max_heap_when_instance_given_iterable_on_init():
    """Test pop from populated heap."""
    m = MaxHeap([30, 50, 90, 55, 20, 99, 66])
    assert m.heap == [99, 90, 66, 55, 50, 30, 20]
    m.push(100)
    assert m.heap == [100, 99, 66, 90, 50, 30, 20, 55]


def test_heap_maintains_max_through_multiple_pushes_and_pops():
    """Test push method multiple times from populated heap."""
    m = MaxHeap()
    m.push(7)
    m.push(30)
    m.push(10)
    m.push(20)
    assert m.heap == [30, 20, 10, 7]
    m.push(30)
    assert len(m.heap) == 5
    assert m.heap == [30, 30, 10, 7, 20]
    m.pop()
    assert m.heap == [30, 20, 7, 10]
    m.push(50)
    assert m.heap == [50, 30, 7, 10, 20]
    m.push(35)
    assert m.heap == [50, 30, 35, 10, 20, 7]
    m.pop()
    assert m.heap == [35, 30, 10, 20, 7]
    m.pop()
    m.pop()
    assert m.heap == [20, 10, 7]
