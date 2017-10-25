"""Tests for Stack."""

import pytest


def test_init_none():
    """Test if stack imports with None."""
    from stack import Stack
    s = Stack()
    assert s.list.head.data is None


def test_init_iterable():
    """Test if stack imports with an iterable input."""
    from stack import Stack
    s = Stack([1])
    assert s.list.head.data == 1


def test_init_non_iterable():
    """Test if stack imports with non-iterable input."""
    from stack import Stack
    with pytest.raises(ValueError):
        Stack({'hello': 'world'})


def test_stack_push_method():
    """Test if push method adds new item to stack."""
    from stack import Stack
    s = Stack()
    s.push(4)
    assert s.list.head.data == 4


def test_stack_push_and_pop():
    """Test if push and pop methods work together."""
    from stack import Stack
    s = Stack()
    s.push(4)
    assert s.pop() == 4
    assert s.list.head.data is None


def test_stack_pop_extreme():
    """Test if pop methods work with lots of vals."""
    from stack import Stack
    s = Stack([1, 2, 3])
    s.pop()
    assert s.pop() == 2


def test_stack_pop_from_empty():
    """Test Error handle when popping from empty Stack."""
    from stack import Stack
    with pytest.raises(IndexError):
        s = Stack()
        s.pop()


def test_stack_len():
    """Test __len__ method of stack."""
    from stack import Stack
    s = Stack([1, 2, 3])
    assert len(s) == 3


def test_stack_len_zero():
    """Test __len__ method of stack when len is zero."""
    from stack import Stack
    s = Stack()
    assert len(s) == 1

# def test_pop_method_removes_head_value():
#     """Tests if pop method returns the value contained in
#     the head of the list."""
#     from linked_list import LinkedList
#     l = LinkedList()
#     l.push(1)
#     l.pop()
#     assert l.head is None


# def test_pop_method_returns_head_value():
#     """Tests if pop method returns the value contained in
#     the head of the list."""
#     from linked_list import LinkedList
#     l = LinkedList()
#     l.push(1)
#     assert l.pop() == 1


# def test_pop_method_shifts_values_properly():
#     """Tests if pop method returns the value contained in
#     the head of the list."""
#     from linked_list import LinkedList
#     l = LinkedList()
#     l.push(1)
#     l.push(2)
#     assert l.pop() == 2
#     assert l.head.data == 1