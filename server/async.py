from gevent.server import StreamServer

def handle(socket, address):
    print("IP connected:", address)
    socket.send("Connection successful")
    socket.close()

server = StreamServer(('192.168.0.57', 5000), handle)
server.serve_forever()
