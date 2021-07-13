# Manages the network connections between all machines.
# Also manages the new connections to the network.
import sys
sys.path.append('util')
import socket
import time
import threading

class Network:
    def __init__(self, port=5005, host_ip=None, server=True):
        # clean up the old setup.
        print("[INFO] Running initial network setup")        
        self.threads = []
        self.setup(port, host_ip, server)
        if server:
            self.start_server()
        print("[INFO] Network initiated")        
        
    def setup(self, port, host_ip, server):
        # Gets the private ip for the current machine
        if server:
            self.TCP_IP = socket.gethostbyname_ex(socket.gethostname())[-1][1]
        else:
            self.TCP_IP = host_ip

        self.TCP_PORT = port
        self.buffer_size = 512

    def start_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.TCP_IP, self.TCP_PORT))
        self.s.listen(1)

        t = threading.Thread(target=self.start_server_thread)
        t.start()
        self.threads.append(t)

    def start_server_thread(self):
        while True:
            c, addr = self.s.accept()
            ip_list.append(addr[0])
        
    def terminate_server(self):
        return 0

    def new_connection(self, server_ip):
        # should be a thread to manage new connections
        return 0

    def get_connections(self):
        return 0
    
    def disconnect(self):
        return 0
    
    def update_connection():
        # update old connections
        return 0 
