import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template, static_file
import json
import urllib.request
from collections import defaultdict

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./vef-midonn/static')



with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read())




@route("/")
def index():

    
    companyNames = []
    for lesa in gogn["results"]:

        x  = lesa["company"]
        
        ## removes duplicates of the company names for rendering purposes

        if(x not in companyNames):
            companyNames.append(x)

    return template("./vef-midonn/templates/index.tpl", gogn=gogn , rows=companyNames)


run(host='localhost', port=8080, debug=True)
                      