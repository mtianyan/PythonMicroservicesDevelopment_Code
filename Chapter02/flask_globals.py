from flask import Flask, jsonify, g, request

app = Flask(__name__)

@app.before_request
def authenticate():
	if request.authorization:
		g.user = request.authorization['username']
	else:
		g.user = 'Anonymous'

@app.route('/api')
def my_microservice():
	"""
	在request上下文中存储数据
	"""
	return jsonify({'Hello': g.user})

if __name__ == '__main__':
	app.run()
"""
C:\Users\tiany\Desktop\PythonMicroservicesDevelopment_Code\Chapter02 (master -> origin)
λ curl http://127.0.0.1:5000/api
{"Hello":"Anonymous"}

C:\Users\tiany\Desktop\PythonMicroservicesDevelopment_Code\Chapter02 (master -> origin)
λ curl http://127.0.0.1:5000/api --user tarek:pass
{"Hello":"tarek"}
"""	