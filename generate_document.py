characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


def generateDocument(characters, document):
    for character in document:
        doc_freq = count_char_freq(character, document)
        char_freq = count_char_freq(character, characters)
        if doc_freq > char_freq:
            return False

    return True


def count_char_freq(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency


def generate_document(characters, document):
    character_counts = {}

    for character in characters:
        if character not in character_counts:
            character_counts[character] = 0

        character_counts[character] += 1

    for character in document:
        if character not in character_counts or character_counts[character] == 0:
            return False

        character_counts[character] -= 1

    return True


print(generate_document(characters, document))
# print(generateDocument(characters, document))
