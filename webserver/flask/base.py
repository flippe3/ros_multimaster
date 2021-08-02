from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def base(name=None):
    return render_template('base.html', name=name)

@app.route("/control.html")
def hello(name=None):
    return render_template('control.html', name=name)

app.run(debug=True)
