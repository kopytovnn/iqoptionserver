# "aalex12345sky@gmail.com Voda12345"
from pyiqoptionapi import IQOption
import time

account = IQOption("alexandrpheonix@gmail.com", "Samsung1991uk")
account.connect()  # connect to iqoption
# a = account.buy(100, "EURUSD", "put", 1.15656)
# print(a)
# b = account.check_win(10064676619)
# print(b)
check, id = account.buy(1, "EURUSD", "call", 1.4833 )
start_time = time.time()
print("start check win please wait")
print(account.check_win_v3(id))
print("--- %s seconds ---" % (time.time() - start_time))
