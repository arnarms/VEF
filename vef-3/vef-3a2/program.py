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

kennitala1 = id(10)
kennitala2 = id(10)
kennitala3 = id(10)

kSum1 = str(sum_digits(kennitala1))
kSum2 = str(sum_digits(kennitala2))
kSum3 = str(sum_digits(kennitala3))
k1={'kennitala': kennitala1, 'sum' : kSum1}
k2={'kennitala': kennitala2, 'sum' : kSum2}
k3={'kennitala': kennitala3, 'sum' : kSum3}

#print ("Kennitala er " + str(kennitala))
#print ("Þversumma er " + str(sum_digits(kennitala)))

array=[k1,k2,k3]

@route ("/")
def index():
    return template("vef-3/vef-3a2/template/index.tpl")

@route('/<id>')
def print(id):
    if id == "kennitala1":
        return template("vef-3/vef-3a2/template/article.tpl", k1)
    elif id == "kennitala2":
        return template("vef-3/vef-3a2/template/article.tpl", k2)
    elif id == "kennitala3":
        return template("vef-3/vef-3a2/template/article.tpl", k3)
    
run(host='localhost', port=8080, debug=True)
                      
            
#bottle.run(host='0.0.0.0', port=argv[1])                           
    
