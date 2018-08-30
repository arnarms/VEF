# Skilgreinum route class og run function úr bottle module.
import os
from os import environ as env
from sys import argv

import bottle
from bottle import route, run, template, BaseTemplate, static_file, error, abort

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url  # reference to function

@error(404)
def custom404(error):
    return 'Sorry, you encountered an error '

@route("/photo/<word>")
def word(word):
        if word == "cute":
                return '<img style="max-width: 450px; max-height: 300px" src="https://is2-ssl.mzstatic.com/image/thumb/Purple71/v4/6b/48/62/6b486209-6e80-2b25-f9d1-36400402a27a/source/512x512bb.jpg">'
        elif word == "sad":
                return '<img style="max-width: 450px; max-height: 300px" src="https://i.pinimg.com/originals/8b/9c/07/8b9c0757ce4a38a8c799c33b77db7559.jpg">'
        elif word == "happy":
                return '<img style="max-width: 450px; max-height: 300px" src="https://data.whicdn.com/images/171399860/large.jpg">'
        else:
                return '<b>This photo does not exist</b>'

run(host='localhost', port=8080, debug=True)
                      
    

#bottle.run(host='0.0.0.0', port=argv[1])                           
    