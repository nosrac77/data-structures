"""Tests for Fibonacci, Lucas and sum_series functions."""


import pytest


def test_init():
    """Test if series imports."""
    from linked_list import LinkedList
    test_list = LinkedList()
    assert test_list.head is None


def test_push():
    """Testing push method of LinkedList class."""
    from linked_list import LinkedList
    from linked_list import Node
    test_list = LinkedList()
    test_list.push(5)
    assert test_list.head == 5


# @pytest.mark.parametrize('n, result', FIB_NUMBERS)
# def test_fibonacci(n, result):
#     """Test for fibonacci sequence."""
#     from series import fibonacci
#     assert fibonacci(n) == result


# @pytest.mark.parametrize('n, result', LUCAS_NUMBERS)
# def test_lucas(n, result):
#     """Test for lucas sequence."""
#     from series import lucas
#     assert lucas(n) == result


# @pytest.mark.parametrize('n, op1, op2, result', SUM_NUMBERS)
# def test_sum_series(n, op1, op2, result):
#     """Test the sum function."""
#     from series import sum_series
#     assert sum_series(n, op1, op2) == result
