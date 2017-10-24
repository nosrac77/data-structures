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
    assert Stack({'hello': 'world'}) == ValueError


# def test_push_method():
#     """Test if push method adds new item to linked list."""
#     from linked_list import LinkedList
#     test_list = LinkedList()
#     test_list.push(1)
#     assert test_list.head.data == 1


# def test_push_method_two():
#     """Test if push method adds new item head, retains last head."""
#     from linked_list import LinkedList
#     test_list = LinkedList()
#     test_list.push(1)
#     test_list.push(2)
#     assert test_list.head.next.data == 1


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