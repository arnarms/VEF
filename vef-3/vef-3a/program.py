import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template
from random import randint

def id(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

kennitala = id(10)

#print ("Kennitala er " + str(kennitala))
#print ("Þversumma er " + str(sum_digits(kennitala)))

@route ("/")
def index():
    return template("vef-3a/template/index.tpl")

@route ("/kennitala")
def print():
        return "Kennitala: ", str(kennitala), " Þversumma er: " , str(sum_digits(kennitala)) 

run(host='localhost', port=8080, debug=True)
                      
            
#bottle.run(host='0.0.0.0', port=argv[1])                           
    
