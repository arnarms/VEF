import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template,static_file

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')

@route("/")
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return template("./templates/index.tpl")

@route("/send", method="POST")
def send():
    name = request.forms.get('name')

    
    return template("./templates/send.tpl", name=name)
run(host='localhost', port=8080, debug=True)
                      