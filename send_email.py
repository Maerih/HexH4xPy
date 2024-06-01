import smtplib
import ssl

def sendEmail(message):
    sender_email = "test@sciat.africa"
    password = "8),p7mObxU6N"
    receiver_email = "onyonka.maeri@sciat.africa"
    smtp_server = "mail.sciat.africa"
    port = 465

    context = ssl.create_default_context()
    server = None  

    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)  # Use SMTP_SSL instead of starttls
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        if server:
            server.quit()
