"""Functions that test DoublyLinked class methods."""
import pytest
from doubly_linked_list import DoublyLinked


def test_doubly_linked_tail():
    """Test that there is a node that points at two different nodes."""
    n = DoublyLinked()
    n.push(1)
    n.push(2)
    n.push(3)
    assert n.tail.data == 1


def test_empty_doubly_linked_list_constructor():
    """Test that a doubly-linked list created with no arguments is empty."""
    n = DoublyLinked()
    assert n.head is None
    assert n.tail is None
    assert len(n) == 0


def test_push_one_node_into_doubly_linked_list():
    """Test that pushing one value adds it to front of doubly linked list."""
    l = DoublyLinked()
    l.push(0)
    assert l.head.data == 0
    assert l.tail.data == 0
    assert l.head.next_node is None
    assert l.head.prev_node is None
    assert l.tail.next_node is None
    assert l.tail.prev_node is None
    assert len(l) == 1


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


def test_pop_method_returns_error_when_list_empty():
    """Test that pushing multiple values changes inner node connections."""
    l = DoublyLinked()
    try:
        assert l.pop() == IndexError
    except IndexError:
        pass


def test_append():
    """Test that append function works."""
    dl = DoublyLinked()
    dl.append(1)
    assert dl.head.data == 1
    assert len(dl) == 1
    dl.append(2)
    assert dl.head.data == 1
    dl.append(3)
    assert len(dl) == 3


def test_shift():
    """Test shift method return and remove value."""
    dl = DoublyLinked()
    dl.push(1)
    dl.push(2)
    assert dl.shift() == 1


def test_shift_raises_exception_if_no_return_value():
    """Test shift method raises exception if there's no return value."""
    dl = DoublyLinked()
    try:
        assert dl.remove(5)
    except AttributeError:
        pass
