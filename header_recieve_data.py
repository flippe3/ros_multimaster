import rospy
from rospy_tutorials.msg import HeaderString
import subprocess
import std_msgs

def callback(data):
    now = rospy.get_rostime()
    str_data =  data.data
    time = data.header.stamp
    convert_to_sec = (float(str(now)) - float(str(time)))*(10**-9)
    rospy.loginfo("Sent at %s Current time: %s \t difference %s ", time, now, convert_to_sec)
    
def listener():
    rospy.init_node('test_2')
    rospy.Subscriber("/test", HeaderString, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

#diff = get_time_difference()
listener()
