from courses import *

from flask import Flask
app = Flask(__name__)

iqoption_engine = IqOptionClass()


@app.route('/<goal>/<interval>')
def hello_world(goal, interval):
    print(4)
    return iqoption_engine.get_candles(goal, interval)


@app.route('/<goal>/<interval>/<params>')
def with_params(goal, interval, params):
    params = params.replace(',', '.').split(';')
    params2 = {}
    for i in params:
        v = i.split(':')
        params2[v[0]] = v[1]
    return iqoption_engine.get_candles(goal, interval, params2)


if __name__ == "__main__":
    app.run()