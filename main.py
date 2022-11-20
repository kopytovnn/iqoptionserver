from courses import *

from flask import Flask

app = Flask(__name__)

iqoption_engine = IqOptionClass()


@app.route('/<goal>/<interval>')
def hello_world(goal, interval):
    # print(4)
    return iqoption_engine.get_candles(goal, interval)


@app.route('/signin/<login>/<password>')
def sign_in(login, password):
    s = iqoption_engine.connect(login, password)
    return s


@app.route('/getTickers/<goal>/<candle_count>/<interval>/<params>/<code>')
def with_params(goal, candle_count, interval, params, code):
    params = params.replace(',', '.').split(';')
    params2 = {}
    for i in params:
        v = i.split(':')
        # print('with_params', v)
        params2[v[0]] = v[1]
    # print(f'-->{goal}<--', code, iqoption_engine.get_candles(goal, candle_count, interval, params2))
    return iqoption_engine.get_candles(goal, candle_count, interval, params2) + '*' + code


@app.route('/get/<goal>/<candle_count>/<interval>/<params>/<code>')
def send_tickers(goal, candle_count, interval, params, code): pass


@app.route('/balance/')
def get_balance():
    # print(iqoption_engine.get_balance())
    return str(iqoption_engine.get_balance())


@app.route('/buy/<count>/<res>/<expirations>/<ticker>')
def buy(count, res, expirations, ticker):
    a = iqoption_engine.buy(int(count), action=res, expiration_mode=expirations, activities=ticker)
    if a:
        return "True"
    return get_balance()


if __name__ == "__main__":
    app.run(port=5000)
