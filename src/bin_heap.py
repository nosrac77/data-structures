"""Class that emulates a max binary heap."""


class MaxHeap(object):
    """Create a max binary heap, optionally accepting an iterable of values."""

    def __init__(self, iterable=[]):
        """Create an instance of MaxHeap class."""
        self.heap = sorted(iterable, reverse=True)

    def find_children(self, idx):
        """."""
        if idx * 2 + 2 <= len(self.heap) + 1:
            print('heap len', len(self.heap))
            print('first child idx', idx * 2 + 1)
            return (self.heap[idx * 2 + 1], self.heap[idx * 2 + 2])
        elif idx * 2 + 1 <= len(self.heap) + 1:
            print('heap len elif', len(self.heap))
            print('second child idx', idx * 2 + 2)
            return (self.heap[idx * 2 + 1])
        return None

    def find_parent(self, idx):
        """."""
        if idx % 2 == 0:
            parent_idx = idx / 2 - 1
        elif idx % 2 == 1:
            parent_idx = (idx - 1) / 2
        return int(parent_idx)

    def push(self, val):
        """Add value to end of heap."""
        self.heap.append(val)
        curr_idx = len(self.heap) - 1
        if len(self.heap) > 1:
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
        for idx in range(len(self.heap)):
            if self.find_children(idx):
                if self.heap[idx] < self.find_children(idx)[0] or self.heap[idx] < self.find_children(idx)[1]:
                    higher_val = max(self.find_children(idx))
                    self.heap[idx] = higher_val
        return head_val
