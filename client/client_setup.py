import sys
sys.path.append('util')
import os
import socket
from wipe import cleanup_hosts

class Client_Setup:
    def __init__(self, host_ip, interface):
        cleanup_hosts()
        self.first_setup(host_ip, interface)

    def first_setup(self, host_ip, interface):
        try:
            os.system("export ROS_MASTER_URI=http://" + str(host_ip) + ":11311")
            ip = os.popen('ip addr show ' + interface).read().split("inet ")[1].split("/")[0]

            hosts = open("/etc/hosts", "a")
            hosts.write("### AUTOMATED NETWORK CONFIG ###\n")
            hosts.write(str(host_ip) + "\thost\n")
            hosts.write(str(ip) + "\t" + str(socket.gethostname()))
            hosts.write("\n### END ###\n")

            os.system("export ROS_HOSTNAME=" + str(ip))
            os.system("sudo sh -c 'echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf'")
            os.system("sudo service procps restart")

        except IOError:
            print("ERROR, are you running this as root?")
            sys.exit()
            
# for debugging
c = Client_Setup(host_ip="192.168.0.201", interface="wlp59s0")
