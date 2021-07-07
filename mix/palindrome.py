a = ['madam', 'car', 'balloon', 'table', 'mam', 'rotator', 'racecar']


def palindromeScore(a):
    a = a.lower()
    score = 0
    r_a = a[::-1]

    if a != r_a:
        for i in range(len(a)):
            if r_a[i] != a[i]:
                score += 1

    return 'palindrome' if score == 0 else score


# Or
# if palindrome: 0 | if not palindrome: -1
def palindromeShort(word):

    for j in range(len(word)):
        print(f'{word[j]} is not a palindrome.') if word[j].lower().find(
            word[j][::-1].lower()) else print(f'{word[j]} is a palindrome.')


if __name__ == '__main__':
    # for i in a:
    #     print(f'{i}: {palindromeScore(i)}')
    # palindromeShort(a)
    pass
