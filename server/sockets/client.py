import socket

client_socket = socket.socket()
host = '192.168.0.201'
port = 1236

print('Waiting for connection')
try:
    client_socket.connect((host, port))
except socket.error as e:
    print(str(e))

response = client_socket.recv(1024)

while True:
    inp = input("Say Something: ")
    client_socket.send(str.encode(str(inp)))
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))

client_socket.close()
