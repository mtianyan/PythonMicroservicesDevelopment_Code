from flask import Flask, jsonify, g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("pip install blinker")

app = Flask(__name__)

"""
<Flask 'flask_blinker'>
About to send a Response
<Response 18 bytes [200 OK]>

For instance, the got_request_exception signal is 
triggered when an exception occursbefore the framework does something with it. 
That's how Sentry's (https://sentry.io)
Python client (Raven) hooks itself onto Flask to log exceptions
"""
def finished(sender, response, **extra):
	print(sender)
	print('About to send a Response')
	print(response)

# 预定义的动作，request_finished完成之后发信号调用finished函数
request_finished.connect(finished)

@app.route('/api')
def my_microservice():
    return jsonify({'Hello': 'World'})

if __name__ == '__main__':
    app.run()