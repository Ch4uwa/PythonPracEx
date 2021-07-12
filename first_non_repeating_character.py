string = "abcdcaf"


def first_non_repeating_character(string):
    for i in string:
        if string.count(i) == 1:
            return string.index(i)

    return -1


print(first_non_repeating_character(string))
