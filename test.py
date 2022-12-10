import time
from iqoptionapi.stable_api import IQ_Option
import inspect

Iq = IQ_Option("alexandrpheonix@gmail.com", "Samsung1991uk")
Iq.connect()  # connect to iqoption
asset = "GBPUSD"

print(inspect.getfullargspec(Iq ))

indicators = Iq.get_technical_indicators(asset)

for i in indicators:
    if i['name'] == 'Stochastic %K (14, 3, 3)':
        print(i)
