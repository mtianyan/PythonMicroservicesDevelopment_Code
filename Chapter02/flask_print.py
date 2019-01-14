from flask import Flask, jsonify, request 
 
app = Flask(__name__) 
"""
flask 返回数据
打印request中environ data
打印response中 data
"""
@app.route('/api') 
def my_microservice(): 
    print(request) 
    print(request.environ) 
    response = jsonify({'Hello': 'World!'}) 
    print(response) 
    print(response.data) 
    return response 

@app.route('/api/post', methods=['POST', 'DELETE', 'GET'])
# 默认只有get head options方法，需要其他http支持，需要显示指定
def my_microservice_post():        
	return jsonify({'Hello': 'World!'})

if __name__ == '__main__':
	# 打印app中已注册的url
    print(app.url_map) 
    app.run() 

"""
Map([<Rule '/api' (GET, HEAD, OPTIONS) -> my_microservice>,     
 <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>])   

<Request 'http://127.0.0.1:5000/api' [GET]>
{'wsgi.version': (1, 0), 'wsgi.url_scheme': 'http', 'wsgi.input': <_io.BufferedReader name=520>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'werkzeug.server.shutdown': <function WSGIRequestHandler.make_environ.<locals>.shutdown_server at 0x000000000411F378>, 'SERVER_SOFTWARE': 'Werkzeug/0.14.1', 'REQUEST_METHOD': 'GET', 'SCRIPT_NAME': '', 'PATH_INFO': '/api', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': 60702, 'SERVER_NAME': '127.0.0.1', 'SERVER_PORT': '5000', 'SERVER_PROTOCOL': 'HTTP/1.1', 'HTTP_HOST': '127.0.0.1:5000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'HTTP_COOKIE': 'csrftoken=NBfjhg3iHgpqvDeHv9JfCvZYg5c0JhxeKgwmDXj0CRpmLpTxy8i0kOw56d5GZuyg; sessionid=1xem8s7cf325mhyh203rqkoyda9ydde4', 'werkzeug.request': <Request 'http://127.0.0.1:5000/api' [GET]>}
<Response 19 bytes [200 OK]>
b'{"Hello":"World!"}\n'
"""    