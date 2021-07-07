"""Create test arrays.

Size of array is min: 3 max: 13
"""

from random import randint


def makeArray():
    """Create an list/array with random length and numbers.
    
    length is 3 -- 13
    numbers is -1000 -- 1000

    Returns:
        list
    """
    array_in = [randint(-1000, 1000) for _ in range(3, randint(3, 14))]
    return array_in
