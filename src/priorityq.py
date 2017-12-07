"""Class that initializes an instance of a priority queue."""


class Priority(object):
    """Class to create priority queue."""

    def __init__(self):
        """Initialize instance of self."""
        self._counter = 0
        self.priorities = []
        self.head = None
        self.tail = None

    def insert(self, val, priority=0):
        """Add value to end of queue."""
        if priority < 0:
            raise ValueError('Lowest priority is 0.')
        self.priorities.append(priority)
        if self.head is None:
            curr = Node(val, priority)
            self.head = curr
            self.tail = self.head
            self._counter += 1
        else:
            curr = Node(val, priority, next_node=None, prev_node=self.tail)
            self.tail.next_node = curr
            self.tail = curr
            self._counter += 1

    def pop(self):
        """Remove highest priority value from queue."""
        if self.head is None:
            raise IndexError('Input priority not in Priority Queue.')
        max_priority = max(self.priorities)
        current_node = self.head
        while current_node is not None:
            print(current_node.priority)
            if current_node.priority == max_priority:
                val = current_node.data
                if current_node is self.head:
                    self.head = None
                    self._counter -= 1
                    return val
                if current_node.prev_node is None:
                    current_node.next_node.prev_node = None
                    self.head = None
                    self._counter -= 1
                    return val
                if current_node.next_node is None:
                    current_node.prev_node.next_node = None
                    self.tail = None
                    self._counter -= 1
                    return val
                current_node.prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = current_node.prev_node
                self._counter -= 1
                self.priorities.remove(max_priority)
                return val
            current_node = current_node.next_node

    def peek(self):
        """Return highest priority node in queue."""
        if self.head is None:
            raise IndexError('Priority Queue is empty.')
        max_priority = max(self.priorities)
        current_node = self.head
        while current_node is not None:
            if current_node.priority == max_priority:
                val = current_node.data
                return val
            current_node = current_node.next_node


class Node(object):
    """Double List Node class."""

    def __init__(self, val, priority, next_node=None, prev_node=None):
        """Initialize Node class instance."""
        self.priority = priority
        self.data = val
        self.next_node = next_node
        self.prev_node = prev_node
