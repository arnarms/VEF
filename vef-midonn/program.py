import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template, static_file
import json
import urllib.request
from collections import defaultdict
import collections

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./vef-midonn/static')



with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read())

split_petrol = collections.defaultdict(list)
for line in gogn["results"]:
    split_petrol[line["company"]].append(line)
    
@route("/")
def index():

    companyNames = []


    for read in gogn["results"]:

        x  = read["company"]


        ## removes duplicates of the company names for
        ## rendering purposes by adding them to a new list

        if(x not in companyNames):
            companyNames.append(x)

    return template("./vef-midonn/templates/index.tpl", gogn=gogn1, rows=companyNames)


run(host='localhost', port=8080, debug=True)
                      