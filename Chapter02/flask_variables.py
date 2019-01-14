from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1': 'Tarek', '2': 'Freya'}
_IDS = {(val, id) for id, val in _USERS.items()}

class RegisteredUser(BaseConverter):
    """
    继承基础的转换类，并实现两个方法
    to_python 方法将值转换成一个Python对象返回给视图
    to_url 方法是另一种方式用于url_for()反向查找url
    """
    def to_python(self, value):
        if value in _USERS:
            print(_USERS[value])
            return _USERS[value]
        raise ValidationError()
		
    def to_url(self, value):
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

"""
@app.route('/api/person/<person_id>')    
def person(person_id):        
    response = jsonify({'Hello': person_id})        
    return response    

$ curl localhost:5000/api/person/3    
{      
"Hello": "3"    
}

/person/<int:person_id> # 将传入的person_id参数转换为int类型
"""
@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello hey': name})
    return response

if __name__ == '__main__':
    app.run()

