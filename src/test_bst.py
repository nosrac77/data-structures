"""Module that contains function for testing binary search tree."""
import pytest


@pytest.fixture
def new_bst():
    """Fixture that creates a new binary search tree."""
    from bst import Bst
    return Bst()


@pytest.fixture
def filled_bst():
    """Fixture that creates a filled binary search tree."""
    from bst import Bst
    b = Bst()
    b.insert(10)
    b.insert(8)
    b.insert(12)
    b.insert(15)
    b.insert(9)
    b.insert(6)
    b.insert(11)
    b.insert(5)
    b.insert(18)
    b.insert(7)
    return b


def test_new_bst_node_initialized_with_correct_values():
    """Function that tests a new binary search tree node contains given value
    and default values for left and right states."""
    from bst import Node

    new_node = Node(10)
    assert new_node.value == 10
    assert new_node.right is None
    assert new_node.left is None


def test_new_bst_initialized_with_empty_lists(new_bst):
    """Function that tests a new_bst is initialized with two empty lists."""

    assert isinstance(new_bst.bst, list)
    assert isinstance(new_bst.node_values, list)


def test_insert_adds_node_with_specified_value(new_bst):
    """Function that tests insert method of binary search tree adds a new node
    with the given value."""
    from bst import Node

    new_bst.insert(10)
    assert isinstance(new_bst.bst[0], Node)
    assert new_bst.bst[0].value == 10
    assert new_bst.node_values[0] == 10


def test_inserts_maintain_binary_heap_lefts_and_rights(new_bst):
    """Function that tests multiple inserts into the binary heap will place
    nodes in the proper left or right states, depending on the value given."""

    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(9)
    assert new_bst.bst[0].value == 10
    assert new_bst.bst[0].left.value == 8
    assert new_bst.bst[0].right.value == 12
    assert new_bst.bst[0].left.right.value == 9


def test_insert_will_not_add_multiples_of_same_value(new_bst):
    """Function that tests insert will not add a value if the given value
    is already in the binary search tree."""

    new_bst.insert(10)
    new_bst.insert(10)
    assert new_bst.size() == 1
    assert len(new_bst.bst) == 1
    assert len(new_bst.node_values) == 1
    assert new_bst.bst[0].value == 10
    assert new_bst.bst[0].right is None
    assert new_bst.bst[0].left is None


def test_search_returns_node_if_node_with_value_in_bst(new_bst):
    """Function that tests the search method of the binary search tree will
    return the node with the given value if a node with that value exists."""

    new_bst.insert(10)
    assert new_bst.search(10).value == 10


def test_search_returns_none_if_node_with_value_not_in_bst(new_bst):
    """Function that tests the search method of the binary search tree will
    return the none if a node with the given value does not exist."""

    new_bst.insert(10)
    assert new_bst.search(999) is None


def test_size_returns_correct_number_of_nodes_in_bst(new_bst):
    """Function that tests the size method of the binary search tree returns
    the number of nodes in the tree."""

    new_bst.insert(55)
    new_bst.insert(66)
    new_bst.insert(77)
    assert new_bst.size() == 3


def test_contain_returns_true_if_node_with_value_in_bst(new_bst):
    """Functtion that tests contains method of binary search tree returns True
    if node with given value exists."""

    new_bst.insert(10)
    assert new_bst.contains(10) is True


def test_contain_returns_false_if_node_with_value_not_in_bst(new_bst):
    """Functtion that tests contains method of binary search tree returns False
    if node with given value does not exist."""

    new_bst.insert(10)
    assert new_bst.contains(11) is False


def test_depth_returns_correct_depth_of_bst(new_bst):
    """Function that tests depth method of binary search tree returns the
    correct number of levels in the tree."""

    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(9)
    new_bst.insert(11)
    assert new_bst.depth(new_bst.bst[0]) == 2


def test_depth_returns_0_if_bst_empty(new_bst):
    """Function that tests depth method of binary search tree returns the
    correct number of levels in the tree."""

    assert new_bst.depth(new_bst.root) == 0


def test_balance_returns_pos_int_if_bst_levels_deeper_on_left(new_bst):
    """Function that tests balance method of binary search tree returns a
    positive integer if the levels on the left side are greater than the
    levels on the right side."""

    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(9)
    assert new_bst.balance() == 1


def test_balance_returns_neg_int_if_bst_levels_deeper_on_right(new_bst):
    """Function that tests balance method of binary search tree returns a
    negative integer if the levels on the right side are greater than the
    levels on the left side."""

    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(15)
    assert new_bst.balance() == -1


def test_balance_returns_zero_if_bst_balanced(new_bst):
    """Function that tests balance method of binary search tree returns zero
    if the tree is balanced on both sides."""

    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(15)
    new_bst.insert(9)
    assert new_bst.balance() == 0


def test_balance_returns_zero_if_bst_only_has_one_node(new_bst):
    """Function that tests balance method of binary search tree returns zero
    if the tree only contains one node."""

    new_bst.insert(10)
    assert new_bst.balance() == 0


