import sys
sys.path.append('util')
from multimaster import Multimaster
from process_mgmt import Subprocess
import socket
import os
from command_server import Command_Server
import threading, time

class Client:
    def __init__(self, port=5006):
        self.multimaster = Multimaster() # Starts roscore and multimaster
        self.setup_server()
        
    def setup_server(self, port):
        self.server = Command_Server(port=port)
        self.server.start()

try:
    c = Client(port=sys.argv[1])
except:
    print("Error did you start the program correctly?")
    print("Example: python3 client/client.py 5006")
