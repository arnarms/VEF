import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run, template, static_file

horseNews={'title': 'Huge horse is born, like really huge', 'article': 'Today a huge horse was born, truly an amazing feat'}
lotteryNews={'title': 'A millionare wins the lottery', 'article': 'Jimmy Moneybags has just won his second billion, people are starting to think this is rigged'}
computerNews={'title': 'Scientist invents the fastest CPU', 'article': 'Scientist invents a superpower CPU,  but unfortunately it is not compatible with modern tech'}

array=[horseNews,lotteryNews,computerNews]

@route("/")
def index():
    return template("vef-3b/templates/index.tpl")

@route('/<article>')
def article(article):
    if article == "horse":
        return template("vef-3b/templates/article.tpl", horseNews)
    elif article == "lottery":
        return template("vef-3b/templates/article.tpl", lotteryNews)
    elif article == "tech":
        return template("vef-3b/templates/article.tpl", computerNews)
    
run(host='localhost', port=8080, debug=True)
                      