def sorted_squared_array(array):
    arrayOut = []
    for item in array:
        arrayOut.append(item * item)
    return arrayOut.sort(reverse=True)
