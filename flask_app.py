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
@app.route("/results", method="POST")
def page():
    color_choice = request.form['color']
    fav_num = request.form['luck_num']
    fav_animal = request.form['fav_class']
    fav_movie = request.form['best_pix']

    return render_template('form_results.html', color = color_choice, luck_num = fav_num, fav_class = fav_animal, best_pix = fav_movie)
    '''
    <form action="/results" method="POST">
        <h2>Favorite Things</h2>
        <label>Favorite Color: <input type="text" name="color"/></label><br>
        <label>Favorite Number: <input type="number" name="luck_num"/></label><br>
        <label>Favorite Animal: <input type="text" name="fav_class"/></label><br>
        <label>Favorite Movie: <input type="text" name="best_pix"/></label><br>
        <button>Submit</button>
    </form>
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



