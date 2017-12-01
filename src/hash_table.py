"""Module that contains Hash Table class."""


class HashTable(object):
    """Class that creates an instance of a HashTable."""

    def __init__(self):
        """Define what instance of HashTable will have upon init."""
        self.table = []
        for i in range(1000):
            self.table.append([])

    def get(self, key):
        """Method to return value of stored data given key."""
        idx = self._hash(key)
        if self.table[idx]:
            return self.table[idx]
        return None

    def set_key(self, key, val):
        """Method to add val to table given key."""
        idx = self._hash(key)
        if self.table[idx]:
            self.table[idx].append(key)
        else:
            self.table[idx] = [key]

    def _hash(self, key):
        """Method to hash the given key."""
        h = 0

        for bucket in self.table:
            h += (h << 10)
            h ^= (h >> 6)

        h += (h << 3)
        h ^= (h >> 11)
        h += (h << 15)

        return h
