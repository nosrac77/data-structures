"""Module that contains a function with an implementation of the radix sort."""


def radix_sort(lst):
    """Function that implements the radix sort."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (float, int, str)) for item in lst):
        raise ValueError('Items in list must be integers, strings, or floats.')
    if len(lst) <= 1:
        return

    buckets = [[]] * 10

    counter = 0

    for val in lst:
            buckets[int(str(val)[-counter])].append(val)
            print(buckets)


if __name__ == '__main__':  # pragma no cover
    import timeit

    opening = """

    The radix sort accomplishes it's sort by dividing the list into several
    halves, which are determined by value comparisons around a pivot point
    (in my case the pivot is the value of the given list at index zero).
    Through repeatedly using a pivot point with which to compare the values of
    the list, as well as it's subsets, the only step left is to add the subsets
    together with the pivot point to return a newly sorted list.

    At worst, the radix sort has a time complexity of O(n^2). This can occur a
    few different ways, all stemming from how the pivot point is chosen (as
    well as how the values in the given list are placed). Below is one such
    occurence.

    Input: worst_case_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """

    worst_case_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(opening)
    print('Time to achieve Output: ', timeit.repeat('radix_sort(worst_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_1 = """

    Above is a demonstration of the radix sort in it's worst case,
    where every item in the given list is sorted in descending order from left
    to right. The time it took, as shown above, is better than that of the
    bubble sort (even though their worst-case time complexities are the same).

    The next case is the best case for the radix sort. It is shown below.

    Input: best_case_list = [1, 2]
    Output: [1, 2]

    """

    best_case_list = [1, 2]

    print(explanation_1)
    print('Time to achieve Output: ', timeit.repeat('radix_sort(best_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_2 = """

    Above is a demonstration of the radix sort in it's best case,
    where only two items exist pre-sorted in ascending order from left to
    right.

    To clarify, the two better cases for the radix sort's time complexity
    would be if there was only one item in the list or if the list were empty
    from the start. I chose to demonstrate the best case above to give the
    function at least two items to compare.

    Thanks for reading!

    """

    print(explanation_2)
