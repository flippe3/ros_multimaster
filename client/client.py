import sys
sys.path.append('util')
from multimaster import Multimaster
from process_mgmt import Subprocess
import socket
import os
from command_server import Command_Server
import threading, time

class Client:
    def __init__(self, multimaster=True, roscore=True):
        self.setup_server()
        
    def setup_server(self):
        self.server = Command_Server(port=5007)
        self.server.start()

    #def start_ros(self):
    #    p = Subprocess("roscore")
    #    p.run(output=False, service=True)
    #    return p 

c = Client()
