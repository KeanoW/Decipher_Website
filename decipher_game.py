import cipher_functions as ciph_function
import api
import time
phrase = api.get_quote(type="q")
# phrase = "Trust in the Lord with all your heart and lean not on your own understanding, in all your ways submit to  \
#          him and He will make your path straight."
print(phrase)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "*", "/", ",", "+", "&", "^", "'", "(", ")", "=", ";", "{", "}", "[", "]", "?",
            "=", "_", ">", "<", ":", "-", "!", "#", "@", "%", " "]

phrase_alphabet = ciph_function.get_alphabet_of_phrase(ciph_function.remove_punctuation_marks(phrase)) +  ciph_function.get_specail_chars(phrase)
cipher_dict = dict(zip(phrase_alphabet, ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)))
# print(cipher_dict)
filtered_phrase_list = ciph_function.remove_punctuation_marks(phrase)
ciphered_phrase = ciph_function.create_cipher_phrase(filtered_phrase_list, cipher_dict)
count = 0
modified_ciphered_phrase = []
modified_dict = {}
ciph_char = False
repl_ciph_char = False
# start_time = time.time()
while(True):
    if count < 1:
        ciphered_phrase_str = "".join(map(str, ciphered_phrase))
        print(ciphered_phrase_str)
        count = 1

    ciphered_char = input("Character you want to change: ").lower()

    if ciphered_char not in alphabet:
        print("Not Valid character! Try Again")
        ciphered_char = input("Character you want to change: ").lower()
    else:
        ciph_char = True

    replace_ciphered_char = input("New character: ").lower()

    if replace_ciphered_char not in alphabet:
        print("Not Valid character! Try Again")
        replace_ciphered_char = input("New character: ").lower()
    else:
        repl_ciph_char = True

    if ciph_char is True and repl_ciph_char is True:
        modified_dict = ciph_function.changed_dict(ciphered_char, replace_ciphered_char, cipher_dict)
        modified_ciphered_phrase = ciph_function.update_cipher(filtered_phrase_list, modified_dict)

        ciphered_phrase_str = "".join(map(str, modified_ciphered_phrase))
        print(ciphered_phrase_str)

    if list(modified_dict.values()) == phrase_alphabet:
        print("Phrase deciphered!")
        auther = api.get_quote(type="a")
        # auther = "Solomon"
        print(f"{phrase} - {auther}")
        break
        end_time = time.time()
