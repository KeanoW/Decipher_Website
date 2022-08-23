from random import sample, shuffle

def create_cipher_key_list(alphabet, phrase_alphabet):
    shuffle(alphabet)
    alphabet_removd_phrase_alph_list = []
    for letter in alphabet:
        if letter not in phrase_alphabet:
            alphabet_removd_phrase_alph_list.append(letter)

    cipher_key_list = alphabet_removd_phrase_alph_list[:len(phrase_alphabet)]

    return cipher_key_list

def remove_punctuation_marks(phrase):
    phrase = phrase.lower()
    phrase_list = list(phrase)
    new_phrase_list = []
    punctuation_list = ('!', ',', '?', '/', '.', ' ')

    for char in phrase_list:
        if char not in punctuation_list:
            new_phrase_list.append(char.lower())

    return new_phrase_list

def get_alphabet_of_phrase(func):
    """
    Pass list of phrase after punctuation removed methode
    """
    set_phrase_alphabet = list(set(func))
    set_phrase_alphabet.sort()

    return set_phrase_alphabet

def get_specail_chars(phrase):
    specail_chars = ["ai", "ea", "to", "ou", "th", "wh", "ss", "cc", "bb", "ll", "mm", "ck", "nn", "dd", "tt", "ee", "ff",
                     "gg", "gh", "kk", "oo", "pp", "iu", "an", "te", "st", "on", "ed", "er", "ry", "ng", "ph", "ch",
                     "un", "ou", "oe", "is", "ing", "able", "was", "the", "and", "tion", "who", "are", "too"]
    phrase_specail_char_list = []

    for char in range(len(phrase)):
        if char + 1 < len(phrase):
            chars_two = phrase[char] + phrase[char + 1]
            if chars_two in specail_chars:
                phrase_specail_char_list.append(chars_two)

        if char + 2 < len(phrase):
            chars_three = phrase[char] + phrase[char + 1] + phrase[char + 2]
            if chars_three in specail_chars:
                phrase_specail_char_list.append(chars_three)

        if char + 3 < len(phrase):
            chars_four = phrase[char] + phrase[char + 1] + phrase[char + 2] + phrase[char + 3]
            if chars_four in specail_chars:
                phrase_specail_char_list.append(chars_four)

    return phrase_specail_char_list

def create_cipher_phrase(phrase_list, cipher_dict):
    ciphered_phrase = []

    for letter in phrase_list:
        if letter.lower() in cipher_dict.keys():
            ciphered_phrase.append(cipher_dict.get(letter.lower()))
        else:
            ciphered_phrase.append(" ")
    return ciphered_phrase

def changed_dict(ciphered_char, replace_ciphered_char, cipher_dict):
    for k, v in cipher_dict.items():
        if v == ciphered_char:
            # if k != v:
            if replace_ciphered_char in list(cipher_dict.values()):
                keys = list(cipher_dict.keys())
                values = list(cipher_dict.values())

                value_index = values.index(replace_ciphered_char)
                key = keys[value_index]
                cipher_dict[key] = ciphered_char
                # cipher_dict[k] = replace_ciphered_char
            cipher_dict[k] = replace_ciphered_char
    return cipher_dict

def update_cipher(phrase_list, cipher_dict):
    new_ciphered_phrase = []
    for letter in phrase_list:
        if letter == " ":
            new_ciphered_phrase.append(" ")
        else:
            for k, v in cipher_dict.items():
                if letter.lower() == k:
                    new_ciphered_phrase.append(v)
                    continue
    return new_ciphered_phrase