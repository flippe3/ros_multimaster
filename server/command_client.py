#!/usr/bin/python3
import socket
import sys

class Command_Client:
    def connect(self, ip, port):
        self.client_socket = socket.socket()        
        try:
            self.client_socket.connect((ip, port))
        except socket.error as e:
            print(str(e))
        self.response = self.client_socket.recv(1024)
        return self.response.decode('utf-8')
    
    def send_command(self, command):        
        self.client_socket.send(str.encode(command))    
        self.response = self.client_socket.recv(1024)
        return self.response.decode('utf-8')
            
    def terminate(self, ip, port):
        self.client_socket.close()
