# Skilgreinum route class og run function úr bottle module.
import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get

@route('/') #decorator

def index():
    return '<a href="/"> <h1>About </h1> </a> <a href="/sida1"> <h1>Biography </h1> </a> <a href="/sida2"> <h1> Pictures </h1>'

@route('/sida1') #decorator

def bio():
    return '<a href="/"> <h1>About </h1> </a> <a href="/sida1"> <h1>Biography </h1> </a> <a href="/sida2"> <h1> Pictures </h1>'

@route('/sida2') #decorator

def pic():
    return '<a href="/"> <h1>About </h1> </a> <a href="/sida1"> <h1>Biography </h1> </a> <a href="/sida2"> <h1> Pictures </h1>'

#run(host='localhost', port=8080, debug=True)
                      
            
bottle.run(host='0.0.0.0', port=argv[1])                           
    