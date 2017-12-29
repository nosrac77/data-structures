"""Module that contains functions which test the radix_sort function."""
import pytest
from random import randint
from radix_sort import radix_sort


@pytest.fixture
def BIG_INT_LIST():
    """Fixture that returns a large list of numbers with which to use for
    parametrization."""

    BIG_LIST = []

    for i in range(0, 201):
        problem = [randint(0, 100) for x in range(0, 21)]
        solution = sorted(problem)
        BIG_LIST.append((problem, solution))

    return BIG_LIST


@pytest.fixture
def BIG_SORTED_INT_LIST():
    """Fixture that returns a large list of numbers with which to use for
    parametrization."""

    BIG_LIST = []

    for i in range(0, 201):
        problem = sorted([x for x in range(0, 21)])
        solution = problem
        BIG_LIST.append((problem, solution))

    return BIG_LIST


@pytest.mark.parametrize('bad_input', [
                                       5,
                                       'a',
                                       2.5,
                                       (1, 2, 3),
                                       {'a': 5},
                                       {1, 2, 3}])
def test_radix_sort_raises_valueerror_if_input_not_list_type(bad_input):
    """Function that tests the radix_sort function will raise a ValueError if
    the given input is not a list."""

    assert isinstance(bad_input, list) is False
    with pytest.raises(ValueError):
        assert radix_sort(bad_input)


@pytest.mark.parametrize('lst_input, output', BIG_INT_LIST())
def test_radix_sort_return_sorted_list_int(lst_input, output):
    """Function that tests the radix_sort function returns the list with the
    correctly sorted values if given whole integers."""

    assert radix_sort(lst_input) == output


@pytest.mark.parametrize('lst_input, output', BIG_SORTED_INT_LIST())
def test_radix_sort_doesnt_alter_presorted_input(lst_input, output):
    """Function that tests the radix_sort function returns the list with the
    correctly sorted values if given whole integers."""

    assert radix_sort(lst_input) == output


def test_radix_sort_raises_valueerror_if_given_list_contains_set():
    """Function that tests the radix_sort function will raise a ValueError if
    given a list that contains a set."""

    with pytest.raises(ValueError):
        assert radix_sort([{1, 2, 3}])


def test_radix_sort_raises_valueerror_if_given_list_contains_list():
    """Function that tests the radix_sort function will raise a ValueError if
    given a list that contains a list."""

    with pytest.raises(ValueError):
        assert radix_sort([[1, 2, 3]])


def test_radix_sort_raises_valueerror_if_given_list_contains_dictionary():
    """Function that tests the radix_sort function will raise a ValueError if
    given a list that contains a dictionary."""

    with pytest.raises(ValueError):
        assert radix_sort([{'a': 1}])


def test_radix_sort_raises_valueerror_if_given_list_contains_tuple():
    """Function that tests the radix_sort function will raise a ValueError if
    given a list that contains a tuple."""

    with pytest.raises(ValueError):
        assert radix_sort([(1, 2, 3)])


def test_radix_sort_raises_valueerror_if_given_list_contains_string():
    """Function that tests the radix_sort function will raise a ValueError if
    given a list that contains a string."""

    with pytest.raises(ValueError):
        assert radix_sort(['a', 'b', 'c'])


def test_radix_sort_raises_valueerror_if_given_list_contains_float():
    """Function that tests the radix_sort function will raise a ValueError if
    given a list that contains a float."""

    with pytest.raises(ValueError):
        assert radix_sort([1.0, 2.0, 3.0])
