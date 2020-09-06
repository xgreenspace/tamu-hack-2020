import json

from twilio.rest import Client

with open('private_key.json') as f:
    KEYS = json.load(f)

account_sid = KEYS['account_sid']
auth_token = KEYS['auth_token']

client = Client(account_sid, auth_token)

def send_message(phone_number="+15555555555", breach_num=-1):
    
    message = client.messages.create(
        to=phone_number,
        from_="+12065671210",
        body="Howdy, you've been involved in a new breach. The number of breaches that have leaked your data is now {}.".format(breach_num)
    )

