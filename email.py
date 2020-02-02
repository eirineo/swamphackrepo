from flask import Flask, request
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

# a randomizer of sorts
serializer = URLSafeTimedSerializer("goodENOUGH")

#this needs to be replaced with the actual email
userEmail = "placeHolder"

#the actual email???
email = resquest.form["email"]

#randomized value for link
token = serializer.dumps(userEmail, salt="nacl")

#creates confirmation email CHANGE THIS
msg = Message("Confirmation", sender="placeholder", recipients=[email])
link = url_for("Confirm_email", token=token, _external=True)
msg.body = "Your link is {}".format(link)
#the email loaded???

mail.send(msg)

try: 
    email = serializer.loads(token,salt="nacl", max_age=7200)
except:
     SignatureExpired