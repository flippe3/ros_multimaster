#!/usr/bin/python3

import socket
import sys

host = '192.168.0.201'
port = 5000

class Command_Client:
    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.threads = []
        self.socket_list = []
        
    def connect(self, ip, port):
        # This is not multi threaded.
        self.client_socket = socket.socket()
        self.socket_list.append(self.client_socket)

        try:
            self.client_socket.connect((ip, port))
        except socket.error as e:
            print(str(e))
        self.response = self.client_socket.recv(1024)

    def send_command(self, ip, port, command):        
        while True:
            self.client_socket.send(str.encode(command))    
            self.response = client_socket.recv(1024)
            print(self.response.decode('utf-8'))

    def terminate(self, ip, port):
        self.client_socket.close()
