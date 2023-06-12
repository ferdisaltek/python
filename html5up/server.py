from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("C:/python_learn/python/html5up/templates/index.html")

    

if __name__=="__main__":
    #rune the app in debug mode to auto-reload
    app.run(debug=True)

    