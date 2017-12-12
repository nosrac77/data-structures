"""Module that contains functions which test the quick_sort function."""
import pytest
from quick_sort import quick_sort


@pytest.fixture
def BIG_INT_LIST():
    """Fixture that returns a large list of numbers with which to use for
    parametrization."""

    BIG_LIST = []

    for i in range(0, 201):
        problem = [x for x in range(0, 21)]
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


@pytest.fixture
def BIG_FLOAT_LIST():
    """Fixture that returns a large list of numbers with which to use for
    parametrization."""

    BIG_LIST = []

    for i in range(0, 201):
        problem = [float(x) for x in range(0, 21)]
        solution = sorted(problem)
        BIG_LIST.append((problem, solution))

    return BIG_LIST


@pytest.fixture
def BIG_STRING_LIST():
    """Fixture that returns a large list of numbers with which to use for
    parametrization."""

    BIG_LIST = []

    for i in range(0, 201):
        problem = [chr(x) for x in range(97, 125)]
        solution = sorted(problem)
        BIG_LIST.append((problem, solution))

    return BIG_LIST


@pytest.mark.parametrize('bad_input', [
                                       5,
                                       2.5,
                                       (1, 2, 3),
                                       {'a': 5},
                                       {1, 2, 3}])
def test_quick_sort_raises_valueerror_if_input_not_list_type(bad_input):
    """Function that tests the quick_sort function will raise a ValueError if
    the given input is not a list."""

    assert isinstance(bad_input, list) is False
    with pytest.raises(ValueError):
        assert quick_sort(bad_input)


@pytest.mark.parametrize('lst_input, output', BIG_INT_LIST())
def test_quick_sort_return_sorted_list_int(lst_input, output):
    """Function that tests the quick_sort function returns the list with the
    correctly sorted values if given whole integers."""

    assert quick_sort(lst_input) == output


@pytest.mark.parametrize('lst_input, output', BIG_SORTED_INT_LIST())
def test_quick_sort_doesnt_alter_presorted_input(lst_input, output):
    """Function that tests the quick_sort function returns the list with the
    correctly sorted values if given whole integers."""

    assert quick_sort(lst_input) == output


@pytest.mark.parametrize('lst_input, output', BIG_FLOAT_LIST())
def test_quick_sort_return_sorted_list_float(lst_input, output):
    """Function that tests the quick_sort function returns the list with the
    correctly sorted values if given floats."""

    assert quick_sort(lst_input) == output


@pytest.mark.parametrize('lst_input, output', BIG_STRING_LIST())
def test_quick_sort_return_sorted_list_string(lst_input, output):
    """Function that tests the quick_sort function returns the list with the
    correctly sorted values if given strings."""

    assert quick_sort(lst_input) == output


def test_quick_sort_raises_valueerror_if_given_list_contains_set():
    """Function that tests the quick_sort function will raise a ValueError if
    given a list that contains a set."""

    with pytest.raises(ValueError):
        assert quick_sort([{1, 2, 3}])


def test_quick_sort_raises_valueerror_if_given_list_contains_list():
    """Function that tests the quick_sort function will raise a ValueError if
    given a list that contains a list."""

    with pytest.raises(ValueError):
        assert quick_sort([[1, 2, 3]])


def test_quick_sort_raises_valueerror_if_given_list_contains_dictionary():
    """Function that tests the quick_sort function will raise a ValueError if
    given a list that contains a dictionary."""

    with pytest.raises(ValueError):
        assert quick_sort([{'a': 1}])


def test_quick_sort_raises_valueerror_if_given_list_contains_tuple():
    """Function that tests the quick_sort function will raise a ValueError if
    given a list that contains a tuple."""

    with pytest.raises(ValueError):
        assert quick_sort([(1, 2, 3)])
