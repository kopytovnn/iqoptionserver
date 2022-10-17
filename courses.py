import datetime
import json
import time
# from iqoptionapi.stable_api import IQ_Option
from pyiqoptionapi import IQOption
from psar import psar


class IqOptionClass:
    def __init__(self):
        self.account = IQOption("aalex12345sky@gmail.com", "Voda12345")
        self.account.connect()  #connect to iqoption

    def get_candles(self, goal='EURUSD', interval='60', params={'psarStep': '0.02', 'psarMaxStep': '0.2'}):
        # print(123)
        d = self.account.get_candles(goal, int(interval), 30, time.time())
        main_list = []
        string = ''
        for i in d:
            string += f"{i['close']}#{i['open']}#{i['max']}#{i['min']}|".replace('.', ',')
            main_list.append({'close': i['close'],
                              'open': i['open'],
                              'high': i['max'],
                              'low': i['min']})
        psar_values = psar(d, step=float(params['psarStep']), maxStep=float(params['psarMaxStep']))
        return string + psar_values
