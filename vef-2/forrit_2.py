# Skilgreinum route class og run function úr bottle module.
import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, error, abort, static_file

@error(404)
def custom404(error):
    return 'Uh, something wrong happened.'

@route ("/")
def index():
        return  """ 
        <a href="happy"> <img border="0"  src="/static/one.jpg" width="100" height="100" </a>
        <a href="cute"> <img border="0"  src="/static/two.jpg" width="100" height="100"> </a>
        <a href="sad"> <img border="0" src="/static/three.jpg" width="100" height="100"> </a>
                """


@route("/<link>")
def site(link):
        if link == "cute":
                        return  """ 
        <a href="happy"> <img border="0"  src="/static/one.jpg" width="200" height="200" </a>
        <a href="cute"> <img border="0"  src="/static/two.jpg" width="500" height="500"> </a>
        <a href="sad"> <img border="0" src="/static/three.jpg" width="200" height="200"> </a>
                                <b> this is cute ! </b>
                                """
        elif link == "sad":
                        return  """ 
        <a href="happy"> <img border="0"  src="/static/one.jpg" width="200" height="200" </a>
        <a href="cute"> <img border="0"  src="/static/two.jpg" width="200" height="200"> </a>
        <a href="sad"> <img border="0" src="/static/three.jpg" width="500" height="500"> </a>
                                <b> this is sad ! </b>
                                """
        elif link == "happy":
                        return  """ 
        <a href="happy"> <img border="0"  src="/static/one.jpg" width="500" height="500" </a>
        <a href="cute"> <img border="0"  src="/static/two.jpg" width="200" height="200"> </a>
        <a href="sad"> <img border="0" src="/static/three.jpg" width="200" height="200"> </a>
                                <b> this is happy ! </b>
                                """

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./photo')

run(host='localhost', port=8080, debug=True)
                                 

#bottle.run(host='0.0.0.0', port=argv[1])                           
    
