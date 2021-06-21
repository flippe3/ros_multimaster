#!/bin/bash

# only works for devices with two network modules
host_ip=$(hostname -i | awk '{print $2}')

# puts the hosts ip in the /etc/host file
echo -e $host_ip'\t'$(hostname) >> /etc/hosts

echo "export ROS_MASTER_URI=http://"$host_ip":11311" >> ~/.bashrc

source ~/.bashrc

echo "net.ipv4.icmp_echo_ignore_broadcasts=0" >> /etc/sysctl.conf
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf

service procps restart

# Setting default gateway for multiple computers ROS networks

#interface=$(iw dev | awk '$1=="Interface"{print $2}')
#if [ "$IFACE" = $interface ]; then
#   route add default gw $host_ip
#fi

#route add -net 192.168.11.0 netmask 255.255.255.0 gw $host_ip
