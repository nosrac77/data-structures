"""Class of doubly linked list."""
from linked_list import LinkedList


class DoublyLinked(LinkedList):
    """Class that creates instance of doubly linked list."""

    def __init__(self):
        """Initialize DoublyLinked instance."""
        self.list = LinkedList()
        self.list._counter = 0
        self.previous = None
        self.tail = None

    def push(self, val):
        """Emulate LinkedList push method."""
        self.previous = self.list.head
        self.list.push(val)

    def pop(self):
        """Emulate LinkedList pop method."""
        super(DoublyLinked, self).pop()

    def remove(self, val):
        """Emulate LinkedList remove method."""
        super(DoublyLinked, self).remove(val)

    def __len__(self):
        """Emulate LinkedList's len method."""
        super(DoublyLinked, self).__len__()

    def shift(self):
        """Shift method to take last val from list and return it."""
        for rep in range(len(self.list)):
            if self.list.head.next is None:
                temp = self.list.head.data
                self.list.remove(temp)
                return temp
            self.list.head = self.list.head.next

if __name__ == '__main__':
    dl = DoublyLinked()
