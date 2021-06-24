#!/usr/bin/env python

import socket
import threading

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
#    conn.close()
    
ip_list = []
threads = []
while True:
    c, addr = s.accept()
    ip_list.append(addr[0])
    print(ip_list)
    print("Threads", threading)
    print('Connection address:', addr)
    t = threading.Thread(target=on_new_client,args=(c,addr))
    t.start()
    threads.append(t)
s.close()
