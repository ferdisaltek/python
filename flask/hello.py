from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
            '<p> this is  a paragraph.</p>'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_emphasis
def say_bye():
    return 'bye bye'

@app.route("/username/<name>/<int:number>")
def greeting(name,number):
    return f"hello there {name}, you are {number} years old!"
    

if __name__=="__main__":
    #rune the app in debug mode to auto-reload
    app.run(debug=True)