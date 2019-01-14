from flask import Flask, jsonify
from flask_blueprint import teams
app = Flask(__name__) 
app.register_blueprint(teams)

if __name__ == '__main__': 
    app.run()
"""
http://127.0.0.1:5000/teams/1
"""    