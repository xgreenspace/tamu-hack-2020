import pyhibp
import time
from pyhibp import pwnedpasswords as pw

class User:
    def __init__(self, email=None, phone_num=None):
        API_KEY = "615d678ee4c3457cbabcca2d8661f891"
        pyhibp.set_api_key(key=API_KEY)
        pyhibp.set_user_agent(ua="Making a test application for a project.")

        self.phone_num = phone_num
        self.email = email
        self.breaches = pyhibp.get_account_breaches(account=self.email, truncate_response=True, include_unverified=True)

        if (not (self.email or self.phone_num)):
            print('This user has an invalid email or phone number.')
            return None

    def __repr__(self):
        return 'The User: {} has been involved in {} breaches.'.format(self.email, len(self.breaches))

    def get_breaches(self):
        return self.breaches

    def get_list_breaches(self):
        list_of_breaches = []
        for dic in self.breaches:
            list_of_breaches.append(dic['Name'])
        return list_of_breaches



