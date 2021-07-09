import sys
sys.path.append('util')
from process_mgmt import Subprocess

class Terminal:
    def __init__(self):
        self.cmd_history = []
        print("***** Starting terminal write q to quit *****")
        self.get_cmd()

    def get_cmd(self):
        self.cmd_string = raw_input("> ")
        self.cmd = str(self.cmd_string).split(" ")

        self.cmd_history.append(self.cmd_string)
        self.run_cmd()

    def run_cmd(self):
        exit_cmds = ["exit", "quit", "e", "q", "terminate"]

        if self.cmd_string in exit_cmds:
            
            return
        else:
            if "ros" in self.cmd[0]:
                self.ros_cmds()

            self.get_cmd()

    def ros_cmds(self):
        self.ros_cmd = Subprocess(self.cmd_string)
        self.ros_cmd.run(output=True)
        
