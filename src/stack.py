"""Stack class function."""
from linked_list import LinkedList
from linked_list import Node


class Stack(object):
    """Creating Stack class."""
    def __init__(self, node=Node()):
        self.list = LinkedList()
        self.list._counter = 0
        if node.data is not None:
            for item in node:
                self.push(item)

    def push(self, val):
        """Utilizes push method from LinkedList class."""
        self.list.push(val)

    def pop(self):
        """Utilizes pop method from LinkedList class."""
        self.list.pop()
        return self.list.output

    def __len__(self):
        """Returns list length."""
        return self.list._counter
