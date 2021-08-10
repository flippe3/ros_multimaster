import sys
sys.path.append('util')
from terminal import Terminal
from multimaster import Multimaster
from process_mgmt import Subprocess
from std_msgs.msg import String
import threading
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

        # Hack that is the only way to start roscore before flask rn.
        self.t = threading.Thread(target=self.start_ros)
        self.t.start()
        
    def start_ros(self):
        p = Subprocess("roscore")
        p.run(output=False)
        return p 

    def recieve_data(self, topic):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber(topic, String, self.callback)
        rospy.spin()

    def callback(self):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
                
    def get_topics(self):
        return rospy.get_published_topics(namespace='/')

    def get_bandwidth(self, topic):
        return 
    #return rospy.set_param()
    
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
