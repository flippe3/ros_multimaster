import sys
sys.path.append('util')
from network import Network
from terminal import Terminal
from multimaster import Multimaster
from process_mgmt import Subprocess

class Server:
    def __init__(self):
        # setup connection
        # print the initial setup (time sync etc.)
        
        # starts the network, scans for machines on the current
        # network, updates if a new machine wants to connect.
        self.network = Network(server=True)
        self.multimaster = Multimaster()
        self.multimaster.setup(debug=False)
        self.terminal = Terminal(self.multimaster)
        self.network.terminate_server()
        
    def connected_machines(self):
        p = Subprocess("rosservice call /master_discovery/list_masters")
        p.run(output=True)
        p.terminate()
        
    def recieve_data(self, topic):
        # start recieving data from a chosen topic
        return 0

    def publish_data(self):
        return 0 

    def offload(self):
        # should probably be its own class.
        return 0
    
    def command(self):
        # this will be the current interface for controlling the server
        # will be replaced by a web interface.
        return 0 

# for debugging
server = Server()
