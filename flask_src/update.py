import pandas as pd
import time
import requests

from emailscript import *
from user import *
from sms import *

def update(id=0):
    # Read from the csv file initialize User object to check if there are any new breaches.
    user_data = User(data['email'][id], data['phone_number'][id])
    time.sleep(2)

    if (user_data.get_number_of_breaches() > data['total_breaches'][id]):
        # FIXME: Will run whatever command will cause the notification to be sent out.
        send_message(user_data.get_phone_number(), user_data.get_number_of_breaches())
        email_message(user_data.get_email())

data = pd.read_csv('database.csv', encoding='utf-8', dtype={'phone_number':'string'})
# print(len(data['email']))

# FIXME: Ideally, will run for a full loop every sing day... But for now
for i in range(len(data['email'])):
    update(i)

