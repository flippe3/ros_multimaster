import sys
sys.path.append('util')
from terminal import Terminal
from multimaster import Multimaster
from process_mgmt import Subprocess
from std_msgs.msg import String
import rospy

class Server:
    def __init__(self):
        # setup connection
        # print the initial setup (time sync etc.)
        
        # starts the network, scans for machines on the current
        # network, updates if a new machine wants to connect.
        #self.network = Network(server=True)
        #self.multimaster = Multimaster()
        #self.multimaster.setup(debug=True)
        #self.recieve_data("/test") # Have to put this in some kind of thread mgmt (probably a subprocess)
        #self.setup_command_clients()
        self.terminal = Terminal()
        #self.add_command_clients("192.168.0.179", 5004)
        #self.add_command_clients("192.168.0.201", 5005)
        #self.list_clients()
        #self.send_command_client("192.168.0.179", "ls -l ~/")
        #self.send_command_client("192.168.0.201", "roscore")
        #self.connected_machines()
        
        
    def connected_machines(self):
        p = Subprocess("rosservice call /master_discovery/list_masters")
        p.run(output=True)
        p.terminate()

    def recieve_data(self, topic):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber(topic, String, self.callback)
        rospy.spin()

    def callback(self):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
                
    def list_clients(self):
        print(self.server_sockets)
        
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
