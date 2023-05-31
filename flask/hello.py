from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'bye bye'

@app.route("/username/<name>/<int:number>")
def greeting(name,number):
    return f"hello there {name}, you are {number} years old!"
    

