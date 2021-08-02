from flask import Flask, request
from flask import render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
@app.route("/index.html")
def base(name=None):
    return render_template('index.html', name=name)

@app.route("/control.html")
def hello(name=None):
    return render_template('control.html', name=name)

@app.route("/server/", methods=['POST'])
def server_command():
    server_input = request.form['input_server']
    print("[Recieved server input] :", server_input)
    return render_template('index.html')
