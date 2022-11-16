from courses import *

from flask import Flask

app = Flask(__name__)

iqoption_engine = IqOptionClass()


@app.route('/<goal>/<interval>')
def hello_world(goal, interval):
    print(4)
    return iqoption_engine.get_candles(goal, interval)


@app.route('/signin/<login>/<password>')
def sign_in(login, password):
    return iqoption_engine.connect(login, password)


@app.route('/getTickers/<goal>/<candle_count>/<interval>/<params>/<code>')
def with_params(goal, candle_count, interval, params, code):
    params = params.replace(',', '.').split(';')
    params2 = {}
    for i in params:
        v = i.split(':')
        print('with_params', v)
        params2[v[0]] = v[1]
    print(f'-->{goal}<--', code, iqoption_engine.get_candles(goal, candle_count, interval, params2))
    return iqoption_engine.get_candles(goal, candle_count, interval, params2) + '*' + code


@app.route('/get/<goal>/<candle_count>/<interval>/<params>/<code>')
def send_tickers(goal, candle_count, interval, params, code):pass


@app.route('/buy/<count>')
def buy(count):
    a = iqoption_engine.buy(int(count))
    if a:
        return "True"
    return "False"


if __name__ == "__main__":
    app.run(port=5001)
