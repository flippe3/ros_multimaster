import sys, re
sys.path.append('util')
from process_mgmt import Subprocess
from multimaster import Multimaster
from socket_clients import Socket_Clients
# COMMAND LIST:
# all subcommands are given inside []
# exit : terminates the terminal
# connect [ip, port] : opens a socket and connects to it
# run [cmd, ip] : runs the cmd on the socket ip
# list sockets : lists the currently connected sockets
# help : shows this menu

class Terminal:
    def __init__(self):
        self.cmd_history = []
        print("[INFO] Starting terminal write q to quit")
        #self.multimaster = multimaster
        self.socket_clients = Socket_Clients()
        self.get_cmd()
        
    def get_cmd(self, cmd_string=None):
        if cmd_string == None:
            self.cmd_string = raw_input("> ")
            self.cmd = str(self.cmd_string).split(" ")
            if self.cmd[0] == "run":
                self.sub_cmd = re.findall('\[.*?\]', self.cmd_string)[0][1:-1]
        else:
            self.cmd_string = cmd_string
            self.cmd = str(self.cmd_string).split(" ")

            self.cmd_history.append(self.cmd_string)
        self.run_cmd()
        
    def run_cmd(self):
        exit_cmds = ["exit", "quit", "e", "q", "terminate", "kill"]

        if self.cmd_string in exit_cmds:            
            return
        else:
            try:
                if self.cmd[0] == "connect" and len(self.cmd) == 3:
                    self.socket_clients.add_command_clients(self.cmd[1], int(self.cmd[2]))

                elif self.cmd[0] == "run" and len(self.sub_cmd) != 0:
                    self.socket_clients.send_command_client(ip=self.cmd[-1], command=self.sub_cmd)

                elif self.cmd[0] == "list" and self.cmd[1] == "sockets":
                    print(self.socket_clients.server_sockets)

                elif self.cmd[0] == "help":
                    print("COMMAND LIST:")
                    print("all subcommands are given inside []")
                    print("exit : terminates the terminal")
                    print("connect [ip, port] : opens a socket and connects to it")
                    print("run [cmd, ip] : runs the cmd on the socket ip")
                    print("list sockets : lists the currently connected sockets")
                    print("help : shows this menu")

                else:
                    print("Unrecognized command: " + self.cmd_string)
                    print("Write help for a help menu.")
                
                self.get_cmd()

            except:
                print("Unrecognized command: " + self.cmd_string)
                print("Write help for a help menu.")
                self.get_cmd()
    def ros_cmds(self):
        self.ros_cmd = Subprocess(self.cmd_string)
        self.ros_cmd.run(output=True)
        
