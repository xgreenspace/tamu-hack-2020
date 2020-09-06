import pandas as pd
import time
import requests

from emailscript import *
from user import *
from sms import *

def update(email, phone):
    # Read from the csv file initialize User object to check if there are any new breaches.
    user_data = User(email, phone)
    time.sleep(2)

    send_message(user_data.get_phone_number(), user_data.get_number_of_breaches())
    email_message(user_data.get_email())

data = pd.read_csv('database.csv', encoding='utf-8', dtype={'phone_number':'string'})
# print(len(data['email']))
