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
    return str(iqoption_engine.get_balance()).replace('.', ',')


@app.route('/s_b/<b>')
def set_balance(b):
    return str(iqoption_engine.set_balance(b))


@app.route('/buy/<count>/<res>/<expirations>/<ticker>')
def buy(count, res, expirations, ticker):
    a = iqoption_engine.buy(int(count), action=res, expiration_mode=expirations, activities=ticker)
    if a:
        print(a)
        return str(a[1])

    return "problems with buying"


"+Address	{http://127.0.0.1:5000/chekwin/Timeout response ID Buy. Verify in IQ Option App or Site if the order was executed.}	System.Uri"


@app.route('/chekwin/<deal_id>')
def check_win(deal_id):
    if deal_id == "Timeout response ID Buy. Verify in IQ Option App or Site if the order was executed.":
        return "Timeout"
    return iqoption_engine.check_win(deal_id)


@app.route('/wincount/<deal_id>')
def wincount(deal_id):
    print("___wincount___")
    if deal_id == "Timeout response ID Buy. Verify in IQ Option App or Site if the order was executed.":
        return "Timeout"
    return str(iqoption_engine.win_count(deal_id))


if __name__ == "__main__":
    app.run(port=5000)
