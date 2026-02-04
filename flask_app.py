from flask import Flask, render_template_string, url_for
from random import randint

app = Flask(__name__)

#First Page
@app.route("/")
def index():
    return '''
    <head>
        <style>
            h1{
                color:blue;
            }
            background-color:black;
        </style>
    </head>
    <body>
        <h1>Hello Flask<h1>
        <img src="creature.png">
        <p>
            <a href="/page"> Page Two </a>
        </p>
        <p>
            <a href="/apple"> Apple </a>
        </p>
         <p>
            <a href="/sprite"> Sprite </a>
        </p>
         <p>
            <a href="/happy"> Happy </a>
        </p>
    </body>
    '''
#Second Page
@app.route("/page")
def page():
    return '''
    <head>
     <style>
            h1{
                color:red
            }
            body{
                background-color: blue;
            }
        </style>
    </head>
    <body>
        <h1>Hello page<h1>
    </body>
    '''
 #third page
@app.route("/apple")
def apple():
    return '''
    <head>
        <style>
        </style>
    </head>
    <body>
        <h1>Apples</h1>
    </body>
    '''
#fourth page
@app.route("/sprite")
def sprite():
    return '''
    <head>
        <style>
        </style>
    </head>
    <body>
        <h1>sprite</h1>
    </body>
    '''
#page five
@app.route("/happy")
def happy():
    return '''
    <head>
        <style>
        </style>
    </head>
    <body>
        <h1>Happy</h1>
    </body>
    '''



