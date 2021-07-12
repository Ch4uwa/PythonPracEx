phrase = 'xyz'
key = 2

alphabet = 26


def caesar_cipher_encryptor(phrase, key):
    new_phrase = []
    new_key = key % alphabet
    for letter in phrase:
        new_phrase.append(get_new_letter(letter, new_key))
    return "".join(new_phrase)


def get_new_letter(letter, newkey):
    new_letter_code = ord(letter) + newkey
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)


if __name__ == '__main__':
    print(caesar_cipher_encryptor(phrase, key))
