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
    return template("./templates/index.tpl")

@route("/send", method="POST")
def send():
    name = request.forms.get('name')
    address = request.forms.get('address')
    email = request.forms.get('email')
    phone = request.forms.get('phone')

    dateOne = request.forms.get('dateOne')
    dateTwo = request.forms.get('dateTwo')
    dateThree = request.forms.get('dateThree')

    workshopOne = request.forms.get('workshopOne')
    workshopTwo = request.forms.get('workshopTwo')
    workshopThree = request.forms.get('workshopThree')
    
    return template("./templates/send.tpl", name=name, email=email, address=address, phone=phone, dateOne=dateOne, 
                                            dateTwo=dateTwo,dateThree=dateThree, workshopOne=workshopOne,
                                            workshopTwo=workshopTwo, workshopThree=workshopThree)

run(host='localhost', port=8080, debug=True)
                      