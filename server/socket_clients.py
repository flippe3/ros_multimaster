from command_client import Command_Client

class Socket_Clients:
    def __init__(self):
        self.server_sockets = []
        
    def add_command_clients(self, ip, port):
        socket = Command_Client()
        connect_msg = socket.connect(ip, port)
        self.server_sockets.append((socket, ip))
        return connect_msg
        
    def send_command_client(self, socket, command):
        for i in self.server_sockets:
            if socket in i[0]:
                response = i[0].send_command(command)
                return response
