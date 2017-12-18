"""Contains class function for generating linked lists."""


class LinkedList(object):
    """Creating LinkedList class."""

    def __init__(self, iterable=()):
        """Initialize LinkedList class."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Create push method of LinkedList."""
        self.head = Node(val, self.head)
        self._counter += 1

    def pop(self):
        """Remove and returns value of head node."""
        if self.head is None:
            raise IndexError('List is empty.')
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def size(self):
        """Return length of linked list."""
        return self._counter

    def __len__(self):
        """Return length of linked list."""
        return self._counter

    def search(self, val):
        """Return node containing given value."""
        current_node = self.head
        while current_node:
            if current_node.data == val:
                return current_node
            current_node = current_node.next

    def remove(self, val):
        """Remove given node from linked list."""
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == val:
                current_node.pop()
            current_node = current_node.next


class Node(object):
    """Creating Node class."""
    def __init__(self, data, next):
        self.data = data
        self.next = next
