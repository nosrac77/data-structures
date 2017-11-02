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
        """Add node with value to head of list."""
        self.head = Node(val, self.head)
        self._counter += 1

    def pop(self):
        """Remove and return value of head node."""
        if self.head is None:
            raise IndexError('List is empty.')
        output = self.head.data
        self.head = self.head.next_node
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
            current_node = current_node.next_node
        return None

    def remove(self, val):
        """Remove given node from linked list."""
        current_node = self.head
        while current_node is not None:
            if current_node.next_node.data == val:
                current_node.next_node = current_node.next_node.next_node
                self._counter -= 1
                return val
            if current_node.next_node is None:
                raise IndexError('Input value not in DoublyLinkedList.')
            current_node = current_node.next_node

    def display(self):
        """Print properly formatted doubly linked list."""
        start_paren = "("
        if self.head is None:
            return "()"
        current_node = self.head
        while current_node:
            if current_node.next_node is None:
                start_paren += str(current_node.data) + ")"
                return start_paren
            else:
                start_paren += str(current_node.data) + ", "
                current_node = current_node.next_node

    def __str__(self):
        """Use display method."""
        return self.display()


class Node(object):
    """Creating Node class."""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
