from flask import Flask, request, render_template, jsonify, session

import sys
sys.path.append('../../server')
sys.path.append('../../util')
from server import Server

app = Flask(__name__)

server = Server()

app.secret_key = "BAD_SECRET_KEY"

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

@app.route("/ros.html")
def ros(name=None):
    return render_template('ros.html', name=name)

@app.route("/server/", methods=['POST'])
def server_command(name=None):
    server_input = request.form['input_server'].strip()
    print("[Recieved server input] :", server_input.strip())
    output = server.terminal.send_cmd(server_input)
    print("Recieved output:", output)
    return render_template('index.html', server_output=output, name=name)

@app.route("/machine/", methods=['POST'])
def machine_command(name=None):
    machine_input = request.form['input_machine'].strip()
    print("[Recieved machine input] :", machine_input.strip())
    if session.get('selected_ip') != None:
        output=server.terminal.send_cmd(machine_input, session['selected_ip'])
    else:
        output = "No IP selected."
    print(output)
    return render_template('index.html', machine_output=output, name=name)

@app.route("/connect/", methods=['POST'])
def connection_command(name=None):
    ip_address = request.form['connection_ip']
    port = request.form['connection_port']
    print("[Recieved IP] :", str(ip_address), ":", str(port))
    command = "connect " + str(ip_address).strip() + " " + str(port).strip()
    output = server.terminal.send_cmd(command)
    return render_template('connection.html', connection=output, name=name)

@app.route("/list-connections/", methods=['POST'])
def list_connections_command(name=None):
    output = server.terminal.send_cmd("list sockets")
    return render_template('connection.html', list_connections=output, name=name)

@app.route("/list-connections/index/", methods=['POST'])
def list_connections_index_command(name=None):
    output = server.terminal.send_cmd("list sockets")
    return render_template('index.html', list_output=output, name=name)

@app.route("/list-connections/ros/", methods=['POST'])
def list_connections_ros_command(name=None):
    output = server.terminal.send_cmd("list sockets")
    return render_template('ros.html', list_output=output, name=name)

@app.route("/select_ip/", methods=['POST'])
def select_ip(name=None):
    ip_address = request.form['select_ip']
    print('Selected ip:', ip_address)
    return render_template('index.html', selected_ip=ip_address, name=name)

@app.route('/_set_ip')
def set_ip():
    ip = request.args.get('select_ip', "None",type=str)
    print("Setting the ip", ip)
    session['selected_ip'] = ip
    print("Session is set session[selected_ip]", session['selected_ip'])
    return jsonify(result=ip)

@app.route("/_refresh_connections")
def refresh_connections():
    output = server.terminal.send_cmd("list sockets")
    ip_list = []
    for i in output: ip_list.append(i[1])
    return jsonify(result=ip_list)

@app.route("/_refresh_topics")
def refresh_ros_topics():
    output = server.get_topics()
    print(output)
    topics = []
    for i in output:
        for j in i:
            topics.append(j)
    return jsonify(result=topics)

@app.route('/_set_topic')
def set_topic():
    topic = request.args.get('select_topic', "None",type=str)
    print("Setting the ros topic", topic)
    session['selected_topic'] = topic
    print("Session is set session[selected_topic]", session['selected_topic'])
    return jsonify(result=topic)

@app.route('/_get_topic_data')
def get_topic_data():
    session['selected_topic']
    return jsonify(result=topic)



if __name__ == '__main__':
    app.run(debug=True)
