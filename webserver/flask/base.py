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
def control(name=None):
    return render_template('control.html', name=name)

@app.route("/connection.html")
def connection(name=None):
    return render_template('connection.html', name=name)


@app.route("/server/", methods=['POST'])
def server_command():
    server_input = request.form['input_server']
    print("[Recieved server input] :", server_input)
    output = terminal.send_cmd(server_input)
    print("Recieved output:", output)
    return render_template('index.html', server_output=output)

@app.route("/machine/", methods=['POST'])
def machine_command():
    machine_input = request.form['input_machine']
    print("[Recieved machine input] :", machine_input)
    terminal.send_cmd(machine_input)
    return render_template('index.html')

@app.route("/connect/", methods=['POST'])
def connection_command():
    ip_address = request.form['connection_ip']
    port = request.form['connection_port']
    print("[Recieved IP] :", str(ip_address), ":", str(port))
    command = "connect " + str(ip_address).strip() + " " + str(port).strip()
    output = terminal.send_cmd(command)
    return render_template('/connection.html', connection=output)

@app.route("/list-connections/", methods=['POST'])
def list_connections_command():
    output = terminal.send_cmd("list sockets")
    return render_template('/connection.html', list_connections=output)

@app.route("/list-connections/index/", methods=['POST'])
def list_connections_index_command():
    output = terminal.send_cmd("list sockets")
    return render_template('/index.html', list_output=output)


if __name__ == '__main__':
    app.run(debug=True)
