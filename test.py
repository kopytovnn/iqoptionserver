from pyiqoptionapi import IQOption
import datetime
import time
import logging
logging.basicConfig(format='%(asctime)s %(message)s')

api = IQOption("aalex12345sky@gmail.com", "Voda12345")

api.connect()
api.change_balance("REAL")
print('Your current blance is: {:.5f}'.format(api.get_balance()))