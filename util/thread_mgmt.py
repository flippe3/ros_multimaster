import threading

class Thread_mgmt():
    def __init__(self, func, args):
        t = threading.Thread(target=func, args=args)
    
