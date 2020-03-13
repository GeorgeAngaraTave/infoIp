import re
import os
import json
import requests
import socket
import urllib
from bs4 import BeautifulSoup
import whois
import csv, operator
from flask import Flask, jsonify, request
from app.controllers.settings.parser_data import *
from app.controllers.settings.validate_data import *


def infoIp(web):
    if len(web) < 6:
        return response(400, 'An error occurred. Please try again!', {'error': 'Ingrese un dirección web valida'})
    else:        
        socket.setdefaulttimeout(60)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        ip = socket.gethostbyname(web)        
        
        info = (urllib.request.urlopen("https://"+web))
        print(info)

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
        
        archivo = open(os.getcwd()+"/app/models/search.csv", mode='a')
        archivo.write(web)
        archivo.write(",")
        archivo.close()
        

        return response(200, 'ok', result) 

def queryInfo():    
    with open(os.getcwd()+"/app/models/search.csv", mode="r") as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            print(reg)
            return response(200, 'ok', reg)          
