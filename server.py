from flask import Flask, render_template, request
import cipher_functions as ciph_function
import api

phrase = api.get_quote(type="q")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "*", "/", ",", "+", "&", "^", "'", "(", ")", "=", ";", "{", "}", "[", "]", "?",
            "=", "_", ">", "<", ":", "-", "!", "#", "@", "%", " "]

phrase_alphabet = ciph_function.get_alphabet_of_phrase(ciph_function.remove_punctuation_marks(phrase))
cipher_dict = dict(zip(phrase_alphabet, ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)))
cipher_chars = ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)
# print(cipher_dict)
filtered_phrase_list = ciph_function.remove_punctuation_marks(phrase)
ciphered_phrase = ciph_function.create_cipher_phrase(filtered_phrase_list, cipher_dict)
ciphered_phrase_str = "".join(map(str, ciphered_phrase))
# print(f"ciphered phrase: {ciphered_phrase_str}")
count = 0
modified_ciphered_phrase = []
modified_dict = {}

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("templates/index.html")


@app.route("/")
def home():
    return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, cipher_dict=cipher_dict)

@app.route("/cipher")
def cipher():
    return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, )

@app.route('/change_char', methods=['POST', 'GET'])
def change_char():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return render_template("/cipher.html")
    else:
        return "Oops! Something went wrong."

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/components")
def components():
    return render_template("/components.html")

if __name__ == "__main__":
    app.run(debug=True)