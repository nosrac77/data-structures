"""Module containing a function that implements the insertion sort."""


def insertion_sort(lst):
    """Function that implements the insertion sort."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (float, int)) for item in lst):
        raise ValueError('Items in list must be integers, or floats.')
    for idx, num in enumerate(lst):
        idx_2 = idx
        curr_val = num
        while lst[idx_2 - 1] > curr_val and idx_2 != 0:
            lst[idx_2] = lst[idx_2 - 1]
            idx_2 -= 1
        lst[idx_2] = curr_val
    return lst


if __name__ == '__main__':  # pragma no cover
    import timeit

    opening = """

    The insertion sort accomplishes it's sort by iterating through a list,
    creating a "subset" of that list with which to compare the other values in
    the list. It starts at the first index of the list, comparing it's value to
    item before it. The next item is then checked against the item before it,
    and the "subset" list continuosly sorts and "inserts" the other values
    until the entire list is completely sorted. If at any point the list value
    being iterated over is greater than the value before it, the current item's
    value becomes the previouus item's value, the index is lowered by one, and
    the loop continues until the previous item's value is no longer greater
    than the current item's value. The item at which this loop finally stops
    then assumes the value of the item in the current position in the for loop.
    This continues until every item is sorted by value, by lowest to greatest,
    from left to right.

    At worst, the insertion sort has a time complexity of O(n^2). This is due to
    the nature of how it accomplishes it's task. Every value encountered must
    be checked against it's previous value, and if the previous value is found
    to be greater than the current value, the current value must be, at worst,
    checked against every item in the subset before it. Below is an example of
    such a case.

    Input: worst_case_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """

    worst_case_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(opening)
    print('Time to achieve Output: ', timeit.repeat('insertion_sort(worst_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_1 = """

    Above is a demonstration of the insertion sort in it's worst case,
    where every item in the given list is sorted in descending order from left
    to right. The time it took, as shown above, is better than that of the
    bubble sort (even though their worst-case time complexities are the same).

    The next case is the best case for the insertion sort. It is shown below.

    Input: best_case_list = [1, 2]
    Output: [1, 2]

    """

    best_case_list = [1, 2]

    print(explanation_1)
    print('Time to achieve Output: ', timeit.repeat('insertion_sort(best_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_2 = """

    Above is a demonstration of the insertion sort in it's best case,
    where only two items exist pre-sorted in ascending order from left to
    right.

    To clarify, the two better cases for the insertion sort's time complexity
    would be if there was only one item in the list or if the list were empty
    from the start. I chose to demonstrate the best case above to give the
    function at least two items to compare.

    Thanks for reading!

    """

    print(explanation_2)
