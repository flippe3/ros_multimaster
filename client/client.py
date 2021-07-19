import sys
sys.path.append('util')
from multimaster import Multimaster
import os

class Client:
    def __init__(self, host_ip):
        self.first_setup(host_ip)
        self.setup()
        
    def first_setup(self, host_ip):
        os.system("export ROS_MASTER_URI=http://" + str(host_ip) + ":11311")
        os.system("sudo sh -c 'echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf'")
        os.system("sudo service procps restart")
        
    def setup(self):
        multimaster = Multimaster()
        multimaster.setup()
        
# for debugging
client = Client(192.168.0.57)
