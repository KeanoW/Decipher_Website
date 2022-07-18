from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("templates/index.html")

@app.route("/cipher")
def contact():
    return render_template("/cipher.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/components")
def components():
    return render_template("/components.html")