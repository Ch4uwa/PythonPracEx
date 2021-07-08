# coins = [5, 7, 1, 1, 2, 3, 22]
coins = [1, 2, 5]


def nonConstructibleChange(coins):
    minSumNotPossible = 0

    if len(coins) == 0:
        return minSumNotPossible + 1

    coins.sort()

    for coin in coins:
        if coin > minSumNotPossible + 1:
            return minSumNotPossible + 1

        minSumNotPossible += coin

    return minSumNotPossible + 1


print(nonConstructibleChange(coins))
