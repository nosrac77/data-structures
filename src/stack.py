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
        elif iterable is None:
            self.push(None)
        else:
            raise ValueError('Stack argument must be an iterable.')

    def push(self, val):
        """Utilize push method from LinkedList class."""
        self.list.push(val)

    def pop(self):
        """Utilize pop method from LinkedList class."""
        if len(self) == 1:
            raise IndexError('Stack is empty.')
        else:
            return self.list.pop()

    def __len__(self):
        """Return list length."""
        return self.list._counter
