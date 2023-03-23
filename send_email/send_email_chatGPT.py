import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(from_email, to_email, password, subject, message):
    # Create a MIMEMultipart message
    msg = MIMEMultipart()

    # Set up the message parameters
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    # Create the SMTP server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Example usage:
from_email = 'your_email@gmail.com'
to_email = 'recipient_email@example.com'
password = 'your_email_password'
subject = 'Hello from Python!'
message = 'This is a test email sent from Python.'

send_email(from_email, to_email, password, subject, message)




#This code uses the smtplib library to create an SMTP server, logs in to your email account using your email address and password, and sends an email message using the sendmail() method. The email.mime.text and email.mime.multipart modules are used to create and format the email message.

#Make sure to replace the from_email, to_email, password, subject, and message variables in the send_email() function with your own information. Also, note that you may need to enable "less secure apps" in your Gmail settings if you are using a Gmail account.

#-----------------------------------------------------------------------------------

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# set up SMTP server and login credentials
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_username'
password = 'your_password'

# set up email message
message = MIMEMultipart()
message['From'] = 'sender@example.com'
message['To'] = 'recipient@example.com'
message['Subject'] = 'Test Email'
body = 'This is a test email sent using Python!'
message.attach(MIMEText(body, 'plain'))

# connect to SMTP server and send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls() # enable TLS encryption
    server.login(username, password)
    text = message.as_string()
    server.sendmail(message['From'], message['To'], text)




# In this example, we first set up the SMTP server and login credentials for the email account we want to use to send the email. 
# Then, we create a MIMEMultipart object to represent the email message, specifying the sender, recipient, subject, and body of the message. 
# Finally, we connect to the SMTP server using smtplib.SMTP, enable TLS encryption with starttls(), log in using our credentials with login(), and send the email using sendmail().