import os

def cleanup_hosts():
    hosts = open("/etc/hosts", 'rw')
    start = "### AUTOMATED NETWORK CONFIG ###"
    for line in hosts.readlines():
        print(line)
        if start in line:
            
cleanup_hosts()
