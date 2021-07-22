# Manages the network connections between all machines.
# Also manages the new connections to the network.
import sys, os, time
sys.path.append('util')
#import socket
import threading
from gevent.server import StreamServer
from gevent.pool import Pool
import socket
from multiprocessing import Process
from hosts import Hosts

class Network:
    def __init__(self, port=5006, host_ip=None, server=True, interface="wlan0"):
        print("[INFO] Setting up network server")
        self.hosts = Hosts() # cleans up the network file
        self.ip_list = []
        self.interface = interface

        if server:
            self.host_ip = os.popen('ip addr show ' + self.interface).read().split("inet ")[1].split("/")[0]
            self.hosts.add_new_device(self.host_ip)
            self.ip_list.append(self.host_ip)
            print("[INFO] Host ip: " + str(self.host_ip))

            self.streamserver = StreamServer((self.host_ip, port), self.handle)
            self.process_serve_forever = Process(target=self.streamserver.serve_forever)
            self.process_serve_forever.start()
        print("[INFO] Setting up network successful")
            
    def handle(self, socket, address):
        if address[0] not in self.ip_list:
            self.ip_list.append(address[0])
            print(self.ip_list)
            
        self.hosts.add_new_device(address[0])
            
        socket.send("Connection successful")
        socket.close()

    def start_server_thread(self):
        return 0
    
    def terminate_server(self):
        self.streamserver.close()
        self.process_serve_forever.terminate()
        
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

network = Network(interface="wlp59s0")
