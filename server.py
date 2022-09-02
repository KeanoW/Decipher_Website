from flask import Flask, render_template, request, redirect
import cipher_functions as ciph_function
import api

phrase = api.get_quote(type="q")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "*", "/", ",", "+", "&", "^", "'", "(", ")", "=", ";", "{", "}", "[", "]", "?",
            "=", "_", ">", "<", ":", "-", "!", "#", "@", "%", " "]

phrase_alphabet = ciph_function.get_alphabet_of_phrase(ciph_function.remove_punctuation_marks(phrase))
cipher_dict = dict(zip(phrase_alphabet, ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)))
cipher_chars = ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)
filtered_phrase_list = ciph_function.remove_punctuation_marks(phrase)
ciphered_phrase = ciph_function.create_cipher_phrase(filtered_phrase_list, cipher_dict)
ciphered_phrase_str = "".join(map(str, ciphered_phrase))
ciph_char = True
app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("templates/index.html")


@app.route("/")
def home():
    return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, ciph_char=ciph_char)

@app.route("/cipher")
def cipher():
    return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, ciph_char=ciph_char)

@app.route('/decipher', methods=['POST', 'GET'])
def decipher():
    ciph_char = False
    if request.method == 'POST':
        data = request.form.to_dict()
        ciphered_char = data['ciph_char'].lower()

        if ciphered_char in alphabet:
            ciph_char = True

        replace_ciphered_char = data['new_char'].lower()

        if ciph_char is True:
            modified_dict = ciph_function.changed_dict(ciphered_char, replace_ciphered_char, cipher_dict)
            modified_ciphered_phrase = ciph_function.update_cipher(filtered_phrase_list, modified_dict)

        ciphered_phrase_str = "".join(map(str, modified_ciphered_phrase))
        return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, ciph_char=ciph_char)
    else:
        return "Oops! Something went wrong."