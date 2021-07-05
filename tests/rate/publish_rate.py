#!/usr/bin/env python
import rospy
from rospy_tutorials.msg import HeaderString
from std_msgs.msg import Int16


def send_header_msgs(rate): 
    pub = rospy.Publisher('/test', HeaderString, queue_size=10)
    rospy.init_node('Publisher1')
    r = rospy.Rate(rate)

    start_time = rospy.get_rostime()
    end_time = start_time + rospy.Duration(1)

    msg = HeaderString()
    msg.data = "test"
    msg.header.stamp = rospy.get_rostime()
    msg_count = 0 

    while not rospy.is_shutdown() and rospy.get_rostime() <= end_time:
        msg.header.stamp = rospy.get_rostime()
        pub.publish(msg)
        msg_count += 1
        r.sleep()
    msg = HeaderString()
    msg.data = str(msg_count)
    msg.header.stamp = rospy.get_rostime()
    pub.publish(msg)
    
    return msg_count

def send_int_msgs(rate):
    pub = rospy.Publisher('/test', Int16, queue_size=10)
    rospy.init_node('Publisher1')
    r = rospy.Rate(rate)

    start_time = rospy.get_rostime()
    end_time = start_time + rospy.Duration(1)
    msg_count = 0

    msg = 0
    msg_count = 0
    
    while not rospy.is_shutdown() and rospy.get_rostime() <= end_time:
        pub.publish(msg)
        msg_count += 1
        r.sleep()

    # Send end msg
    msg = msg_count
    pub.publish(msg)    
    
    return msg_count

data_type = int(input("Enter 0 for header messages or 1 for int messages: "))
data_rate = int(input("Enter the rate in Hz: "))

if data_type:
    print("Sent messages over 1 second: ", send_int_msgs(data_rate))
else:
    print("Sent messages over 1 second: ", send_header_msgs(data_rate))
