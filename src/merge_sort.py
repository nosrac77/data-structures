"""Module containing a function that implements the merge sort."""


def merge_sort(lst):
    """Function that implements the merge sort."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (float, int, str)) for item in lst):
        raise ValueError('Items in list must be integers or floats.')
    if len(lst) <= 1:
        return lst
    list_left = [x for x in lst[:len(lst) // 2]]
    merge_sort(list_left)
    list_right = [x for x in lst[len(lst) // 2:]]
    merge_sort(list_right)
    left_idx = 0
    right_idx = 0
    lst_idx = 0
    left_length = len(list_left)
    right_length = len(list_right)
    while left_idx < left_length and right_idx < right_length:
        if list_left[left_idx] < list_right[right_idx]:
            lst[lst_idx] = list_left[left_idx]
            left_idx += 1
        else:
            lst[lst_idx] = list_right[right_idx]
            right_idx += 1
        lst_idx += 1

    while left_idx < left_length:
        lst[lst_idx] = list_left[left_idx]
        lst_idx += 1
        left_idx += 1

    while right_idx < right_length:
        lst[lst_idx] = list_right[right_idx]
        lst_idx += 1
        right_idx += 1
    return lst


if __name__ == '__main__':  # pragma no cover
    import timeit

    opening = """

    The merge sort accomplishes it's sort by dividing the entire list into
    several smaller subsets of the list. It does this recursively, continuing
    to divide until every value in the list is in it's own separate "left" or
    "right" list. At this point, the left and right list values are compared
    to one another and the list from which the two left and right lists spawned
    is sorted based upon the comparisons. This acts as a "merge" of the main
    list's left and right lists. This process continues until the final two
    left and right lists are merged, creating one final sorted list with values
    from left to right, lowest to highest.

    At worst, the merge sort has a time complexity of O(n log n). Below is an
    example of the merge sort at it's worst by being given a list that forces
    a check and iteration over every value in the list through every layer of
    the merge process.

    Input: worst_case_list = [4, 0, 6, 2, 5, 1, 7, 3]
    Output: [0, 1, 2, 3, 4, 5, 6, 7]

    """

    worst_case_list = [4, 0, 6, 2, 5, 1, 7, 3]

    print(opening)
    print('Time to achieve Output: ', timeit.repeat('merge_sort(worst_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_1 = """

    As you can see, it's worst case is a lengthy process. The next case is the
    best case for the merge sort. It is shown below.

    Input: best_case_list = [1, 2]
    Output: [1, 2]

    """

    best_case_list = [1, 2]

    print(explanation_1)
    print('Time to achieve Output: ', timeit.repeat('merge_sort(best_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_2 = """

    Above is a demonstration of the merge sort in it's best case,
    where only two items exist pre-sorted in ascending order from left to
    right.

    To clarify, the two better cases for the merge sort's time complexity
    would be if there was only one item in the list or if the list were empty
    from the start, in which case the function would simply return the list
    before any recurisve or iterative processes are triggered. I chose to
    demonstrate the best case above to give the function at least two items to
    compare.

    Thanks for reading!

    """

    print(explanation_2)
