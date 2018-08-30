# Skilgreinum route class og run function úr bottle module.
import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, error, abort

@error(404)
def custom404(error):
    return 'Sorry, you encountered an error '

@route('/admin/<admin>') #decorator
def admin(admin):
        return '<b> You are on the admin page '  + admin + '</b>'

@route('/page/<id>/<name>') #decorator
def page(id, name):
        return '<b> You are now viewing page ' + id + ' with the name of ' + name + '</b>'

@route('/articles/<page>/<id>') #decorator
def article(id, page):
        return '<b> You are now browsing article with the ID '  + id + ' called ' + page + '</b>'

run(host='localhost', port=8080, debug=True)
                      
            
#bottle.run(host='0.0.0.0', port=argv[1])                           
    