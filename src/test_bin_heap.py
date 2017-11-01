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
    assert m.heap == 


def test_size_of_zero():
    """Test size of deque when empty."""
    d = Deque()
    assert d.size() == 0


def test_append_left():
    """Test append left function, test head and tail."""
    d = Deque()
    d.append_left(500)
    assert d.deque.head.data == 500
    assert d.deque.tail.data == 500


def test_append_left_multiple_items():
    """Test append left function, test head and tail."""
    d = Deque()
    d.append_left(500)
    d.append_left(1000)
    d.append_left(5000)
    assert d.deque.head.data == 5000
    assert d.deque.tail.data == 500


def test_append_left_and_regular_append_together():
    """Test that append_left and append work together."""
    d = Deque()
    d.append_left(1)
    d.append(5)
    assert d.deque.head.data == 1
    assert d.deque.tail.data == 5


def test_pop_on_empty_deque():
    """Test pop on an empty deque."""
    d = Deque()
    try:
        assert d.pop()
    except IndexError:
        pass


def test_pop_on_deque_with_contents():
    """Test pop on queue with stuff in it."""
    d = Deque()
    d.append(5)
    d.append(10)
    d.append(15)
    assert d.pop() == 15
    assert d.pop() == 10


def test_pop_left_on_empty_deque():
    """Test pop_left on an empty deque."""
    d = Deque()
    try:
        assert d.pop_left()
    except IndexError:
        pass


def test_pop_left_on_filled_deque():
    """Test pop_left on a deque with contents in it."""
    d = Deque()
    d.append(1)
    d.append(2)
    d.append(3)
    assert d.pop_left() == 1
    assert d.pop_left() == 2


def test_peek_on_empty_deque():
    """Test peek on empty deque."""
    d = Deque()
    assert d.peek() is None


def test_peek_on_deque_with_head():
    """Test peek on a deque with a head, aka with contents."""
    d = Deque()
    d.append(1)
    d.append(2)
    assert d.peek() == 2


def test_peek_left_on_empty_deque():
    """Test peek on empty deque."""
    d = Deque()
    assert d.peek_left() is None


def test_peek_left_on_deque_with_head():
    """Test peek on a deque with a head, aka with contents."""
    d = Deque()
    d.append(1)
    d.append(2)
    assert d.peek_left() == 1


def test_peek_and_peek_left_on_deque_with_one_node():
    """Test peek and peek_left on a one-node deque."""
    d = Deque()
    d.append(1)
    assert d.peek() == 1 and d.peek_left() == 1
