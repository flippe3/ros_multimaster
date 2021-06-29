#!/usr/bin/env python

import socket

# This is the IP of the host
TCP_IP = '192.168.1.106'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str.encode(MESSAGE))

def check_duplicates(data):
    ips = data.split("\n")
    hosts = open("/etc/hosts", "r")
    print(ips)
    for i in ips:
        if i in hosts.read():
            print("duplicates")            
    hosts.close()
while True:
    data = s.recv(BUFFER_SIZE)
    print("received data:", data)
    hosts = open("/etc/hosts", "a")
    hosts.write(data)
s.close()
