import threading
import os

class Thread_mgmt():
    def __init__(self, func, args):
        self.t = threading.Thread(target=func, args=args)

    def start(self):
        self.t.start()

    def get_pid(self):
        return os.getpid()        
    
    def terminate(self):
        # Wait for the thread to finish.
        self.t.join()

    
