#!/usr/bin/env python
import rospy
from rospy_tutorials.msg import HeaderString

pub = rospy.Publisher('/test', HeaderString, queue_size=10)
rospy.init_node('publisher1')
r = rospy.Rate(1000) # 10hz

start_time = rospy.get_rostime()

while not rospy.is_shutdown() or  :
    msg = HeaderString()
    msg.data = "test"
    msg.header.stamp = rospy.get_rostime()
    pub.publish(msg)
    r.sleep()
