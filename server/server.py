import sys
sys.path.append('util')
from network import Network
from terminal import Terminal
from multimaster import Multimaster
from process_mgmt import Subprocess
from hosts import Hosts

from std_msgs.msg import String
import rospy

class Server:
    def __init__(self):
        # setup connection
        # print the initial setup (time sync etc.)
        
        # starts the network, scans for machines on the current
        # network, updates if a new machine wants to connect.
        #self.network = Network(server=True)
        self.multimaster = Multimaster()
        self.multimaster.setup(debug=True)
        #self.recieve_data("/test") # Have to put this in some kind of thread mgmt (probably a subprocess)
        self.terminal = Terminal(self.multimaster)
        #self.connected_machines()
        
        self.network.terminate_server()
        
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
