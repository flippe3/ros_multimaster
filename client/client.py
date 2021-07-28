import sys
sys.path.append('util')
from multimaster import Multimaster
from process_mgmt import Subprocess
import socket
import os
from _thread import *
from command_server import Command_Server

class Client:
    def __init__(self):
        #self.multimaster = Multimaster()
        #self.multimaster.setup(debug=True)
        self.setup_server()
        
    def setup_server(self):
        self.server = Command_Server(port=5004)
        self.server.start()

c = Client()
