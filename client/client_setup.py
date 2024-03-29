import sys
sys.path.append('util')
import os
import socket
from hosts import Hosts
import subprocess

class Client_Setup:
    def __init__(self, host_ip, interface, port):
        host = Hosts() # Cleans up the host file

        self.host_ip = host_ip
        self.interface = interface
        self.port = port
        self.first_setup()
        self.connect_server()
        
    def first_setup(self):
        try:
            ip = os.popen('ip addr show ' + self.interface).read().split("inet ")[1].split("/")[0]

            # Doesn't work
            # Only works for the local python env
            #os.environ['ROS_MASTER_URI'] = "http://" + str(ip) + ":11311"
            #os.environ['ROS_HOSTNAME'] = str(ip)

            hosts = open("/etc/hosts", "a")
            hosts.write("### AUTOMATED NETWORK CONFIG ###\n")
            hosts.write(str(self.host_ip) + "\thost\n")
            hosts.write(str(ip) + "\t" + str(socket.gethostname()))
            hosts.write("\n### END ###\n")

            multicast = int(subprocess.check_output("cat /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts", shell=True))
            if multicast == 1:
                os.system("sudo sh -c 'echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf'")
            os.system("sudo service procps restart")

        except IOError:
            print("ERROR, are you running this as root?")
            sys.exit()
        except IndexError:
            print("ERROR, have you configured the correct interface?")
            sys.exit()
            

    def connect_server(self):
        os.system("nc " + self.host_ip + " " + str(self.port))

try:
    c = Client_Setup(host_ip=sys.argv[1], interface=sys.argv[2], port=sys.argv[3])
except:
    print("Error, have you entered everything?")
    print("Example: sudo python3 client/client_setup.py 192.168.0.201 wlan0 5006")
