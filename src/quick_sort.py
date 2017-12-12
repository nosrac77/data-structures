"""Module that contains a function with an implementation of the quick sort."""


def quick_sort(lst):
    """Function that implements the quick sort."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (float, int, str)) for item in lst):
        raise ValueError('Items in list must be integers, strings, or floats.')
    if len(lst) <= 1:
        return
    pivot = lst[0]
    right_list = []
    left_list = []
    for val in lst[1:]:
        if val > pivot:
            right_list.append(val)
        else:
            left_list.append(val)
    quick_sort(left_list)
    quick_sort(right_list)
    return left_list + [pivot] + right_list


if __name__ == '__main__':  # pragma no cover
    import timeit

    opening = """

    The quick sort accomplishes it's sort by.

    At worst, the quick sort has a time complexity of O(n^2). This is due to
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
    print('Time to achieve Output: ', timeit.repeat('quick_sort(worst_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_1 = """

    Above is a demonstration of the quick sort in it's worst case,
    where every item in the given list is sorted in descending order from left
    to right. The time it took, as shown above, is better than that of the
    bubble sort (even though their worst-case time complexities are the same).

    The next case is the best case for the quick sort. It is shown below.

    Input: best_case_list = [1, 2]
    Output: [1, 2]

    """

    best_case_list = [1, 2]

    print(explanation_1)
    print('Time to achieve Output: ', timeit.repeat('quick_sort(best_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_2 = """

    Above is a demonstration of the quick sort in it's best case,
    where only two items exist pre-sorted in ascending order from left to
    right.

    To clarify, the two better cases for the quick sort's time complexity
    would be if there was only one item in the list or if the list were empty
    from the start. I chose to demonstrate the best case above to give the
    function at least two items to compare.

    Thanks for reading!

    """

    print(explanation_2)
