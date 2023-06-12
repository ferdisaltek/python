from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def profile(name):
  return render_template("index.html", name=name)
    

if __name__=="__main__":
    #rune the app in debug mode to auto-reload
    app.run(debug=True)

    