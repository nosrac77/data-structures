"""Tests for queue data structure."""

import pytest
from que_ import Q


def test_enqueue():
    """Test that enqueue function works."""
    q = Q()
    q.enqueue(1)
    assert q.queue.head.data == 1
    assert len(q) == 1
    q.enqueue(2)
    assert q.peek() == 1
    q.enqueue(3)
    assert len(q) == 3


def test_dequeue():
    """Test that dequeue works."""
    q = Q()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert len(q) == 2
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_dequeue_from_empty():
    """Test dequeue from empty queue."""
    q = Q()
    with pytest.raises(IndexError):
        q.dequeue()


def test_peek():
    """Test that peek works."""
    q = Q()
    q.enqueue(1)
    assert q.peek() == 1
    q.enqueue(2)
    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 2


def test_peek_on_empty_queue():
    """Test edge case, calling peak on empty queue."""
    q = Q()
    assert q.peek() is None


def test_len_empty_queue():
    """Test that an empty queue has no len."""
    q = Q()
    assert len(q) == 0


def test_len():
    """Test that len function works."""
    q = Q()
    q.enqueue(500)
    assert len(q) == 1
    q.enqueue(1000)
    assert len(q) == 2
    q.enqueue(1500)
    assert len(q) == 3
    q.dequeue()
    assert len(q) == 2
