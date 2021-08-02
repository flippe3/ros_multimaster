from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index.html")
def base(name=None):
    return render_template('base.html', name=name)
@app.route("/control.html")
def hello(name=None):
    return render_template('control.html', name=name)
