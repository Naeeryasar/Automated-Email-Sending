import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "alf.stoltenberg21@ethereal.email"
sender_password = "6kFGCmFVUnU3RDjBmP"
receiver_email = "naeeryasar3486@gmail.com"

subject = "Automated Email Test"
body = "I need water"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

server = smtplib.SMTP("smtp.ethereal.email", 587)
server.starttls()
server.login(sender_email, sender_password)

server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent successfully!")

server.quit()