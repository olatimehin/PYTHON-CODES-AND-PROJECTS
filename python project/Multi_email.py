# CODE NEED TO BE CORRECTED 

# Problem Statement:
# You want to write a Python program that can send emails to one or multiple recipients using an email account.

# Question:
# How can I write a Python program that can send emails to one or multiple recipients using an email account?

# To execute the program you must create APP PASSWORD from gmail which will be used as the password to send the email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# email information
sender_email = "olatimehinigbekele@gmail.com"
sender_password = input("your_email_password")
recipient_email = "olatnet06@gmail.com" 
email_subject = "Just Sending Email Through Python Program"
email_body = "HI, How are you I am just conforming when you received email then reply on whatsapp received."

# create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

# create an SMTP object and send the message
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(sender_email, sender_password)
smtp_object.sendmail(sender_email, recipient_email, message.as_string())
smtp_object.quit()
