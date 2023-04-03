import smtplib
import datetime as dt

my_email="your_mail@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password="pass")
    connection.sendmail(
        from_addr=my_email,
        to_addrs="to_mailk@gmail.com",
        msg="Subject:hello\n\n this is the body of my mail"
        )


