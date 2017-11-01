"""Class that emulates a max binary heap."""


class MaxHeap(object):
    """Class that creates a max binary heap, optionally accepting an
    iterable of values."""

    def find_children(self, idx):
        return (self.heap[idx * 2 + 1], self.heap[idx * 2 + 2])

    def find_parent(self, idx):
        if idx % 2 == 0:
            parent_idx = idx / 2 - 1
        elif idx % 2 == 1:
            parent_idx = (idx - 1) / 2
        return parent_idx

    def __init__(self, iterable=[]):
        """Create an instance of MaxHeap class."""
        self.heap = sorted(iterable, reverse=True)

    def push(self, val):
        """Add value to end of heap."""
        self.heap.append(val)
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

    def pop(self):
        """Remove and return value from top of heap."""
        if len(self.heap) == 0:
            raise IndexError('Cannot pop from an empty list.')
        head_val = self.heap[0]
        self.heap.pop(0)
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
        # for idx, num in enumerate(self.heap):
        #     if self.heap[idx] < self.find_children(idx)[0] or self.heap[idx] < self.find_children(idx)[1]:
        #         higher_val = max(self.find_children(idx))
        #         self.heap[idx] = higher_val
        # while self.heap[curr_idx] > self.heap[parent_idx]:
        #     parent_val = self.heap[parent_idx]
        #     self.heap[parent_idx] = self.heap[curr_idx]
        #     self.heap[curr_idx] = parent_val
        #     curr_idx = self.find_parent(curr_idx)
        # if self.heap[curr_idx] > self.heap[0]:
        #     head_val = self.heap[0]
        #     self.heap[0] = self.heap[curr_idx]
        #     self.heap[curr_idx] = head_val
        return head_val
