"""BubbleSort."""
import makearray

my_array = makearray.make_array()


def bubbleSort(array):
    """Sort array by comparing left > right. Swap place if true."""
    isSorted = False
    counter = 0
    while not isSorted:
        # while array is not sorted
        isSorted = True
        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                # if we get here array is not sorted
                swap(idx, idx + 1, array)
                isSorted = False
        counter += 1

    return array


def swap(i, j, array):
    """Swap numbers."""
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    print(bubbleSort(my_array))
