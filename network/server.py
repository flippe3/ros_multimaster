#!/usr/bin/env python

import socket

TCP_IP = '192.168.1.106'
TCP_PORT = 5005
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connection address:', addr)
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print("received data:", data)
        f = open("ips.txt", "a")
        f.write("\n" + addr[0] + "\t" + data)
        f.close()
        conn.send(data)
    conn.close()
