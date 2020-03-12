from flask import Flask, jsonify, request
from app import app
from app.controllers.settings.validate_data import *
from app.controllers.settings.parser_data import *
from app.models.read_data import *

@app.route('/test')
def ping():
    return parserNumbers('123abcdef456')

@app.route('/')
def home():
    return validator()

@app.route('/analyze/<string:web>', methods=['GET'])
def index(web):  
    return infoIp(web)

@app.route('/query', methods=['GET'])
def info():  
    return queryInfo()    

if __name__ == '__main__':
    app.run(debug=True, port=5000)