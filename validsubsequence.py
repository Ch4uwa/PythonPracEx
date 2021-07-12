array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(array, sequence):
    subId = 0
    for item in array:
        if sequence[subId] == item:
            subId += 1
    return (subId == len(sequence))


print(isValidSubsequence(array, sequence))
