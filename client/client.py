import sys
sys.path.append('util')
from process_mgmt import Subprocess

class Client:
    def __init__(self):
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
