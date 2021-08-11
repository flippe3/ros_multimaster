import sys
sys.path.append('util')
#from process_mgmt import Subprocess
import subprocess, time
import threading

class Multimaster:
    def __init__(self):
        self.roscore = threading.Thread(target=self.start_ros)
        print("[INFO] Starting roscore")
        self.roscore.start()
        time.sleep(1)
        
        self.discovery = threading.Thread(target=self.multimaster_discovery)
        print("[INFO] Starting multimaster discovery")
        self.discovery.start()
        time.sleep(1)

        self.sync = threading.Thread(target=self.multimaster_sync)
        print("[INFO] Starting multimaster sync")
        self.sync.start()
        time.sleep(1)
        
    def start_ros(self):
        subprocess.call(["roscore"], shell=True)
        
    def multimaster_discovery(self):
        subprocess.call(["rosrun master_discovery_fkie master_discovery _mcast_group:=224.0.0.1"], shell=True)

    def multimaster_sync(self):
        subprocess.call(["rosrun master_sync_fkie master_sync"], shell=True)


    
m = Multimaster()
