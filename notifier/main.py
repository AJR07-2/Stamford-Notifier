import firebase_admin
import ssl
import smtplib
from firebase_admin import credentials, firestore
cred = credentials.Certificate('notifier/ServiceAccountKey.json')

default_app = firebase_admin.initialize_app(cred)
dataBase = firestore.client()

smtp_server = 'smtp.gmail.com'
port = 465
sender = 'stamfordunoffical@gmail.com'
receiver = 'xiaonianhe@hotmail.com'
password = input("Password:")
message = """
Subject: Yay it works? (:D)

This message was sent from Python!
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    # send email
    server.sendmail(sender, receiver, message)
