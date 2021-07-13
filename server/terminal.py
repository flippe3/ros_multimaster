import sys
sys.path.append('util')
from process_mgmt import Subprocess
from multimaster import Multimaster

class Terminal:
    def __init__(self, multimaster):
        self.cmd_history = []
        print("[INFO] Starting terminal write q to quit")
        self.multimaster = multimaster
        self.get_cmd()
        
    def get_cmd(self):
        self.cmd_string = raw_input("> ")
        self.cmd = str(self.cmd_string).split(" ")

        self.cmd_history.append(self.cmd_string)
        self.run_cmd()

    def run_cmd(self):
        exit_cmds = ["exit", "quit", "e", "q", "terminate", "kill"]

        if self.cmd_string in exit_cmds:            
            self.multimaster.terminate()
            return
        else:
            if "ros" in self.cmd[0]:
                self.ros_cmds()
            elif self.cmd[0] in exit_cmds and self.cmd[1] == "multimaster":
                self.multimaster.terminate()
            self.get_cmd()

    def ros_cmds(self):
        self.ros_cmd = Subprocess(self.cmd_string)
        self.ros_cmd.run(output=True)
        
