from flask import Flask, render_template, request, redirect
from flask_bootstrap import  Bootstrap
import smtplib
#import dns.resolver
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

    if email == "":
        return render_template("signup.html", message = ("Please enter required fields"))

    if password == "":
        return render_template("signup.html", message = ("Please enter required fields"))
    
    if username == "":
        return render_template("signup.html", message = ("Please enter required fields"))


    senderEmail = "gregholysnake@gmail.com"
    emailReciever = email

    regex = '^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,})$'

    body = username + "," + "\nYour verification link is below."

    mail = smtplib.SMTP("smtp.gmail.com", 587)

    mail.helo

    #encyrpts login
    mail.starttls()

    mail.login(str(senderEmail), "montyGREGORY")

    mail.sendmail(str(senderEmail), str(emailReciever), body)

    mail.close()

    return redirect("/activation/" + username)

@app.route("/login/")
def login():
    return render_template("login.html")



@app.route("/activation/<string:username>", methods = ["GET"])
def activateEmail(username):
    return render_template("congrats.html", Username = username)


