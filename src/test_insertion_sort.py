"""Module that contains functions which test the insertion_sort function."""
import pytest
from insertion_sort import insertion_sort


@pytest.mark.parametrize('bad_input', ['string',
                                       5,
                                       2.5,
                                       (1, 2, 3),
                                       {'a': 5},
                                       {1, 2, 3}])
def test_insertion_sort_raises_valueerror_if_input_not_list_type(bad_input):
    """Function that tests the insertion_sort function will raise a ValueError if
    the given input is not a list."""

    assert isinstance(bad_input, list) is False
    with pytest.raises(ValueError):
        assert insertion_sort(bad_input)


TEST_LISTS_INT = [
             ([1, 2, 5, 4, 3, 7, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
             ([10, 27, 51, 11, 3, 88, 29, 7], [3, 7, 10, 11, 27, 29, 51, 88]),
             ([401, 301, 201, 101, 106, 206, 306], [101, 106, 201, 206, 301, 306, 401])
]


@pytest.mark.parametrize('lst_input, output', TEST_LISTS_INT)
def test_insertion_sort_return_sorted_list_int(lst_input, output):
    """Function that tests the insertion_sort function returns the list with the
    correctly sorted values if given whole integers."""

    assert insertion_sort(lst_input) == output


TEST_LISTS_FLOAT = [
             ([.1, .2, .5, .4, .3, .7, .6, .8], [.1, .2, .3, .4, .5, .6, .7, .8]),
             ([.10, .27, .51, .11, .33, .88, .29, .70], [.10, .11, .27, .29, .33, .51, .70, .88]),
             ([.401, .301, .201, .101, .106, .206, .306], [.101, .106, .201, .206, .301, .306, .401])
]


@pytest.mark.parametrize('lst_input, output', TEST_LISTS_FLOAT)
def test_insertion_sort_return_sorted_list_float(lst_input, output):
    """Function that tests the insertion_sort function returns the list with the
    correctly sorted values if given floats."""

    assert insertion_sort(lst_input) == output


def test_insertion_sort_raises_valueerror_if_given_list_contains_set():
    """Function that tests the insertion_sort function will raise a ValueError if
    given a list that contains a set."""

    with pytest.raises(ValueError):
        assert insertion_sort([{1, 2, 3}])


def test_insertion_sort_raises_valueerror_if_given_list_contains_list():
    """Function that tests the insertion_sort function will raise a ValueError if
    given a list that contains a list."""

    with pytest.raises(ValueError):
        assert insertion_sort([[1, 2, 3]])


def test_insertion_sort_raises_valueerror_if_given_list_contains_dictionary():
    """Function that tests the insertion_sort function will raise a ValueError if
    given a list that contains a dictionary."""

    with pytest.raises(ValueError):
        assert insertion_sort([{'a': 1}])


def test_insertion_sort_raises_valueerror_if_given_list_contains_tuple():
    """Function that tests the insertion_sort function will raise a ValueError if
    given a list that contains a tuple."""

    with pytest.raises(ValueError):
        assert insertion_sort([(1, 2, 3)])
