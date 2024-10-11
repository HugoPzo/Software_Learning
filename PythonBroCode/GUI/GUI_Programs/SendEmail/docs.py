
# Simple Mail Transfer Protocol Library
import smtplib

# Who will send the email
sender = "sender@email.com"

# Se debe crear una App Password para poder acceder con el servidor
# smpt -> Con la contraseña real no funciona
# https://myaccount.google.com/apppasswords

# Contraseña de Aplicaciones
# Password of email - Using an App password
appPassword = "appPassword"
# Who will receive the email
receiver = "receiver@email.com"
# Subject of the email
subject = "SUBJECT OF EMAIL"
# Body of the email
body = "Body of email!!!"

# Header of Email
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}

"""

# DO NOT USE NAME 'email.py'
# Turn on 'Less secure app' access on our email

try:
    # Open the server 'smtplib.SMTP(host -> "smtp.gmail.com", port -> 587)'
    # 587 -> Default Mail Submission Port
    server = smtplib.SMTP("smtp.gmail.com", 587)

    #      start transport layer security
    # Init server security
    server.starttls()

    # Login in the server
            # .login(sender, password)
    server.login(sender, appPassword)
    print("Logged in...")
    #           .sendmail(sender, receiver, message)
    server.sendmail(sender, receiver, message)
    print("Email sent!")

except Exception as e:
    print(f"Error: {e}")
except smtplib.SMTPAuthenticationError:
    print("Username or Password is wrong...")
