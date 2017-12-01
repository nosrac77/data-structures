"""Class that emulates a max binary heap."""


class Node(object):
    """Class that creates Node object."""
    def __init__(self, value, left=None, right=None):
        """Creates instance of Node class object."""
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    def _get_children(self):
        """Return left and right values of node."""
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children


class Bst(object):
    """Class that creates a binary search tree, optionally accepting an
    iterable of values."""

    def __init__(self):
        """Create instance of MaxHeap class."""
        self.node_values = []
        self.bst = []
        self.root = None
        self.traversal_list = []
        self._recursion_check = False

    def insert(self, val):
        """Add value to bst."""
        if len(self.bst) == 0:
            self.bst.append(Node(val))
            self.node_values.append(val)
            self.root = self.bst[0]
            return
        if val in self.node_values:
            return
        self.node_values.append(val)
        new_node = Node(val)
        self.bst.append(new_node)
        current_node = self.bst[0]
        while current_node is not None:
            if val > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                    continue
                new_node.parent = current_node
                current_node.right = new_node
                break
            if val < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                    continue
                new_node.parent = current_node
                current_node.left = new_node
                break

    def search(self, val):
        """Search for and return Node containing value, if value exists."""
        for node in self.bst:
            if node.value == val:
                return node
        return None

    def size(self):
        """Return size of binary search tree."""
        return len(self.node_values)

    def contains(self, val):
        """Return True if val in binary search tree."""
        if val in self.node_values:
            return True
        return False

    def depth(self, node):
        """Return number of levels in binary search tree."""
        if node is None:
            return 0
        if not node.left and not node.right:
            return 0
        elif node.left and not node.right:
            return self.depth(node.left) + 1
        elif node.right and not node.left:
            return self.depth(node.right) + 1
        return max(self.depth(node.left), self.depth(node.right)) + 1

    def balance(self):
        """Return an integer based upon how balanced binary search tree depth
        is."""
        if self.size() == 1:
            return 0
        if self.root.right and not self.root.left:
            return -1
        if self.root.left and not self.root.right:
            return 1
        left_levels = self.depth(self.root.left)
        right_levels = self.depth(self.root.right)
        if left_levels == right_levels:
            return 0
        elif left_levels > right_levels:
            return 1
        elif right_levels > left_levels:
            return -1

    def delete(self, val):
        """Delete node with value from binary search tree, if present."""
        if val not in self.node_values:
            return
        node = self.search(val)
        if not node.left and not node.right:
            if node.parent.left.value == val:
                node.parent.left = None
                node.parent = None
                return
            node.parent.right = None
            node.parent = None
            self.bst.remove(node)
            self.node_values.remove(val)
            return
        if len(node._get_children()) == 2:
            if node.right.left:
                current_node = node.right.left
                while current_node.left is not None:
                    current_node = current_node.left
                if current_node.right:
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                    current_node.parent = None
                    current_node.right = None
                    node.value = current_node.value
                    self.bst.remove(current_node)
                    self.node_values.remove(val)
                    return
                current_node.parent.left = None
                current_node.parent = None
                node.value = current_node.value
                self.bst.remove(current_node)
                self.node_values.remove(val)
                return
            node.right.parent = node.parent
            node.parent.right = node.right
            node.parent = None
            node.right = None
            self.bst.remove(current_node)
            self.node_values.remove(val)
            return
        node._get_children()[0].parent = node.parent
        if node.parent.value > node.value:
            node.parent.left = node._get_children()[0]
        elif node.parent.value < node.value:
            node.parent.right = node._get_children()[0]
        node.parent = None
        self.bst.remove(node)
        self.node_values.remove(val)
        return

    def _pre_order_traversal(self, node):
        """Helper function for pre_order method."""
        if self.root.value not in self.traversal_list:
            self.traversal_list.append(self.root.value)
        if node.left:
            self.traversal_list.append(node.left.value)
            self._pre_order_traversal(node.left)
        if node.right:
            self.traversal_list.append(node.right.value)
            self._pre_order_traversal(node.right)

    def pre_order(self):
        """Return generator that returns values of tree using pre_order
        traversal, one at a time."""
        if self._recursion_check is False:
            self._recursion_check = True
            self._pre_order_traversal(self.root)
        for val in self.traversal_list:
            num = val
            self.traversal_list.pop(0)
            if len(self.traversal_list) == 0:
                self._recursion_check = False
            yield num

    def _post_order_traversal(self, node):
        """Helper function for post_order method."""
        if node.left:
            self._post_order_traversal(node.left)
        if node.right:
            self._post_order_traversal(node.right)
        self.traversal_list.append(node.value)

    def post_order(self):
        """Return generator that returns values of tree using post_order
        traversal, one at a time."""
        if self._recursion_check is False:
            self._recursion_check = True
            self._post_order_traversal(self.root)
        for val in self.traversal_list:
            num = val
            self.traversal_list.pop(0)
            if len(self.traversal_list) == 0:
                self._recursion_check = False
            yield num

    def _in_order_traversal(self, node):
        """Helper function for in_order method."""
        if node.left:
            self._in_order_traversal(node.left)
        self.traversal_list.append(node.value)
        if node.right:
            self._in_order_traversal(node.right)

    def in_order(self):
        """Return generator that returns values of tree using in_order
        traversal, one at a time."""
        if self._recursion_check is False:
            self._recursion_check = True
            self._in_order_traversal(self.root)
        for val in self.traversal_list:
            num = val
            self.traversal_list.pop(0)
            if len(self.traversal_list) == 0:
                self._recursion_check = False
            yield num

    def _breadth_first_traversal(self):
        """Helper function of breadth_first method."""
        stack = [self.root]
        while stack:
            current_node = stack[0]
            stack = stack[1:]
            self.traversal_list.append(current_node.value)
            for child in current_node._get_children():
                stack.append(child)

    def breadth_first(self):
        """Return generator that returns values of tree using breadth_first
        traversal, one at a time."""
        if len(self.traversal_list) == 0:
            self._breadth_first_traversal()
        for val in self.traversal_list:
            num = val
            self.traversal_list.pop(0)
            yield num


