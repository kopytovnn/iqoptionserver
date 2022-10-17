import pandas as pd
import ta

# value = {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 2}
# low = pd.Series(data=value, index=['a', 'b', 'c', 'd', 'e'])
#
# value = {'a': 3, 'b': 4, 'c': 2, 'd': 2, 'e': 4}
# high = pd.Series(data=value, index=['a', 'b', 'c', 'd', 'e'])
#
# value = {'a': 2, 'b': 3, 'c': 2, 'd': 3, 'e': 4}
# close = pd.Series(data=value, index=['a', 'b', 'c', 'd', 'e'])

# a = ta.trend.PSARIndicator(high, low, close)
#
# print(a.psar())


def psar(values, step=0.02, maxStep=0.2):
    low = dict()
    high = dict()
    close = dict()
    indexes = []
    for i in range(len(values)):
        low[i] = float(values[i]['min'])
        high[i] = float(values[i]['max'])
        close[i] = float(values[i]['close'])
        indexes.append(i)
    low_psar = pd.Series(data=low, index=indexes)
    high_psar = pd.Series(data=high, index=indexes)
    close_psar = pd.Series(data=close, index=indexes)
    return "*" + "|".join([str(i) for i in ta.trend.PSARIndicator(high_psar, low_psar, close_psar, step=step, max_step=maxStep).psar()]).replace('.', ',')


