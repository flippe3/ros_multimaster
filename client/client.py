import sys
sys.path.append('util')
from multimaster import Multimaster

class Client:
    def __init__(self):
        self.multimaster = Multimaster()
        self.multimaster.setup(debug=True)


c = Client()

