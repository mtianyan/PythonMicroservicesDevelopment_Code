from flask import Flask, jsonify    
app = Flask(__name__)
@app.errorhandler(500)
def error_handling(error):
	return jsonify({'Error': str(error)}, 500)

@app.errorhandler(404)
def error_handling(error):
	return jsonify({'Error': str(error)}, 404)

@app.route('/api')
def my_microservice():
	raise TypeError("Some Exception")

if __name__ == '__main__':
	app.run()

"""
http://127.0.0.1:5000/api 500
http://127.0.0.1:5000/api/ 404
自定义服务器错误返回:

[
{
"Error": "Some Exception"
},
500
]
"""