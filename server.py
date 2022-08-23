from flask import Flask, render_template, request
import cipher_functions as ciph_function
app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("templates/index.html")

@app.route("/")
def home():
    return render_template("/cipher.html")

@app.route("/cipher")
def cipher():
    return render_template("/cipher.html")

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