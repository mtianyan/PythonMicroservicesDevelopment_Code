from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def auth():
	print("The raw Authorization header")
	print(request.environ["HTTP_AUTHORIZATION"])
	print("Flask's Authorization header")
	print(request.authorization)
	return ""

"""
curl http://localhost:5000/ -u tarek:password
The raw Authorization header                               
Basic dGFyZWs6cGFzc3dvcmQ=                                 
Flask's Authorization header                               
{'username': 'tarek', 'password': 'password'}              
127.0.0.1 - - [14/Jan/2019 13:45:43] "GET / HTTP/1.1" 200 -

最基础的授权方式，使用base64加密用户名，密码。
import requests
requests.get('http://localhost:5000/', auth=('user', 'pass'))
"""
if __name__ == "__main__":
	app.run()