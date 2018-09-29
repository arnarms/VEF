import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template, static_file
import json
import urllib.request
from collections import defaultdict
import collections
from bottle import error
from datetime import datetime
from operator import itemgetter

with urllib.request.urlopen("http://apis.is/petrol") as url:
    bottle.TEMPLATE_PATH.insert(0, 'templates')

#    json_response = json.loads(url.read())
#    last_modified = datetime.strptime(json_response["timestampPriceChanges"],
#                                      '%Y-%m-%dT%H:%M:%S.%f').strftime("%d-%m-%Y %H:%M %p")
    stations_list = json_response["results"]
    trimmed_data = sorted(stations_list, key=itemgetter('bensin95'))[:2]

         
removedDuplicate = []

#for lesa in gogn["results"]:
#
#    x  = lesa["company"]
#
#    if(x not in removedDuplicate):
#        removedDuplicate.append(x)




print(trimmed_data)
