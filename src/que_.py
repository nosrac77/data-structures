"""Queue data structure."""
from doubly_linked_list import DoublyLinked


class Q(object):
    """Create queue data structure."""

    def __init__(self):
        """Create instance of Q class."""
        self.queue = DoublyLinked()

    def enqueue(self, value):
        """Add value to end of queue."""
        self.queue.append(value)

    def dequeue(self):
        """Remove and return value of queue front."""
        self.queue.pop()

    def peek(self):
        """Return next value in queue."""
        if self.queue.head.data:
            return self.queue.head.data
        return None
