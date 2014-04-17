#! /usr/bin/python

import smtplib as s
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import getpass

user  = raw_input('Enter you email     : ')
passw = getpass.getpass('Enter your password : ')

receiver = raw_input('Enter the reciever`s email : ')

msg = MIMEMultipart()
msg['From'] = user
msg['To'] = receiver
msg['Subject'] = "Python email"

body = raw_input('Enter the message : ')

msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()

server = s.SMTP('smtp.yandex.ua')
server.ehlo()
server.starttls()
server.login(user, passw)
server.sendmail(user, receiver, text)


