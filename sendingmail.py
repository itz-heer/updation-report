import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


def send_email():
    # Email configuration
    sender_email = "patelheer8009@gmail.com"
    receiver_email = "piyushsarawagi1996@gmail.com"
    subject = "Investment Advisor"
    
    # Create the MIME object

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Email body
    body = "Weekly report on updation of investment advisor"
    message.attach(MIMEText(body, "plain"))

    # Attach a file
    file_path = "updated report.xlsx"  
    attachment = open(file_path, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {file_path}")
    message.attach(part)

    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "patelheer8009@gmail.com"
    smtp_password = "gmay dwks fbek qwgf"

    # Create a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    # Schedule the email to be sent every Monday at 3 pm
    schedule.every().day.at("15:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)