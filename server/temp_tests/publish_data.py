#!/usr/bin/env python
import rospy
from rospy_tutorials.msg import HeaderString

pub = rospy.Publisher('/test', HeaderString, queue_size=10)
rospy.init_node('publisher1')
r = rospy.Rate(30) # 10hz

while not rospy.is_shutdown():
    msg = HeaderString()
    msg.data = "test"
    msg.header.stamp = rospy.get_rostime()
    #now = rospy.get_rostime()
    #time = str(now.secs) + "." + str(now.nsecs)
    pub.publish(msg)
    r.sleep()
