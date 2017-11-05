"""Class that emulates a max binary heap."""


class MaxHeap(object):
    """Class that creates a max binary heap, optionally accepting an
    iterable of values."""

    def __init__(self, iterable=[]):
        """Create instance of MaxHeap class."""
        self.heap = sorted(iterable, reverse=True)

    def find_children(self, idx):
        """Return tuple of children values given parent value."""
        return (self.heap[idx * 2 + 1], self.heap[idx * 2 + 2])

    def find_parent(self, idx):
        """Return index of parent value given child value."""
        if idx % 2 == 0:
            parent_idx = idx / 2 - 1
        elif idx % 2 == 1:
            parent_idx = (idx - 1) / 2
        return int(parent_idx)

    def bubble_up(self):
        """Sort Max Heap from end of heap."""
        curr_idx = len(self.heap) - 1
        parent_idx = self.find_parent(curr_idx)
        while self.heap[curr_idx] > self.heap[parent_idx]:
            parent_val = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[curr_idx]
            self.heap[curr_idx] = parent_val
            curr_idx = self.find_parent(curr_idx)
            parent_idx = self.find_parent(curr_idx)
        if self.heap[curr_idx] > self.heap[0]:
            head_val = self.heap[0]
            self.heap[0] = self.heap[curr_idx]
            self.heap[curr_idx] = head_val
        return self.heap

    def sort_down(self):
        """Sort Max Heap from top downward."""
        if len(self.heap) == 3:
            first_child = self.heap[1]
            second_child = self.heap[2]
            biggest_child = max(first_child, second_child)
            if biggest_child > self.heap[0]:
                self.heap[self.heap.index(biggest_child)] = self.heap[0]
                self.heap[0] = biggest_child
        elif len(self.heap) > 4:
            for idx in range((len(self.heap) // 2) - 1):
                first_child = self.find_children(idx)[0]
                second_child = self.find_children(idx)[1]
                if self.heap[idx] < first_child or self.heap[idx] < second_child:
                    higher_val = max(first_child, second_child)
                    lower_val = self.heap[idx]
                    self.heap[self.heap.index(higher_val)] = lower_val
                    self.heap[idx] = higher_val

    def push(self, val):
        """Add value to end of heap."""
        self.heap.append(val)
        self.bubble_up()

    def pop(self):
        """Remove and return value from top of heap."""
        if len(self.heap) == 0:
            raise IndexError('Cannot pop from an empty list.')
        elif len(self.heap) == 1:
            return self.heap.pop()
        elif len(self.heap) == 2:
            return self.heap.pop(0)
        elif len(self.heap) == 3:
            head_val = self.heap[0]
            self.heap.pop(0)
            if self.heap[0] < self.heap[1]:
                self.heap[0] = self.heap[1]
                self.heap[1] = self.heap[0]
            return head_val
        head_val = self.heap[0]
        self.heap.pop(0)

        self.sort_down()
        self.bubble_up()

        return head_val
