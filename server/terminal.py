import sys, re
sys.path.append('util')

from process_mgmt import Subprocess
from multimaster import Multimaster
from socket_clients import Socket_Clients
from get_ip import get_ip

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
        self.server_ip = get_ip()
        self.ip = None
        self.socket_clients = Socket_Clients()
        
    def get_cmd(self, cmd_string=None):
        if cmd_string == None:
            self.cmd_string = input("> ")
            self.cmd = str(self.cmd_string).split(" ")
            if self.cmd[0] == "run":
                self.sub_cmd = re.findall('\[.*?\]', self.cmd_string)[0][1:-1]
        else:
            self.cmd_string = cmd_string
            self.cmd = str(self.cmd_string).split(" ")
            self.cmd_history.append(self.cmd_string)
        self.run_cmd()

    def send_cmd(self, cmd_string=None, socket=None):
        self.cmd_string = cmd_string.strip()
        self.socket = socket
        self.cmd = str(self.cmd_string).split(" ")
        if self.cmd[0] == "run":
            self.sub_cmd = str(re.findall('\[.*?\]', self.cmd_string)[0][1:-1])
        return self.run_cmd()
        
    def run_cmd(self):
        exit_cmds = ["exit", "quit", "e", "q", "terminate", "kill"]
        
        if self.cmd_string in exit_cmds:            
            return
        else:
            try:
                if self.cmd[0] == "connect" and len(self.cmd) == 3:
                    return self.socket_clients.add_command_clients(self.cmd[1], int(self.cmd[2]))

                elif self.cmd[0] == "run" and len(self.sub_cmd) != 0:
                    print("Running command on client")
                    return self.socket_clients.send_command_client(ip=self.cmd[-1], command=self.sub_cmd)

                elif self.cmd[0] == "list" and self.cmd[1] == "sockets":
                    s_sockets = self.socket_clients.server_sockets 
                    clean_socket = []
                    for i in s_sockets:
                        print(i[1], hex(id(i[0])))
                        clean_socket.append([hex(id(i[0])), i[1]])
                    return clean_socket                    
                
                elif self.cmd[0] == "help":
                    help_str = "COMMAND LIST:\n"
                    help_str += "all subcommands are given inside []\n"
                    help_str += "exit : terminates the terminal:\n"
                    help_str += "connect ip port : opens a socket and connects to it\n"
                    help_str += "run [cmd] ip : runs the cmd on the socket ip\n"
                    help_str += "list sockets : lists the currently connected sockets\n"
                    help_str += "help : shows this menu"
                    return help_str

                else:
                    if self.ip == None:
                        # Tries running the command on the server
                        p = Subprocess(self.cmd_string)
                        output = p.run(output=True, service=False)
                    else:
                        output = self.socket_clients.send_command_client(ip=self.ip, command=str(self.cmd_string))
                    return output

            except:
                err_msg = "ERROR: Unrecognized command: " + self.cmd_string + "\n"
                err_msg += "Write help for a help menu."
                print(err_msg)
                return err_msg


    def ros_cmds(self):
        self.ros_cmd = Subprocess(self.cmd_string)
        self.ros_cmd.run(output=True)
