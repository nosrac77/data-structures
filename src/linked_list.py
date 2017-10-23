"""Contains class function for generating linked lists."""


class LinkedList(object):

    def __init__(self):
        """Initializing LinkedList class."""
        self.head = None


    def push(self, val):
        """Create push method of LinkedList."""
        self.head = Node(val, self.head)
        return self.head

    #
    # def pop(val):
    #     try:
    #         del num_series[0]
    #         return val
    #     except IndexError:
    #         print('Cannot remove value at non-existent index.')
    #
    #
    # def size(num_series):
    #     return len(num_series)
    #
    #
    # def search(val):
    #     if LinkedList.size(num_series) > 0:
    #         return num_series.index(val)


class Node(object):
    """Creating Node class."""

    def __init__(self, data, next):
        self.data = data
        self.next = next
