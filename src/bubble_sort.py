"""Module that contains an implementation of the Bubble Sort."""


def bubble_sort(lst):
    """Function that performs a bubble sort on a given list."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (str, float, int)) for item in lst):
        raise ValueError('Items in list must be strings, integers, or floats.')
    for idx in range(len(lst)-1, 0, -1):
        for i in range(idx):
            if lst[i] > lst[i + 1]:
                val = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = val
    return lst


if __name__ == '__main__':  # pragma no cover
    import timeit

    opening = """

    The bubble sort accomplishes it's sort by iterating through a list and
    comparing values. It starts at the beginning of the list, checking the
    value of the list at the index of zero against it's neighbor located at the
    index plus one. If the beginning value is greater than it's neighbor's
    value, the two items are swapped. This occurs until every value has been
    effectively sorted, left to right, from smallest to biggest.

    At worst, the bubble sort has a time complexity of O(n^2). This is due to
    the nature of how it accomplishes it's task. At worst, every value must be
    moved for every number in the range of the list's length minus one.

    Input: worst_case_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """

    worst_case_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(opening)
    print('Time to achieve Output: ', timeit.repeat('bubble_sort(worst_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_1 = """

    Above is a demonstration of the bubble sort in it's worst case,
    where every item in the given list is sorted in descending order from left
    to right. Note: it was performed only once as it was clearly taxing on my
    hardware to repeat it!

    The next case will be easier on our hardware, as it is the best case for
    the bubble sort. It is shown below.

    Input: best_case_list = [1, 2]
    Output: [1, 2]

    """

    best_case_list = [1, 2]

    print(explanation_1)
    print('Time to achieve Output: ', timeit.repeat('bubble_sort(best_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_2 = """

    Above is a demonstration of the bubble sort in it's best case,
    where only two items exist pre-sorted in ascending order from left to
    right.

    To clarify, the two better cases for the bubble sort's time complexity
    would be if there was only one item in the list or if the list were empty
    from the start. I chose to demonstrate the best case above to give the
    function at least two items to compare.

    Thanks for reading!

    """

    print(explanation_2)
