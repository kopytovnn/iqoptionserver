# "aalex12345sky@gmail.com Voda12345"
from pyiqoptionapi import IQOption
import time

account = IQOption("alexandrpheonix@gmail.com", "Samsung1991uk")
account.connect()  # connect to iqoption
a = account.buy(100, "GBPUSD-OTC", "put", 1)
print(a)
b = account.check_win(10064676)
print(b)
# start_time = time.time()
# print("start check win please wait")
# print(account.check_win_v3(10064676619))
# print("--- %s seconds ---" % (time.time() - start_time))
