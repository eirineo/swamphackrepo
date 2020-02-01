from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/welcome/")
def grabUserInfo():
    return render_template("welcome.html")

@app.route("/activation/")
def activateEmail():
    return render_template("activation.html")


