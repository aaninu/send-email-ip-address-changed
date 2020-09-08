import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read more: https://realpython.com/python-send-email/

# MAIL Server Credentials
server_address = ""
server_port = 465
sender_email = ""
receiver_email = ""
password = ""

def send_email(text , html):
    message = MIMEMultipart("alternative")
    message["Subject"] = "IP Address was changed"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server_address, server_port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
