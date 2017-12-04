"""Module that contains Hash Table class."""


class HashTable(object):
    """Class that creates an instance of a HashTable."""

    def __init__(self, table_size, hash_type='one'):
        """Define what instance of HashTable will have upon init. Hash Type
        is defined based upon the input given. For my implementation of the One
        at a Time Hash, input nothing for hash_type upon init. For my
        implementation of a simpler hash, input any other string."""

        self.table = []
        self.hash_type = hash_type
        for i in range(table_size):
            self.table.append([])

    def get(self, key):
        """Method to return value of stored data given key."""
        if not isinstance(key, str):
            raise ValueError('The key provided must be a string.')
        idx = self._hash(key)
        return self.table[idx]

    def set_key(self, key, val):
        """Method to add val to table given key."""
        if not isinstance(key, str):
            raise ValueError('The key provided must be a string.')
        idx = self._hash(key)
        self.table[idx].append(val)

    def _hash(self, key):
        """Method to hash the given key. One hash is more simple, the other is
        an implementation of the One at a Time hash."""
        if not isinstance(key, str):
            raise ValueError('The key provided must be a string.')
        if self.hash_type == 'one':
            char_ord = 0

            for idx, letter in enumerate(key):
                char_ord += ord(key[idx])
                char_ord += (char_ord << 10)
                char_ord ^= (char_ord >> 6)

            char_ord += (char_ord << 3)
            char_ord ^= (char_ord >> 11)
            char_ord += (char_ord << 15)

            return char_ord % len(self.table)
        else:
            char_ord = 0
            for idx, letter in enumerate(key):
                char_ord += ord(letter)
                if letter.lower() == letter:
                    char_ord += ((idx + 1) * ord(letter.upper()))
                else:
                    char_ord += ((idx + 1) * ord(letter.lower()) < 1)
            return char_ord % len(self.table)
