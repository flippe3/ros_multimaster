from flask import Flask, request
from flask import render_template

import sys
sys.path.append('../../server')
sys.path.append('../../util')
from terminal import Terminal

app = Flask(__name__)

terminal = Terminal()

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
    output = terminal.send_cmd(server_input)
    print("Recieved output:", output)
    return render_template('index.html', value=output)

@app.route("/machine/", methods=['POST'])
def machine_command():
    machine_input = request.form['input_machine']
    print("[Recieved machine input] :", machine_input)
    terminal.send_cmd(machine_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
