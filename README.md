# login-and-sign-up-using-sqlite3-flask-python-and-html-css
Create New folder

Right click, open with terminal command prompt or gitbash. Then type

code .

Provide folders inside this project: templates and static

mkdir templates

mkdir static

Create file main.py. Type this

notepad main.py

Open the visual studio code

Inside static folder, Create file style.css

cd static

notepad style.css

Go back to up level

cd ..

Inside templates folder, Create file base.html. 

cd templates

notepad base.html

Copy and paste this file in base.html

<!doctype html>

<html lang="en">

  <head>

    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Welcome</title>

    <link rel="stylesheet" type=text/css href="{{ url_for('static', filename='style.css') }}">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">

  </head>

  <body>

{% block main %}



{% endblock %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>

  </body>

</html>

Inside templates folder, Create file index.html. Then type this code:

{% extends 'base.html' %}

{% block main %}

<h1>Hello, world!</h1>



{% endblock %}

Focus on main.py file. Copy and paste this code:

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')

def index():

    return render_template('index.html')

if __name__ == '__main__':

    app.run('0.0.0.0',8080)

Open new terminal in visual studio code, then install the following package in python (pip)

pip install flask

Next,

pip install db-sqlite3

Run the program, by typing this code

python main.py

end
