import sys
sys.path.append('util')
from process_mgmt import Subprocess

class Multimaster:
    def setup_multimaster(self, debug=False):
        print("***** Starting multimaster *****")
        # setting up the subprocesses
        self.roscore = Subprocess("roscore")
        self.master_discovery_fkie = Subprocess("rosrun master_discovery_fkie master_discovery _mcast_group:=224.0.0.1") 
        self.master_sync_fkie = Subprocess("rosrun master_sync_fkie master_sync")

        # runs the terminal comand
        self.roscore.run(output=debug)
        self.master_discovery_fkie.run(output=debug)
        self.master_sync_fkie.run(output=debug)
        print("***** Successfully started multimaster *****")

    def terminate_multimaster(self):
        self.roscore.terminate()
        self.master_discovery_fkie.terminate()
        self.master_sync_fkie.terminate()
        print("Terminated multimaster")
