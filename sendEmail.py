
# change the email server and credentials before testing script

import smtplib
import ssl
from email.message import EmailMessage

email_sender ="test@sciat.africa"
email_password = "8),p7mObxU6N"
email_receiver = "onyonkamaeriofficial@gmail.com"

subject = "This is the Py Email Script"
body = """
The reggae will never be stopped!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('mail.sciat.africa', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("[+] Success Email Sent!")