if __name__ == '__main__':  # pragma no cover
    import timeit

    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(6)
    new_bst.insert(15)
    new_bst.insert(9)
    new_bst.insert(11)
    new_bst.insert(5)
    new_bst.insert(18)
    new_bst.insert(7)

    balanced_output = """
    The assignment asked for a time complexity check against searching the tree
    for a given value. Since the .contains() method of the tree does this, I
    will be using it on two different binary search trees. One will be
    balanced and the other will be the most unbalanced it can be.

    Since the .contains() method simply checks the value given against a list
    of all known node values, the depth level will not effect the time taken to
    search for a value in either tree. The time complexity for the method will
    be 0(k) at best and 0(n) at worst. Let's demonstrate the worst case first.

    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(6)
    new_bst.insert(15)
    new_bst.insert(9)
    new_bst.insert(11)
    new_bst.insert(5)
    new_bst.insert(18)
    new_bst.insert(7) <--- value being searched for, depth level is 3, list
                           index is 9.

    Above is the code I used to create a balanced binary search tree. The time
    to search through that tree to find the value of 7, which is 3 levels deep
    on the left side, is below. I set timeit to repeat the search 3 times to
    show the average run time of the method.
    """
    print(balanced_output)
    print('Time to find 7: ', timeit.repeat('new_bst.contains(7)', repeat=3, globals=globals()))

    unbalanced_bst = Bst()
    unbalanced_bst.insert(10)
    unbalanced_bst.insert(9)
    unbalanced_bst.insert(8)
    unbalanced_bst.insert(7)
    unbalanced_bst.insert(6)
    unbalanced_bst.insert(5)
    unbalanced_bst.insert(4)
    unbalanced_bst.insert(3)
    unbalanced_bst.insert(2)
    unbalanced_bst.insert(1)

    unbalanced_output = """
    Now that we've tested a balanced binary search tree, let's build one that's
    unbalanced.

    unbalanced_bst = Bst()
    unbalanced_bst.insert(10)
    unbalanced_bst.insert(9)
    unbalanced_bst.insert(8)
    unbalanced_bst.insert(7)
    unbalanced_bst.insert(6)
    unbalanced_bst.insert(5)
    unbalanced_bst.insert(4)
    unbalanced_bst.insert(3)
    unbalanced_bst.insert(2)
    unbalanced_bst.insert(1) <--- value being searched for, depth level is 9,
                                  list index is 9.

    All nodes from start to end are flowing off to the left, with the final
    node sitting 9 levels deep. Below is the time it took to search through the
    tree to find the value of 1, the lowest node in the tree, again repeated
    3 times to get the method's average speed.
    """
    print(unbalanced_output)
    print('Time to find 1: ', timeit.repeat('unbalanced_bst.contains(1)', repeat=3, globals=globals()))

    closer_value_output = """
    In both of the examples above, even though the values searched for lay in
    very different depth levels, the time taken to find those values was still
    consistent across both trees.

    Now that we've seen the .contains() method at it's worst,
    which is 0(n), lets test it's best, 0(k). Using the same two trees we
    created before, let's search for the values at the 0th index of their
    respective values lists.

    new_bst = Bst()
    new_bst.insert(10) <--- value being searched for, depth level is 0, index
    new_bst.insert(8)       in list is 0.
    new_bst.insert(12)
    new_bst.insert(6)
    new_bst.insert(15)
    new_bst.insert(9)
    new_bst.insert(11)
    new_bst.insert(5)
    new_bst.insert(18)
    new_bst.insert(7)

    unbalanced_bst = Bst()
    unbalanced_bst.insert(10) <--- value being searched for, depth level is 0,
    unbalanced_bst.insert(9)       index is list is 0.
    unbalanced_bst.insert(8)
    unbalanced_bst.insert(7)
    unbalanced_bst.insert(6)
    unbalanced_bst.insert(5)
    unbalanced_bst.insert(4)
    unbalanced_bst.insert(3)
    unbalanced_bst.insert(2)
    unbalanced_bst.insert(1)
    """
    print(closer_value_output)
    print('Time to find 10 in unbalanced bst: ', timeit.repeat('unbalanced_bst.contains(10)', repeat=3, globals=globals()))
    print('Time to find 10 in balanced bst: ', timeit.repeat('new_bst.contains(10)', repeat=3, globals=globals()))
    final_thoughts = """

    As you can see, the time it takes to find a value is determined by that
    value's index in the list it exists in and not it's depth level within the
    binary search tree itself.
    """
    print(final_thoughts)
