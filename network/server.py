#!/usr/bin/env python

import socket
import thread

# This is the ip of the host.
TCP_IP = '192.168.1.106'
TCP_PORT = 5005
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

# Wipe ip file on boot
open('ips.txt', 'w').close()

def on_new_client(conn, addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print("received data:", data)

        # Makes sure that the data is not replicated
        fin = open("ips.txt", "r")
        ips = fin.read()
        new_ip = "\n"+addr[0]+"\t"+data
        fout = open("ips.txt", "a")
        fin.close()
        
        if addr[0] in ips:
            if new_ip in ips:
                fout.write(new_ip)
            else:
                lines = ips.split("\n")
                foverwrite = open("ips.txt", "w")
                for line in lines:
                    if addr[0] in line:
                        foverwrite.write(ips.replace(line, new_ip))
                foverwrite.close()
        else:
            fout.write(new_ip)
        fout.close()

        fin = open("ips.txt", "r")
        ips = fin.read()
        conn.send(ips)
        fin.close()
    conn.close()
    
while True:
    c, addr = s.accept()
    print('Connection address:', addr)
    thread.start_new_thread(on_new_client,(c,addr))
s.close()
