import smtplib
from email.message import EmailMessage
from user import User

def email_message(email='', phone_num=''):
    user_email = User(email, phone_num)
    to_email = user_email.get_email()
    msg = EmailMessage()
    msg["Subject"] = "Howdy"
    msg["From"] = "breachcheckreport@gmail.com"
    msg["To"] = user_email.get_email()
    msg.set_content("{}".format(user_email.__repr__()))
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("breachcheckreport@gmail.com", "iuninypwmxmxnksd")
        smtp.send_message(msg)
    