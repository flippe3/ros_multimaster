from network import Network

class Server:
    def __init__(self):
        # setup connection
        # print the initial setup (time sync etc.)

        # starts the network, scans for machines on the current
        # network, updates if a new machine wants to connect.
        network = Network()

        self.setup_multimaster()
    
    def setup_multimaster(self):
        return 0

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

