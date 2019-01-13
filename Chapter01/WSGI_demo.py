import json
import jsonify, request
# pip install jsonify request
import time

def application(environ, start_response):
	"""WSGI协议, 返回服务器的本地时间"""
	headers = [('Content-type', 'application/json')]
	start_response('200 OK', headers)
	return bytes(json.dumps({'time': time.time()}), 'utf8')


