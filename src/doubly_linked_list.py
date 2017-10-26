"""Class of doubly linked list."""


class DoublyLinked(object):
    """Class that creates instance of doubly linked list."""

    def __init__(self):
        """Initialize DoublyLinked instance."""
        self._counter = 0
        self.head = None
        self.tail = None

    def push(self, val):
        """Emulate LinkedList push method."""
        val = Node(val)
        self._counter += 1
        if self.head is None:
            self.head = val
            self.tail = self.head
        else:
            self.head.prev_node = val
            val.next_node = self.head
            self.head = val

    def pop(self):
        """Emulate LinkedList pop method."""
        if self.head is None:
            raise IndexError('List is empty.')
        if self.head.next_node is None:
            self.tail = None
        if self.head.next_node.next_node is None:
            self.tail = self.head
        output = self.head.data
        self.head = self.head.next_node
        if self.head:
            self.head.prev_node = None
        self._counter -= 1
        return output

    def remove(self, val):
        """Remove given node from linked list."""
        current_node = self.head
        while current_node is not None:
            if current_node.data == val:
                self._counter -= 1
                return current_node.pop()
            if current_node.next_node is None:
                raise IndexError('Input value not in DoublyLinkedList.')
        current_node = current_node.next_node

    def __len__(self):
        """Emulate LinkedList's len method."""
        return self._counter

    def shift(self):
        """Shift method to take last val from list and return it."""
        return self.remove(self.tail)

    def append(self, val):
        """Appends to end of list."""
        val = Node(val)
        self._counter += 1
        if self.head is None:
            self.push(val)
        else:
            self.tail.next_node = None
            val.prev_node = self.tail
            self.tail = val


class Node(object):
    """Double List Node class."""
    def __init__(self, val, next_node=None, prev_node=None):
        self.next_node = next_node
        self.prev_node = prev_node


if __name__ == '__main__':
    dl = DoublyLinked()
