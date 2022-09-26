from flask import Flask, render_template, request
import cipher_functions as ciph_function
from flask_sqlalchemy import SQLAlchemy
from random import randint
import os

#Config
app = Flask(__name__)
# app.config['TESTING'] = True
# app.config['FLASK_ENV'] = 'development'
# app.config['DEBUG'] = True

#DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://dhvcykblkuglhn:e6c0ce0e1523d8fedde25c74443c8d021bd1b2f948f257e744e84f67be5873ce@ec2-3-93-206-109.compute-1.amazonaws.com:5432/d5q970ot4dokb'
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
# author = get_phrase_from_db(type="a")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "*", "/", ",", "+", "&", "^", "'", "(", ")", "=", ";", "{", "}", "[", "]", "?",
            "=", "_", ">", "<", ":", "-", "!", "#", "@", "%"]

phrase_alphabet = ciph_function.get_alphabet_of_phrase(ciph_function.remove_punctuation_marks(phrase))
cipher_dict = dict(zip(phrase_alphabet, ciph_function.create_cipher_key_list(alphabet, phrase_alphabet)))
filtered_phrase_list = ciph_function.remove_punctuation_marks(phrase)
ciphered_phrase = ciph_function.create_cipher_phrase(filtered_phrase_list, cipher_dict)
ciphered_phrase_str = "".join(map(str, ciphered_phrase))
CIPH_CHAR = True

@app.route("/")
@app.route("/cipher")
def cipher():
    global CIPH_CHAR
    return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, ciph_char=CIPH_CHAR)

@app.route('/decipher', methods=['POST', 'GET'])
def decipher():
    deciphered = False
    global ciphered_phrase_str, phrase, author, CIPH_CHAR
    ciph_char_values = []
    replace_char_values = []

    if request.method == 'POST':
        data = request.form.to_dict()
        ciphered_char = data['ciph_char'].lower()
        replace_ciphered_char = data['new_char'].lower()

        if ciphered_char not in ciphered_phrase_str:
            CIPH_CHAR = False

        else:
            CIPH_CHAR = True
            ciph_char_values.append(ciphered_char)
            replace_char_values.append(replace_ciphered_char)

        if ciphered_char is True:
            modified_dict = ciph_function.changed_dict(ciphered_char, replace_ciphered_char, cipher_dict)
            modified_ciphered_phrase = ciph_function.update_cipher(filtered_phrase_list, modified_dict)
            ciphered_phrase_str = "".join(map(str, modified_ciphered_phrase))

            keys = list(modified_dict.keys())
            values = list(modified_dict.values())

            if keys == values:
                deciphered = True
        else:
            if len(ciph_char_values) == 0:
                ciphered_phrase_str = ciphered_phrase_str

            else:
                modified_dict = {}
                for i in range(len(ciph_char_values)):
                    modified_dict = ciph_function.changed_dict(ciph_char_values[i], replace_char_values[i], cipher_dict)

                modified_ciphered_phrase = ciph_function.update_cipher(filtered_phrase_list, modified_dict)
                ciphered_phrase_str = "".join(map(str, modified_ciphered_phrase))

        return render_template("/cipher.html", ciphered_phrase_str=ciphered_phrase_str, deciphered=deciphered, ciph_char=CIPH_CHAR, phrase=phrase, author=author)
    else:
        return render_template("/error.html")

if __name__ == '__main__':
    app.run()