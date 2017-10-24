"""Tests for Fibonacci, Lucas and sum_series functions."""
import pytest


def test_init():
    """Test if series imports."""
    from linked_list import LinkedList
    test_list = LinkedList()
    assert test_list.head is None


def test_push_method():
    """Test if push method adds new item to linked list."""
    from linked_list import LinkedList
    test_list = LinkedList()
    test_list.push(1)
    assert test_list.head.data == 1


def test_push_method_two():
    """Test if push method adds new item head, retains last head."""
    from linked_list import LinkedList
    test_list = LinkedList()
    test_list.push(1)
    test_list.push(2)
    assert test_list.head.next.data == 1


def test_pop_method_removes_head_value():
    """Tests if pop method returns the value contained in
    the head of the list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    l.pop()
    assert l.head is None


def test_pop_method_returns_head_value():
    """Tests if pop method returns the value contained in
    the head of the list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.pop() == 1


def test_pop_method_shifts_values_properly():
    """Tests if pop method returns the value contained in
    the head of the list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    l.push(2)
    assert l.pop() == 2
    assert l.head.data == 1


def test_node_has_attribute():
    """Test if new Node has attributes upon initialization."""
    from linked_list import Node
    test_node = Node(5, 5)
    assert hasattr(test_node, 'data')
    assert hasattr(test_node, 'next')


def test_list_has_attribute():
    """Test if new LinkedList has attribute upon initialization."""
    from linked_list import LinkedList
    test_linked_list = LinkedList(5)
    assert hasattr(test_linked_list, 'head')


def test_node_has_given_attribute_values():
    """Test if new Node has given attribute values."""
    from linked_list import Node
    test_node = Node(5, 5)
    assert test_node.data and test_node.next == 5


def test_linked_list_search_returns_none_if_empty():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


def test_linked_list_search_returns_node_val():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(1) == l.head


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_returns_random_node_val(n):
    """."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).data == search_me


def test_iterable_upon_initialization():
    """."""
    from linked_list import LinkedList
    a_list = [1, 2, 3]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item
