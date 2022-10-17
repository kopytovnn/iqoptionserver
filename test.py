import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("aalex12345sky@gmail.com", "Voda12345")
Iq.connect()#connect to iqoption
asset="EURUSD"
indicators = Iq.get_technical_indicators(asset)
for i in indicators:
    print(i)