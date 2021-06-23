# ros_multimaster

The goal of this repo is to create a simple solution to dealing with multiple multimasters in ROS. The setup necessary will be provided in setup files and then to add a new machine to the network you only need to add the IP and all the /etc/hosts will be updated.

The network setup is from: https://digital.csic.es/bitstream/10261/133333/1/ROS-systems.pdf

TODO:
* Create a solution that does not require every ip in /etc/hosts.

## Current setup for a single ROS network (on ubuntu) (`setup_client.sh` replaces step 2 and forward)

#### Step 1. Install multimaster-fkie
```
sudo apt-get install ros-melodic-multimaster-fkie
``` 
#### Step 2. Put this in the `~/.bashrc` file with the IP of that machines IP.
```
export ROS_MASTER_URI=http://<hostname or IP address>:11311
``` 
#### Step 3. Enable multicast
```
sudo sh -c "echo net.ipv4.icmp_echo_ignore_broadcasts=0 >> /etc/sysctl.conf"
```
#### Step 4. Restart services
```
sudo service procps restart
```
## Setup NTP on host
Install NTP
```
sudo apt install ntp
```
Save this in `ntp.conf` in `/etc/ntp.conf`
```
sudo cp ntp.conf /etc/ntp.conf
```
Start the service
```
sudo service ntp start
```

## Setup chrony on client
Install chrony
```
sudo apt install chrony
```
Save this in `/etc/chrony/chrony.conf`
```
server <host-ip> minpoll 2 maxpoll 4
initstepslew 2 <host-ip>
keyfile /etc/chrony/chrony.keys
commandkey 1
driftfile /var/lib/chrony/chrony.drift
maxupdateskew 5
dumponexit
dumpdir /var/lib/chrony
pidfile /var/run/chronyd.pid
logchange 0.5
rtcfile /etc/chrony.rtc
rtconutc
rtcdevice /dev/rtc
sched_priority 1
local stratum 10
allow 127.0.0.1/8
```
Synchronize with the server
```
sudo chrony stop
sudo chrony start
```
For debugging
```
chronyc tracking
```
## Starting the multimaster
Testing requires 4 terminals running on each machine. 
#### Start roscore on every machine
```
roscore
```
#### Start a master discovery
```
rosrun master_discovery_fkie master_discovery _mcast_group:=224.0.0.1
```
#### Start a master sync
```
rosrun master_sync_fkie master_sync
```
### Testing
#### Run publish_data.py or recieve_data.py on any machine.
```
python publish_data.py
python recieve_data.py
```
## Setup for multiple local ROS networks

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
