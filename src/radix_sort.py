"""Module that contains a function with an implementation of the radix sort."""


def radix_sort(lst):
    """Function that implements the radix sort."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (int)) for item in lst):
        raise ValueError('Items in list must be integers, strings, or floats.')
    if len(lst) <= 1:
        return

    max_int = len(str(max(lst)))
    counter = 1

    while counter <= max_int:
        lst = _radix_helper(lst, counter, max_int)
        counter += 1
    return lst


def _radix_helper(lst, counter, max_int):
    """Helper function for Radix Sort."""

    buckets = [[] for x in range(10)]

    for val in lst:
        try:
            buckets[int(str(val)[-counter])].append(val)
        except IndexError:
            buckets[0].append(val)
    del lst[:]

    for bucket in buckets:
        lst += bucket
    return lst


if __name__ == '__main__':  # pragma no cover
    import timeit

    opening = """

    The radix sort accomplishes it's task by continuously repeating a two step
    process until the list has been fully sorted. The first step of the process
    is to sort the list into another list, which contain 10 "buckets" (other
    lists, in this case). List numbers are initially placed in their buckets
    based upon their ones place value. The second step involves replacing the
    original list with the values contained in the buckets. This process then
    repeats, except the numbers now get sorted by their tenths place value, and
    then their hundreths place value, and so on until no numbers have that
    place value.

    At worst, the radix sort has a time complexity of O(nd). The run-time for
    a properly implemented radix sort is linear, always maintaining O(nd). A
    worst-case scenario for this sort would be if all numbers in the list
    never exceed the ones place for the exception of one large number. This
    would naturally reduce efficiency by requiring the function to iterate
    for as many times as there are place-values for the largest number, even
    though the list is essentially already sorted after the first iteration
    over the numbers with only ones-place values. Below is an example.

    Input: worst_case_list = [100000, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 100000]

    """

    worst_case_list = [100000, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(opening)
    print('Time to achieve Output: ', timeit.repeat('radix_sort(worst_case_list)',
                                                    repeat=1,
                                                    globals=globals()))

    explanation_1 = """

    As you could probably tell, the time taken is excessive.

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
