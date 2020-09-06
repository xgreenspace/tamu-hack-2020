from twilio.rest import Client 

account_sid = "AC4eba4bf47bf6745b243e9afc0d5c98a7"
auth_token = "511ba420b410309f53e64d9be5c28094"

client = Client(account_sid, auth_token)

def send_message(phone_number="+15555555555", breach_num=-1):
    
    message = client.messages.create(
        to=phone_number,
        from_="+12065671210",
        body="Howdy, you've been involved in a new breach. The number of breaches that have leaked your data is now {}.".format(breach_num)
    )


