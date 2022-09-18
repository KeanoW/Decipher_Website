from flask import Flask, render_template, request
import cipher_functions as ciph_function
from flask_sqlalchemy import SQLAlchemy
from random import randint

#Config
app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True

#DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote =db.Column(db.String(60), nullable=False)
    auther = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Quote: {self.quote} - {self.auther}"

def get_phrase_from_db(type):
    rand = randint(1, 84)
    first_quote = Quotes.query.get(rand)
    if type == "q":
        return first_quote.quote
    elif type == "a":
        return first_quote.auther

# phrase = get_phrase_from_db(type="q")
phrase = "hello"
print(phrase)
author = get_phrase_from_db(type="a")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "*", "/", ",", "+", "&", "^", "'", "(", ")", "=", ";", "{", "}", "[", "]", "?",
            "=", "_", ">", "<", ":", "-", "!", "#", "@", "%", " "]

phrase_alphabet = ciph_function.get_alphabet_of_phrase(ciph_function.remove_punctuation_marks(phrase))
cipher_dict = dict(zip(phrase_alphabet, ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)))
cipher_chars = ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)
filtered_phrase_list = ciph_function.remove_punctuation_marks(phrase)
ciphered_phrase = ciph_function.create_cipher_phrase(filtered_phrase_list, cipher_dict)
ciphered_phrase_str = "".join(map(str, ciphered_phrase))


@app.route("/")
@app.route("/cipher")
def cipher():
    return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str)

@app.route('/decipher', methods=['POST', 'GET'])
def decipher():
    ciph_char = True
    modified_dict = {}
    deciphered = False
    if request.method == 'POST':
        data = request.form.to_dict()
        ciphered_char = data['ciph_char'].lower()

        if ciphered_char not in alphabet:
            ciph_char = False

        replace_ciphered_char = data['new_char'].lower()

        if ciph_char is True:
            modified_dict = ciph_function.changed_dict(ciphered_char, replace_ciphered_char, cipher_dict)
            modified_ciphered_phrase = ciph_function.update_cipher(filtered_phrase_list, modified_dict)

        ciphered_phrase_str = "".join(map(str, modified_ciphered_phrase))
        print(f"Keys: {modified_dict.keys()} Values: {modified_dict.values()}")
        if modified_dict.keys() == modified_dict.values():
            deciphered = True
        return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, ciph_char=ciph_char, deciphered=deciphered)
    else:
        return "Oops! Something went wrong."

if __name__ == '__main__':
    app.run(debug=True)