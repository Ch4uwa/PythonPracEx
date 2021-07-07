# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array, multiplier=1):
    # Write your code here.
    total = 0
    for ele in array:
        if type(ele) is list:
            total += productSum(ele, multiplier + 1)
        else:
            total += ele

    return total * multiplier


print(productSum(array=array))
