# ros_multimaster

The goal of this repo is to create a simple solution to dealing with time synchronization between multiple multimasters in ROS. The setup necessary will be provided in setup files and then to add a new machine to the network you should only need to add the IP and all the /etc/hosts will be updated.

The network setup is from: https://digital.csic.es/bitstream/10261/133333/1/ROS-systems.pdf

## Setup server
#### Step 1. Start a network process
```
sudo python server/network.py
```
#### Step 2. Start the webserver
```
cd webserver/
```
```
export FLASK_APP=app
```
```
flask run
```
## Setup client
#### Step 1. Run network setup
```
sudo python3 client/client_setup.py <SERVER-IP> wlan0 5006
```
#### Step 2. Start all clients and close the program after every client is connected to the server.
```
sudo python network/client.py <SERVER-IP>
```

## Setup for a single ROS network (both hosts and clients)

#### Step 1. Install multimaster-fkie
```
sudo apt-get install ros-melodic-multimaster-fkie
``` 
or https://github.com/fkie/multimaster_fkie

#### Step 2. Put this in the `~/.bashrc` file with the IP of that machines IP.
```
export ROS_MASTER_URI=http://<hostname or IP address>:11311
``` 

## Setup NTP on host
Install NTP
```
sudo apt install ntp
```
Save `ntp.conf` in `/etc/ntp.conf`
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
Edit the `<host-ip>` with the host ip then save this in `/etc/chrony/chrony.conf` 
```
server <host-ip> minpoll 0 maxpoll 4 maxdelay .05
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
systemctl chrony stop
systemctl chrony start
```
For debugging
```
chronyc tracking
```
## Starting the multimaster (on both host and clients)
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
## Testing
#### Run publish_data.py or recieve_data.py on any machine.
```
python publish_data.py
python recieve_data.py
```
