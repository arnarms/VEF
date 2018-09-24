import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template, static_file
import json
import urllib.request

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read())



removedDuplicate = []

for lesa in gogn["results"]:

    x  = lesa["company"]

    if(x not in removedDuplicate):
        removedDuplicate.append(x)

print(removedDuplicate)
