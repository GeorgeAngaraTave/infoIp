from flask import Flask, make_response, jsonify, Response
from app.controllers.databases.mysql import connection as conn
from app.controllers.settings.parser_data import *

# def response(status = "", message = "", code = 200):
#     return {"code":code,"status":status,"message":message}

def response(status_http=200, message='success', data=None, status_code=None, errors=None):
    CORS_HEADERS = cors_head()
    data = None if data is None else data
    json_resp = {'status': status_code or status_http, 'message': message, 'data': data}
    if errors is not None:
        json_resp.update({'error': errors})
    resp = make_response(jsonify(json_resp), status_http)
    resp.headers.extend(CORS_HEADERS or {})
    return resp    

def validator():
    return response(200, 'SUCCESS', ["Welcome to the BackEnd"]) 

def cors_head():
    return {
        "Access-Control-Allow-Headers": "Origin, x-requested-with, Content-Type, Accept, Authorization",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH",
        "Access-Control-Max-Age": 1,
        "Allow": "GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, PATCH"
    }
