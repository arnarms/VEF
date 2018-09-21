import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template
import json
import urllib.request


with urllib.request.urlopen("https://apis.is/currency/lb") as url:
    gogn = json.loads(url.read())


@route("/")
def index():
    return """
    <ul>
        <li><a href="/local">Read Local Json File</a></li>
        <li><a href="/api">Read Online API Information</a></li>
    </ul>
    """

@route("/local")
def local():
    return template("vef-4/templates/local.tpl")


@route("/api")
def api():
    return template("vef-4/templates/api.tpl", gogn=gogn)

run(host='localhost', port=8080, debug=True)
                      