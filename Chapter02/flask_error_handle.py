from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions
def JsonApp(app):
	def error_handling(error):
		print(error)
		if isinstance(error, HTTPException):
			result = {'code': error.code, 'description':
					   error.description, 'message': str(error)}
		else:
			# description = abort.mapping[500].description
			description = "服务器 500错误"
			result = {'code': 500, 'description': description,
					  'message': str(error)}
		resp = jsonify(result)
		resp.status_code = result['code']
		return resp
	print(default_exceptions)
	for code in default_exceptions.keys():
		print(code)
		app.register_error_handler(code, error_handling)
	return app

app = JsonApp(Flask(__name__))
@app.route('/api')
def my_microservice():
	raise TypeError("Some Exception")

if __name__ == '__main__':
	app.run()
