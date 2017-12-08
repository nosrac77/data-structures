"""Module that contains Trie Tree."""


class Node(object):
    """Create Node."""
    def __init__(self, letter, parent=None):
        """Create instance of Node class object."""
        self.letter = letter
        self.parent = parent
        self.children = {}


class Trie(object):
    """Class to create Trie Tree with methods."""

    def __init__(self):
        """Create instance of Trie class object."""
        self.root = Node('*')
        self._size = 0

    def insert(self, string):
        """Add new string to Trie Tree."""
        if self.contains(string):
            return
        try:
            self.root.children[string[0]]
        except KeyError:
            self.root.children[string[0]] = Node(string[0])
            self.root.children[string[0]].parent = self.root
        current_node = self.root.children[string[0]]
        idx = 1
        while current_node:
            try:
                current_node = current_node.children[string[idx]]
                idx += 1
            except IndexError:
                current_node.children['$'] = Node('$')
                current_node.children['$'].parent = current_node
                break
            except KeyError:
                current_node.children[string[idx]] = Node(string[idx])
                current_node.children[string[idx]].parent = current_node
                current_node = current_node.children[string[idx]]
                idx += 1
                continue
        self._size += 1

    def contains(self, string):
        """Return true if string in table, else return false."""
        try:
            self.root.children[string[0]]
        except KeyError:
            return False
        current_node = self.root.children[string[0]]
        idx = 1
        while current_node:
            try:
                current_node = current_node.children[string[idx]]
                idx += 1
            except IndexError:
                try:
                    current_node.children['$']
                    return True
                except KeyError:
                    return False
            except KeyError:
                return False

    def size(self):
        """Return word count of Trie Tree."""
        return self._size

    def remove(self, string):
        """Delete string from Trie, if string in Trie."""
        try:
            self.root.children[string[0]]
        except KeyError:
            raise KeyError('Given word not in Trie Tree.')
        current_node = self.root.children[string[0]]
        idx = 1
        while current_node:
            try:
                current_node = current_node.children[string[idx]]
                idx += 1
            except IndexError:
                try:
                    current_node.children['$']
                    self._remove_helper(current_node, current_node.children['$'])
                    self._size -= 1
                    break
                except KeyError:
                    raise KeyError('Given word not in Trie Tree.')
            except KeyError:
                raise KeyError('Given word not in Trie Tree.')

    def _remove_helper(self, parent, child):
        """Helper function for remove method of Trie Tree."""
        if not child.children and parent is not None:
            new_parent = parent.parent
            new_child = parent
            del parent.children[child.letter]
            child.parent = None
            self._remove_helper(new_parent, new_child)

    def traversal(start):
        """Method of Trie Tree that returns generator containing all letters
        that branch off of start, if applicable."""
