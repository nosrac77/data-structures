"""Class of doubly linked list."""
from linked_list import LinkedList
from linked_list import Node


class DoublyLinked(LinkedList):
    """Class that creates instance of doubly linked list."""

    def __init__(self):
        """Initialize DoublyLinked instance."""
        self.list = LinkedList()
        self.list._counter = 0

    def push(self, val):
        """Emulate LinkedList push method."""
        super(DoublyLinked, self).push(val)

    def pop(self):
        """Emulate LinkedList pop method."""
        super(DoublyLinked, self).pop()

    def remove(self, val):
        """Emulate LinkedList remove method."""
        super(DoublyLinked, self).remove(val)


if __name__ == '__main__':
    dl = DoublyLinked()
