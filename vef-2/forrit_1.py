
    # Skilgreinum route class og run function úr bottle module.
import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, error, abort

@error(404)
def custom404(error):
    return 'Uh, something wrong happened.'

@route ("/")
def index():
        return  """ 
                <a href="happy"> happy </a> 
                <a href="cute"> cute </a> 
                <a href="sad"> sad </a> 
                """


@route("/<link>")
def site(link):
        if link == "cute":
                        return  """ 
                                <a href="happy"> happy </a> 
                                <a href="cute"> cute </a> 
                                <a href="sad"> sad </a> 
                                <b> this is cute ! </b>
                                """
        elif link == "sad":
                        return  """ 
                                <a href="happy"> happy </a> 
                                <a href="cute"> cute </a> 
                                <a href="sad"> sad </a> 
                                <b> this is sad ! </b>
                                """
        elif link == "happy":
                        return  """ 
                                <a href="happy"> happy </a> 
                                <a href="cute"> cute </a> 
                                <a href="sad"> sad </a> 
                                <b> this is happy ! </b>
                                """
run(host='localhost', port=8080, debug=True)
                      
            
#bottle.run(host='0.0.0.0', port=argv[1])                           
    
