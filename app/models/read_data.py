import re
import json
import requests
import socket
import urllib
from bs4 import BeautifulSoup
import whois

from flask import Flask, jsonify, request, session
from app.controllers.settings.parser_data import *
from app.controllers.settings.validate_data import *


def infoIp(web):
    if len(web) < 6:
        return response(400, 'An error occurred. Please try again!', {'error': 'Ingrese un dirección web valida'})
    else:
        list_ = []
        
        if(len(session["addrees_web"])==0):
            list_.append(web)
            session["addrees_web"] = list_
        else:
            list_ =  session["addrees_web"] 
            list_.append(web)
            session["addrees_web"] = list_
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        ip = socket.gethostbyname(web)        
        
        info = (urllib.request.urlopen("https://"+web))
        redditHtml = info.read()
        soup = BeautifulSoup(redditHtml)

        title = soup.find("head").find("title")
        logo = ""
        for links in soup.find_all("link", attrs={"rel": "icon"}):
            logo = links.get('href')
        
        domain = whois.whois(web)
        
        result = {
            "servers": domain.name_servers,
            "address": ip,
            "country": domain.country,
            "whois": domain.whois_server,
            "whois": domain.whois_server,
            "owner": domain.registrar,
            "servers_changed": True,
            "logo": str(logo),
            "title": str(title)
        }
        
        return response(200, 'ok', result) 

def queryInfo():
    return response(200, 'ok', session["addrees_web"]) 