string = 'AAAAABBBCCCCCCCCCCCCCCDDDDDD'


def run_length_encoding(string):
    encoded_str_char = []
    cur_run_len = 1

    for i in range(1, len(string)):
        cur_char = string[i]
        prev_char = string[i - 1]

        if cur_char != prev_char or cur_run_len == 9:
            encoded_str_char.append(str(cur_run_len))
            encoded_str_char.append(prev_char)
            cur_run_len = 0

        cur_run_len += 1

    encoded_str_char.append(str(cur_run_len))
    encoded_str_char.append(string[len(string) - 1])

    return "".join(encoded_str_char)


print(run_length_encoding(string))
