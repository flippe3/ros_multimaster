# ros_multimaster

The goal of this repo is to create a simple solution to dealing with multiple multimasters in ROS. The setup necessary will be provided in setup files and then to add a new machine to the network you only need to add the IP and all the /etc/hosts will be updated.

The network setup is from: https://digital.csic.es/bitstream/10261/133333/1/ROS-systems.pdf

## Current setup for a single ROS network (on linux)

Install multimaster-fkie
```
sudo apt-get install ros-melodic-multimaster-fkie
``` 
Put this in the `~/.bashrc` file with the IP of that machines IP.
```
export ROS_MASTER_URI=http://<hostname or IP address>:11311
``` 
Enable multicast
```
sudo sh -c "echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf"
```
Restart services
```
sudo service procps restart
```

## Current setup for multiple local ROS networks (on linux)

Install multimaster-fkie
```
sudo apt-get install ros-melodic-multimaster-fkie
``` 
Put this in the `~/.bashrc` file with the host IP.
```
export ROS_MASTER_URI=http://<hostname or IP address>:11311
``` 
Put this as a file in `/etc/netowrk/id-up.d` with the correct interface and the host IP. 
```
#!/bin/sh
if [ "$IFACE" = "<interface>" ]; then
  route add default gw <gateway IP address>
fi
```
Make that file executable
```
chmod a+x multimaster
```
(ONLY FOR HOST MACHINE) Enable IP forwarding 
```
sudo sh -c "echo net.ipv4_forward=1 >> /etc/sysctl.conf"
```
(ONLY FOR HOST MACHINE) Add a static route between networks (if multiple networks) 
where `<common network gateway>` is the host ip.
```
route add -net <local network> netmask 255.255.255.0 gw <common network gateway>
```
Enable multicast
```
sudo sh -c "echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf"
```
Restart services
```
sudo service procps restart
```
For all local ROS networks edit `/etc/hosts` on all machines to include the IP of every machine. 
Example:
```
192.168.0.201   drone1
192.168.0.221   turlebot
```
