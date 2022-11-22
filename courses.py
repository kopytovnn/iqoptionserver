import datetime
import json
import time
# from iqoptionapi.stable_api import IQ_Option
from pyiqoptionapi import IQOption
from psar import psar


class IqOptionClass:
    def __init__(self):
        pass
        # self.account = IQOption("aalex12345sky@gmail.com", "Voda12345")
        # self.account.connect()  #connect to iqoption

    def connect(self, mail, password):
        try:
            self.account = IQOption(mail, password)
            self.account.connect()  #connect to iqoption
            print("Login True")
            return "True"
        except Exception:
            return "False"

    def get_balance(self):
        return self.account.get_balance()

    def get_candles(self, goal='EURUSD', candle_count=30, interval='60', params={'psarStep': '0.02', 'psarMaxStep': '0.2'}):
        d = self.account.get_candles(goal + "", int(interval), int(candle_count), time.time())
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

    def buy(self, count, activities="EURUSD-OTC", action="call", expiration_mode=1):
        print(count, activities, action, expiration_mode)
        print(activities)
        check, id = self.account.buy(count, str(activities) + "", action, float(expiration_mode.replace(',', '.')))
        return check, id

    def check_win(self, deal_id):
        res = self.account.check_win_v3(int(deal_id))
        if int(res) >= 0:
            return 'True'
        return 'False'