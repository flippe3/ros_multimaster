import os

def cleanup_hosts():
    hosts = open("/etc/hosts", 'r')
    start = "### AUTOMATED NETWORK CONFIG ###"
    end = "### END ###"
    new_file = ""
    found = False
    for line in hosts.readlines():
        if start in line:
            found = True
        elif found == False:
            new_file += line
        elif found == True and end in line:
            found = False
    hosts.close()
    new_hosts = open("/etc/hosts", 'w')
    new_hosts.write(new_file)
    new_hosts.close()
    
