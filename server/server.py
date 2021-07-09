import sys
sys.path.append('util')
from network import Network
from terminal import Terminal
from multimaster import Multimaster

class Server:
    def __init__(self):
        # setup connection
        # print the initial setup (time sync etc.)
        
        # starts the network, scans for machines on the current
        # network, updates if a new machine wants to connect.
        network = Network()

        multimaster = Multimaster()
        multimaster.setup(debug=True)
        terminal = Terminal(multimaster)
                        
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

