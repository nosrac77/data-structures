"""Deque data structure."""
from doubly_linked_list import DoublyLinked


class Deque(object):
    """Create Deque data structure."""

    def __init__(self):
        """Create instance of Deque class."""
        self.deque = DoublyLinked()

    def append(self, val):
        """Add value to end of deque."""
        self.deque.append(val)

    def append_left(self, val):
        """Add val to front of deque."""
        self.deque.push(val)

    def pop(self):
        """Remove and return value of deque end."""
        return self.deque.shift()

    def pop_left(self):
        """Remove and return value of deque front."""
        return self.deque.pop()

    def peek_left(self):
        """Return next value in deque."""
        if len(self.deque) > 0:
            return self.deque.head.data
        return None

    def peek(self):
        """Return tail value in deque."""
        if len(self.deque) > 0:
            return self.deque.tail.data
        return None

    def size(self):
        """Return length of deque."""
        return self.deque._counter
