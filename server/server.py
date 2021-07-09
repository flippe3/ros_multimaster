import sys
sys.path.append('util')
from network import Network
from process_mgmt import Subprocess

class Server:
    def __init__(self):
        # setup connection
        # print the initial setup (time sync etc.)

        # starts the network, scans for machines on the current
        # network, updates if a new machine wants to connect.
        network = Network()
        self.setup_multimaster()
        
    def setup_multimaster(self):
        # setting up the subprocesses
        self.roscore = Subprocess("roscore")
        self.master_discovery_fkie = Subprocess("rosrun master_discovery_fkie master_discovery _mcast_group:=224.0.0.1") 
        self.master_sync_fkie = Subprocess("rosrun master_sync_fkie master_sync")
        
        self.roscore.run()
        self.master_discovery_fkie.run()
        self.master_sync_fkie.run()
        print("Started multimaster")

    def terminate_multimaster(self):
        self.roscore.terminate()
        self.master_discovery_fkie.terminate()
        self.master_sync_fkie.terminate()
        print("Terminated multimaster")
        
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

