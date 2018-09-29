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


@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')

with urllib.request.urlopen("http://apis.is/petrol") as url:
    bottle.TEMPLATE_PATH.insert(0, 'templates')

    json_response = json.loads(url.read())
    last_modified = datetime.strptime(json_response["timestampPriceChanges"],
                                      '%Y-%m-%dT%H:%M:%S.%f').strftime("%d-%m-%Y %H:%M %p")
    stations_list = json_response["results"]
    trimmed_data = sorted(stations_list, key=itemgetter('bensin95'))[:5]

marker_switcher = {
        'Atlantsolía': 'https://i.imgur.com/jtEZrit.jpg',
        'Costco Iceland': 'https://i.imgur.com/NVMe8Ru.jpg',
        'Dælan': 'https://i.imgur.com/4am3rJe.jpg',
        'N1': 'https://i.imgur.com/NDn2kNA.jpg',
        'ÓB': 'https://i.imgur.com/j6HQkVh.jpg',
        'Olís': 'https://i.imgur.com/ELf9PXc.jpg',
        'Orkan': 'https://i.imgur.com/wrGwrm9.jpg',
        'Orkan X': 'https://i.imgur.com/ziMAsaq.jpg',
    }

@route("/")
def index():
    company_names = []

    for read in json_response["results"]:

        x = read["company"]
        # removes duplicates of the company names for
        # rendering purposes by adding them to a new list

        if x not in company_names:
            company_names.append(x)

    return template("./templates/index.tpl", data=trimmed_data, rows=company_names, time=last_modified)


@route("/<station:path>")
def station(station):
    filter_list = [station]
    expected_result = [d for d in stations_list if d['company'] in filter_list][:90]

    if len(expected_result) > 0:
        map_url = 'https://maps.googleapis.com/maps/api/staticmap?size=1000x400&maptype=roadmap'
        for item in expected_result:
            map_url += '&markers=icon:'+marker_switcher.get(
                station, '')+'%7Clabel:%7C'+str(item['geo']['lat'])+','+str(item['geo']['lon'])
        map_url += '&key=AIzaSyDZP3D1JaCJ5EHX1xjFqSF96buWNfLP1Mw'
        return template("./templates/station.tpl", data=expected_result, time=last_modified, url=map_url)
    return error404('Sorry! We couldn\'t find what you are looking for')


@error(404)
def error404(error):
    return template("./templates/error_404.tpl", error=error)


run(host='localhost', port=8080, debug=True)
