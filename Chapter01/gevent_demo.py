from gevent import monkey; monkey.patch_all()
"""gevent 自动替换标准库插槽"""

def application(environ, start_response):
	headers = [('Content-type', 'application/json')]
	start_response('200 OK', headers)
	# ...do something with sockets here...
	return result