from flask import Flask, render_template, request, redirect
import os
import smtplib
import json
import psycopg2
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

    elif password == "":
        return render_template("signup.html", message = ("Please enter required fields"))
    
    elif username == "":
        return render_template("signup.html", message = ("Please enter required fields"))

    senderEmail = "gregholysnake@gmail.com"
    emailReciever = email

    body = username + "," + "\nYour verification link is below"

    mail = smtplib.SMTP("smtp.gmail.com", 587)

    mail.helo

    #encyrpts login
    mail.starttls()

    mail.login(str(senderEmail), "montyGREGORY")

    mail.sendmail(str(senderEmail), str(emailReciever), body)

    mail.close()

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

    cur = connection.cursor()

    # Inserts the data into each column
    cur.execute('INSERT INTO ' + table + '(username, password, email, registered) VALUES (%s, %s, %s, %s)', (username, password, email, False))

    # Push the data onto the database
    connection.commit()

    # Close the database
    connection.close()

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


