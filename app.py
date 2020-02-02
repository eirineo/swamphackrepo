from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
import json
import psycopg2
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)
mail = Mail(app)
# Renders the page
@app.route("/")
def index():
    return render_template("index.html")

# Renders our signup page
@app.route("/signup/")
def signup():
    return render_template("signup.html")

# Our post request for user information
@app.route("/unconfirmed/", methods = ["POST"]) 
def grabUserInfo():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    if email == "":
        return render_template("signup.html", message = ("Please enter required fields"))

    elif password == "":
        return render_template("signup.html", message = ("Please enter required fields"))
    
    elif username == "":
        return render_template("signup.html", message = ("Please enter required fields"))


    # Initate database
    with open('settings/db.json') as loop:
            data = json.load(loop)

    # Declare our data from the json file
    databaseName = data["Login"]["Database"]
    password = data["Login"]["Password"]
    userName = data["Login"]["Username"]
    table = data["Login"]["Table"]

    connection = psycopg2.connect(user = data["Login"]["Username"],
                                  password = data["Login"]["Password"],
                                  database = data["Login"]["Database"])

    # Assigns the cursor so we can execute commands
    cur = connection.cursor()

    # Inserts the data into each column
    cur.execute('INSERT INTO ' + table + '(username, password, email, registered) VALUES (%s, %s, %s, %s)', (username, password, email, False))

    # Push the data onto the database
    connection.commit()

    # Close the database
    connection.close()

    senderEmail = "gregholysnake@gmail.com"

    # a randomizer of sorts
    serializer = URLSafeTimedSerializer("goodENOUGH")

    #randomized value for link
    token = serializer.dumps(email, salt="nacl")

    #creates confirmation email CHANGE THIS
    msg = Message("Confirmation", sender = senderEmail, recipients = email)
    link = url_for("confirm_email", token = token, _external = True)
    msg.body = "Your link is {}".format(link)
    #the email loaded???
    mail.send(msg)

    try: 
        email = serializer.loads(token,salt="nacl", max_age=7200)
    except:
        SignatureExpired
    # Redirects to the activation screen to give a custom url
    return redirect("/activation/" + username)

# Our route for the login page
@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

@app.route("/activation/<string:username>", methods = ["GET"])
def activateEmail(username):
    return render_template("congrats.html", Username = username)


