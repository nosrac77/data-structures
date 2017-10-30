"""Test for deque module."""

from deque import Deque


def test_empty_deque():
    """Test that an empty deque has head and tail."""
    d = Deque()
    assert d.head is None
    assert d.tail is None
    assert d.size() == 0


def test_append_to_deque():
    """Test that the append method is functional."""
    d = Deque()
    d.append(1)
    d.append(2)
    d.append(3)
    assert d.size() == 3
    assert d.deque.head.data == 1
    assert d.deque.tail.data == 3


def test_size_of_deque():
    """Test that the size method is functional."""
    d = Deque()
    d.append(1)
    assert d.size() == 1
    d.append(2)
    d.append(3)
    assert d.size() == 3


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
    except AttributeError:
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
    except AttributeError:
        pass



def test_push_two_values_into_doubly_linked_list():
    """Test that pushing two values adds to front of DLL."""
    l = DoublyLinked()
    l.push(0)
    l.push(1)
    assert l.head.data == 1
    assert l.tail.data == 0
    assert l.head.next_node.data == 0
    assert l.head.prev_node is None
    assert l.tail.next_node is None
    assert l.tail.prev_node.data == 1
    assert len(l) == 2


def test_push_multiple_values_into_doubly_linked_list_change_head():
    """Test that pushing multiple values adds to front of DLL."""
    l = DoublyLinked()
    l.push(0)
    l.push(1)
    l.push(3)
    l.push(4)
    assert l.head.data == 4
    assert l.tail.data == 0
    assert l.head.next_node.data == 3
    assert l.head.prev_node is None
    assert l.tail.next_node is None
    assert l.tail.prev_node.data == 1
    assert len(l) == 4


def test_pop_method():
    """Test that pushing multiple values changes inner node connections."""
    l = DoublyLinked()
    l.push(0)
    l.push(1)
    assert l.pop() == 1
    assert len(l) == 1
