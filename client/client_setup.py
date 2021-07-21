import sys
sys.path.append('util')
import os
import socket
from wipe import cleanup_hosts

class Client_Setup:
    def __init__(self, host_ip, interface):
        cleanup_hosts()

        self.host_ip = host_ip
        self.interface = interface
        self.first_setup(host_ip, interface)
        self.connect_server()
        
    def first_setup(self)
        try:
            os.system("export ROS_MASTER_URI=http://" + str(self.host_ip) + ":11311")
            ip = os.popen('ip addr show ' + self.interface).read().split("inet ")[1].split("/")[0]

            hosts = open("/etc/hosts", "a")
            hosts.write("### AUTOMATED NETWORK CONFIG ###\n")
            hosts.write(str(self.host_ip) + "\thost\n")
            hosts.write(str(ip) + "\t" + str(socket.gethostname()))
            hosts.write("\n### END ###\n")

            os.system("export ROS_HOSTNAME=" + str(ip))
            os.system("sudo sh -c 'echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf'")
            os.system("sudo service procps restart")

        except IOError:
            print("ERROR, are you running this as root?")
            sys.exit()
        except IndexError:
            print("ERROR, have you configured the correct interface?")
            sys.exit()
            

    def connect_server(self):
        return 0

# for debugging
c = Client_Setup(host_ip="192.168.0.201", interface="wlan0")
