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

    gen = filled_bst.pre_order()
    assert list(gen) == [10, 8, 6, 5, 7, 9, 12, 11, 15, 18]


def test_pre_order_traversal_non_op_if_bst_empty(new_bst):
    """Function that tests pre_order method of binary search tree non-op if bst
    is empty."""

    gen = new_bst.pre_order()
    assert gen is None


def test_post_order_traversal_non_op_if_bst_empty(new_bst):
    """Function that tests post_order method of binary search tree non-op if
    bst is empty."""

    gen = new_bst.post_order()
    assert gen is None


def test_in_order_traversal_non_op_if_bst_empty(new_bst):
    """Function that tests in_order method of binary search tree non-op if
    bst is empty."""

    gen = new_bst.in_order()
    assert gen is None


def test_breadth_first_traversal_non_op_if_bst_empty(new_bst):
    """Function that tests breadth_first method of binary search tree non-op
    returns an empty generator object if bst is empty."""

    gen = new_bst.breadth_first()
    assert new_bst.root is None
    assert list(gen) == []


def test_post_order_traversal_yields_correct_values(filled_bst):
    """Function that tests post_order method of binary search tree yields the
    correct post order traversal values."""

    gen = filled_bst.post_order()
    assert list(gen) == [5, 7, 6, 9, 8, 11, 18, 15, 12, 10]


def test_in_order_traversal_yields_correct_values(filled_bst):
    """Function that tests in_order method of binary search tree yields the
    correct in order traversal values."""

    gen = filled_bst.in_order()
    assert list(gen) == [5, 6, 7, 8, 9, 10, 11, 12, 15, 18]


def test_breadth_first_yields_correct_values(filled_bst):
    """Function that tests breadth_first method of binary search tree yields the
    correct breadth first traversal values."""

    gen = filled_bst.breadth_first()
    assert list(gen) == [10, 8, 12, 6, 9, 11, 15, 5, 7, 18]


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

    new_bst.insert(12)
    new_bst.insert(10)
    new_bst.insert(11)
    new_bst.insert(7)

    new_bst.delete(7)

    assert new_bst.bst[1].value == 10
    assert new_bst.bst[1].parent.value == 12
    assert new_bst.bst[1].right.value == 11
    assert new_bst.bst[1].left is None
    assert new_bst.size() == 3
    assert len(new_bst.bst) == 3

    new_bst.delete(11)

    assert new_bst.bst[1].value == 10
    assert new_bst.bst[1].parent.value == 12
    assert new_bst.bst[1].right is None
    assert new_bst.bst[1].left is None
    assert new_bst.size() == 2
    assert len(new_bst.bst) == 2


def test_delete_method_on_node_with_two_children(new_bst):
    """Function that tests delete method on binary search tree removes node and
    reassigns parent node pointer."""

    new_bst.insert(100)
    new_bst.insert(94)
    new_bst.insert(50)
    new_bst.insert(49)
    new_bst.insert(75)
    new_bst.insert(74)
    new_bst.insert(73)
    new_bst.insert(72)
    new_bst.insert(71)
    new_bst.insert(70)
    new_bst.delete(50)

    assert len(new_bst.bst) == 9
    assert new_bst.size() == 9
    assert new_bst.bst[2].value == 70
    assert new_bst.bst[2].left.value == 49
    assert new_bst.bst[2].right.value == 75
    assert new_bst.bst[2].parent.value == 94


def test_delete_method_node_has_2_children_replacement_node_has_right(new_bst):
    """Function that tests delete method on binary search tree removes node and
    reassigns parent node pointer."""

    new_bst.insert(100)
    new_bst.insert(94)
    new_bst.insert(50)
    new_bst.insert(49)
    new_bst.insert(80)
    new_bst.insert(74)
    new_bst.insert(73)
    new_bst.insert(70)
    new_bst.insert(72)
    new_bst.insert(71)
    new_bst.delete(50)

    assert len(new_bst.bst) == 9
    assert new_bst.size() == 9
    assert new_bst.bst[2].value == 70
    assert new_bst.bst[2].left.value == 49
    assert new_bst.bst[2].right.value == 80
    assert new_bst.bst[2].parent.value == 94
    assert new_bst.bst[7].parent.value == 73
    assert new_bst.bst[7].value == 72
    assert new_bst.bst[7].left.value == 71
    assert new_bst.bst[7].right is None


def test_delete_method_node_has_2_children_no_right_left_child(new_bst):
    """Function that tests delete method on binary search tree removes node and
    reassigns parent node pointer."""

    new_bst.insert(100)
    new_bst.insert(94)
    new_bst.insert(50)
    new_bst.insert(49)
    new_bst.insert(80)
    new_bst.insert(81)

    new_bst.delete(50)

    assert len(new_bst.bst) == 5
    assert new_bst.size() == 5
    assert new_bst.bst[3].value == 80
    assert new_bst.bst[3].left.value == 49
    assert new_bst.bst[3].right.value == 81
    assert new_bst.bst[3].parent.value == 94


def test_delete_method_on_node_with_one_child(new_bst):
    """Function that tests delete method on binary search tree removes node and
    reassigns parent node pointer."""

    new_bst.insert(10)
    new_bst.insert(9)
    new_bst.insert(8)
    new_bst.insert(7)
    new_bst.delete(8)
    assert new_bst.bst[2].value == 7
    assert new_bst.bst[2].parent.value == 9
    assert new_bst.bst[2].left is None
    assert new_bst.bst[2].right is None
    assert len(new_bst.bst) == 3
    assert new_bst.size() == 3

    new_bst.insert(11)
    new_bst.insert(12)
    new_bst.insert(13)
    new_bst.insert(14)
    new_bst.delete(12)
    assert new_bst.bst[4].value == 13
    assert new_bst.bst[4].parent.value == 11
    assert new_bst.bst[4].left is None
    assert new_bst.bst[4].right.value == 14
    assert len(new_bst.bst) == 6
    assert new_bst.size() == 6
