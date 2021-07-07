"""Find and return three largest numbers in array.

Size of array is min: 3
"""
from random import randint


"""Create test array."""
array_in = [randint(-1000, 1000) for _ in range(3, randint(3, 14))]


def three_largest(array_1):
    """Return three largest"""
    return [find_largest(array_1) for _ in range(3)]


def find_largest(array):
    """Return largest number and remove from array."""
    max_num = max(array)
    idx = array.index(max_num)

    return array.pop(idx)


if __name__ == '__main__':
    largest = three_largest(array_in)
    print(largest)
