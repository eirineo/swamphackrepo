from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/unconfirmed/", methods = ["POST"])
def grabUserInfo():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    return redirect("/activation/" + username + email)

@app.route("/login/")
def login():
    return render_template("login.html")

#@app.route("//")
#def grabUserInfo():
    return render_template("welcome.html")

@app.route("/activation/<string:username>", methods = ["GET"])
def activateEmail(username):
    return render_template("congrats.html", Username = username)


