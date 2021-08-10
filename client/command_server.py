import sys
sys.path.append('util')
from process_mgmt import Subprocess
import socket
from get_ip import get_ip
from _thread import *

class Command_Server:
    def __init__(self, port=5000):
        self.server_socket = socket.socket()
        self.host = get_ip()
        self.port = port
        self.thread_count = 0
        try:
            self.server_socket.bind((self.host, self.port))
            print("[INFO] Command server running on " + str(self.host) + ":" + str(self.port))
        except socket.error as e:
            print(str(e))

    def threaded_client(self, connection):
        connection.send(str.encode('success ' + socket.gethostname()))
        while True:
            data = connection.recv(2048)
            # Run the command as a subprocess
            p = Subprocess(data.decode("utf-8"))
            result = p.run(output=True, service=False)
            p.terminate()
            reply = 'Result: ' + str(result.decode("utf-8"))
            if not data:
                break
            connection.sendall(str.encode(reply))
        connection.close()

    def start(self):
        self.server_socket.listen(5)
        print("[INFO] Waiting for a connection")
        while True:
            client, address = self.server_socket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.threaded_client, (client, ))
            self.thread_count += 1
            print('Thread Number: ' + str(self.thread_count))

    def terminate(self):
        self.server_socket.close()
