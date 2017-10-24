"""Stack class function."""
from linked_list import LinkedList


class Stack(object):
    """Create Stack class."""

    def __init__(self, iterable=None):
        """Initialize Stack."""
        self.list = LinkedList()
        self.list._counter = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Utilize push method from LinkedList class."""
        self.list.push(val)

    def pop(self):
        """Utilize pop method from LinkedList class."""
        try:
            return self.list.pop()
        except IndexError:
            raise IndexError('Stack is empty.')

    def __len__(self):
        """Return list length."""
        return self.list._counter
