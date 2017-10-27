"""Tests for queue data structure."""

import pytest
from que_ import Q

q = Q()


def test_empty_queue():
    """Test that an empty queue has no len, test empty peek."""
    assert q.peek() is None
    assert len(q) == 0
    with pytest.raises(IndexError):
        q.pop()


def test_enqueue():
    """Test that enqueue function works."""
    q.enqueue(1)
    assert q.queue.head.data == 1
    assert len(q) == 1
    q.enqueue(2)
    assert q.peek() == 1
    q.enque(3)
    assert len(q) == 3


def test_dequeue():
    """Test that dequeue works."""
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert len(q) == 2
    assert q.dequeue() == 2
    assert q.dequeue() == 3


# def test_push_one_node_into_doubly_linked_list():
#     """Test that pushing one value adds it to front of doubly linked list."""
#     l = DoublyLinked()
#     l.push(0)
#     assert l.head.data == 0
#     assert l.tail.data == 0
#     assert l.head.next_node is None
#     assert l.head.prev_node is None
#     assert l.tail.next_node is None
#     assert l.tail.prev_node is None
#     assert len(l) == 1