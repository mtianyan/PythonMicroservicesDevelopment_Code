from flask import Flask, jsonify 

"""使用flask开发微服务的基础"""
app = Flask(__name__) 
 
@app.route('/api') 
def my_microservice(): 
    return jsonify({'Hello': 'World!'}) 
 
if __name__ == '__main__': 
    app.run()