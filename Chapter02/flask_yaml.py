from flask import Flask
import yaml      # requires PyYAML
app = Flask(__name__)
def yamlify(data, status=200, headers=None):
	_headers = {'Content-Type': 'application/x-yaml'}
	if headers is not None:
		_headers.update(headers)
	return yaml.safe_dump(data), status, _headers
"""
通常状态下使用jsonify，如果你的终端要求你提供另一种content-type
"""
@app.route('/api')
def my_microservice():
	return yamlify(['Hello', 'YAML', 'World!'])

if __name__ == '__main__':
	app.run()