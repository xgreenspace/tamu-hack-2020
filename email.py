import smtplib
from email.message import EmailMessage
from user import User

user_email = User(email=None, phone_num=None)
to_email = User.get_email()
msg = EmailMessage()
msg["Subject"] = "Howdy"
msg["From"] = "breachcheckreport@gmail.com"
msg["To"] = User.get_email()
msg.set_content("{}".format(User.__repr__()))
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("breachcheckreport@gmail.com", "iuninypwmxmxnksd")
    smtp.send_message(msg)
    