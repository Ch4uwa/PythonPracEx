array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                temp = array[i] + array[j]
                if temp == targetSum:
                    return [array[i] + array[j]]
    return []


print(twoNumberSum(array, targetSum))