def test_balance_returns_pos_int_if_root_only_has_left(new_bst):
    """Function that tests balance method of binary search tree returns a
    positive integer if tree only has one root node with a left node."""

    new_bst.insert(10)
    new_bst.insert(8)
    assert new_bst.balance() == 1


def test_balance_returns_neg_int_if_root_only_has_right(new_bst):
    """Function that tests balance method of binary search tree returns a
    negative integer if tree only has one root node with a right node."""

    new_bst.insert(10)
    new_bst.insert(12)
    assert new_bst.balance() == -1


def test_pre_order_traversal_yields_correct_values(filled_bst):
    """Function that tests pre_order method of binary search tree yields the
    correct pre order traversal values."""

    assert next(filled_bst.pre_order()) == 10
    assert next(filled_bst.pre_order()) == 8
    assert next(filled_bst.pre_order()) == 6
    assert next(filled_bst.pre_order()) == 5
    assert next(filled_bst.pre_order()) == 7
    assert next(filled_bst.pre_order()) == 9
    assert next(filled_bst.pre_order()) == 12
    assert next(filled_bst.pre_order()) == 11
    assert next(filled_bst.pre_order()) == 15
    assert next(filled_bst.pre_order()) == 18
    assert filled_bst.traversal_list == []


def test_post_order_traversal_yields_correct_values(filled_bst):
    """Function that tests post_order method of binary search tree yields the
    correct post order traversal values."""

    assert next(filled_bst.post_order()) == 5
    assert next(filled_bst.post_order()) == 7
    assert next(filled_bst.post_order()) == 6
    assert next(filled_bst.post_order()) == 9
    assert next(filled_bst.post_order()) == 8
    assert next(filled_bst.post_order()) == 11
    assert next(filled_bst.post_order()) == 18
    assert next(filled_bst.post_order()) == 15
    assert next(filled_bst.post_order()) == 12
    assert next(filled_bst.post_order()) == 10
    assert filled_bst.traversal_list == []


def test_in_order_traversal_yields_correct_values(filled_bst):
    """Function that tests in_order method of binary search tree yields the
    correct in order traversal values."""

    assert next(filled_bst.in_order()) == 5
    assert next(filled_bst.in_order()) == 6
    assert next(filled_bst.in_order()) == 7
    assert next(filled_bst.in_order()) == 8
    assert next(filled_bst.in_order()) == 9
    assert next(filled_bst.in_order()) == 10
    assert next(filled_bst.in_order()) == 11
    assert next(filled_bst.in_order()) == 12
    assert next(filled_bst.in_order()) == 15
    assert next(filled_bst.in_order()) == 18
    assert filled_bst.traversal_list == []


def test_breadth_first_yields_correct_values(filled_bst):
    """Function that tests breadth_first method of binary search tree yields the
    correct breadth first traversal values."""

    assert next(filled_bst.breadth_first()) == 10
    assert next(filled_bst.breadth_first()) == 8
    assert next(filled_bst.breadth_first()) == 12
    assert next(filled_bst.breadth_first()) == 6
    assert next(filled_bst.breadth_first()) == 9
    assert next(filled_bst.breadth_first()) == 11
    assert next(filled_bst.breadth_first()) == 15
    assert next(filled_bst.breadth_first()) == 5
    assert next(filled_bst.breadth_first()) == 7
    assert next(filled_bst.breadth_first()) == 18
    assert filled_bst.traversal_list == []


def test_node_insert_creates_parent_relationship(new_bst):
    """Function that tests multiple inserts create proper child/parent
    relationship between applicable nodes."""
    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(12)
    new_bst.insert(15)
    new_bst.insert(6)
    new_bst.insert(9)
    new_bst.insert(11)
    assert new_bst.bst[0].parent is None
    assert new_bst.bst[1].parent.value == 10
    assert new_bst.bst[2].parent.value == 10
    assert new_bst.bst[3].parent.value == 12
    assert new_bst.bst[4].parent.value == 8
    assert new_bst.bst[5].parent.value == 8
    assert new_bst.bst[6].parent.value == 12


def test_delete_method_on_leaf_node(new_bst):
    """Function that tests delete method on binary search tree removes node and
    reassigns parent node pointer."""

    new_bst.insert(10)
    new_bst.insert(9)
    new_bst.insert(8)
    new_bst.insert(7)
    new_bst.delete(8)
    assert new_bst.bst[1].left.value == 7
    assert new_bst.bst[2].parent.value == 9
    assert new_bst.size() == 3
    assert len(new_bst.bst) == 3


def test_delete_method_on_node_with_two_children(filled_bst):
    """Function that tests delete method on binary search tree removes node and
    reassigns parent node pointer."""

    filled_bst.delete(12)
    assert filled_bst.bst[0].right.value == 11
    assert filled_bst.bst[5].parent.value == 10
    assert filled_bst.bst[5].right.value == 15
    assert filled_bst.bst[5].left.value is None
    assert filled_bst.size() == 9
    assert len(filled_bst.bst) == 9
