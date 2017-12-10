"""Module that contains an implementation of the Bubble Sort."""


def bubble_sort(lst):
    """Function that performs a bubble sort on a given list."""
    if not isinstance(lst, list):
        raise ValueError('Input must be a list.')
    if not all(isinstance(item, (str, float, int)) for item in lst):
        raise ValueError('Items in list must be strings, integers, or floats.')
    for idx in range(len(lst)-1, 0, -1):
        print(lst[idx])
        for i in range(idx):
            if lst[i] > lst[i + 1]:
                val = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = val
    return lst


if __name__ == '__main__':
    import timeit
