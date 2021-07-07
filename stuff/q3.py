def sortedSquaredArray(array):
    arrayOut = []
    for item in array:
        arrayOut.append(item * item)
    return arrayOut.sort(reverse=True)
