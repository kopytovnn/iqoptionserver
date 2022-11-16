# "aalex12345sky@gmail.com Voda12345"

from pyiqoptionapi import IQOption

account = IQOption("alexandrpheonix@gmail.com", "Samsung1991uk")
account.connect()  # connect to iqoption
a = account.buy(10, "EURUSD", "call", 1)
print(a)
