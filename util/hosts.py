class Hosts():
    def __init__(self):
        self.start = "### AUTOMATED NETWORK CONFIG ###\n"
        self.end = "### END ###"
        
        self.cleanup()
        self.ip_list = []
        
    def cleanup(self):
        hosts = open("/etc/hosts", 'r')
        new_file = ""
        found = False
        for line in hosts.readlines():
            if self.start in line:
                found = True
            elif found == False:
                new_file += line
            elif found == True and self.end in line:
                found = False
        hosts.close()
        new_hosts = open("/etc/hosts", 'w')
        new_hosts.write(new_file)
        new_hosts.close()

    def find_duplicate(self, ip):
        hosts = open("/etc/hosts", 'r')
        lines = hosts.readlines()
        for i in lines:
            if ip in i:
                hosts.close()
                return True
        hosts.close()
        return False

    def write_ip_list(self):
        self.cleanup()
        hosts = open("/etc/hosts", 'a')
        
        hosts.write(self.start)
        count = 0
        for i in self.ip_list:
            hosts.write(i + "\t device" + str(count) + "\n")
            count += 1
        hosts.write(self.end)
            
    def add_new_device(self, ip):
        if self.find_duplicate(ip):
            print("[INFO] IP already exists")
        else:
            self.ip_list.append(ip)
            self.write_ip_list()
            
    def remove_device(self, ip):
        self.ip_list.remove(ip)
        self.write_ip_list()
            
