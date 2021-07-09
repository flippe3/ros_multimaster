import sys
sys.path.append('util')
from multimaster import Multimaster

class Client:
    def __init__(self):
        multimaster = Multimaster()
        multimaster.setup_multimaster()

# for debugging
client = Client()
