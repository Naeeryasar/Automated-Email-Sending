import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "alf.stoltenberg21@ethereal.email"
sender_password = "YOUR_PASSWORD"
receiver_email = "naeeryasar3486@gmail.com"

subject = "Automated Email Test"
body = "I need water"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))